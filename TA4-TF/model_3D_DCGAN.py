import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from stl import mesh
from shapely.geometry import Polygon, MultiPoint
from shapely.ops import triangulate
from scipy.spatial import Delaunay
import os

def build_generator(latent_dim):
    model = models.Sequential()

    model.add(layers.Dense(8 * 8 * 8 * 64, input_dim=latent_dim))
    model.add(layers.Reshape((8, 8, 8, 64)))

    model.add(layers.Conv3DTranspose(64, kernel_size=(3, 3, 3), strides=(2, 2, 2), padding='same'))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU(alpha=0.2))

    model.add(layers.Conv3DTranspose(32, kernel_size=(3, 3, 3), strides=(2, 2, 2), padding='same'))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU(alpha=0.2))

    model.add(layers.Conv3DTranspose(1, kernel_size=(3, 3, 3), padding='same', activation='tanh'))

    return model

def build_discriminator(input_shape):
    model = models.Sequential()

    model.add(layers.Conv3D(32, kernel_size=(4, 4, 4), strides=(2, 2, 2), padding='same', input_shape=input_shape))
    model.add(layers.LeakyReLU(alpha=0.2))

    model.add(layers.Conv3D(64, kernel_size=(4, 4, 4), strides=(2, 2, 2), padding='same'))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU(alpha=0.2))

    model.add(layers.Conv3D(128, kernel_size=(4, 4, 4), strides=(2, 2, 2), padding='same'))
    model.add(layers.BatchNormalization())
    model.add(layers.LeakyReLU(alpha=0.2))

    model.add(layers.Flatten())
    model.add(layers.Dense(1, activation='sigmoid'))

    return model

data_dir = 'Dataset-bed-stl-test'

stl_objects = []

stl_objects = []
a = 0

for filename in os.listdir(data_dir):
    if filename.endswith(".stl"):
        stl_mesh = mesh.Mesh.from_file(os.path.join(data_dir, filename))
        vertices = stl_mesh.vectors.reshape((-1, 3))

        
        polygon = Polygon(vertices)
        simplified_polygon = polygon.simplify(0.001)

        if isinstance(simplified_polygon, Polygon):
            triangles = np.array(triangulate(simplified_polygon))
        else:
            triangles_list = []
            for polygon in simplified_polygon:
                triangles = np.array(triangulate(polygon))
                triangles_list.append(triangles)

            triangles = np.concatenate(triangles_list)

        normalized_vertices = triangles[a].normalize()
        
        print(normalized_vertices)
        a+=1
        stl_objects.append(normalized_vertices)

      # Asegurarse de que todas las secuencias tengan la misma longitud
max_length = max(len(obj) for obj in stl_objects)
stl_objects = np.array([np.pad(obj, ((0, max_length - len(obj)), (0, 0)), mode='constant', constant_values=0) for obj in stl_objects])

# Tamaño del lote y dimensionalidad del espacio latente
batch_size = 64
latent_dim = 100

# Crear el generador y el discriminador
generator = build_generator(latent_dim)
discriminator = build_discriminator((64, 64, 64, 1))

# Compilar el discriminador
discriminator.compile(loss='binary_crossentropy', optimizer=tf.keras.optimizers.Adam(lr=0.0002, beta_1=0.5), metrics=['accuracy'])

# Congelar el discriminador durante el entrenamiento del generador
discriminator.trainable = False

# Construir la GAN
gan_input = tf.keras.Input(shape=(latent_dim,))
generated_object = generator(gan_input)
gan_output = discriminator(generated_object)
gan = tf.keras.Model(gan_input, gan_output)

# Compilar la GAN
gan.compile(loss='binary_crossentropy', optimizer=tf.keras.optimizers.Adam(lr=0.0002, beta_1=0.5))

# Función para entrenar la GAN
def train_gan(epochs, batch_size):
    batch_count = stl_objects.shape[0] // batch_size

    for epoch in range(epochs):
        for _ in range(batch_count):
            noise = np.random.normal(0, 1, size=(batch_size, latent_dim))


            generated_objects = generator.predict(noise)

            real_objects_idx = np.random.randint(0, stl_objects.shape[0], batch_size)
            real_objects = stl_objects[real_objects_idx]

            labels_real = np.ones((batch_size, 1))
            labels_fake = np.zeros((batch_size, 1))


            d_loss_real = discriminator.train_on_batch(real_objects, labels_real)

            d_loss_fake = discriminator.train_on_batch(generated_objects, labels_fake)

            d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)

            noise = np.random.normal(0, 1, size=(batch_size, latent_dim))

            labels_gan = np.ones((batch_size, 1))

            g_loss = gan.train_on_batch(noise, labels_gan)

        # Imprimir métricas de pérdida cada cierto número de épocas
        if epoch % 10 == 0:
            print(f"Epoch {epoch}, Discriminator Loss: {d_loss[0]}, Generator Loss: {g_loss}")

# Entrenar la GAN
train_gan(epochs=100, batch_size=batch_size)