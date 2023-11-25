import os
import pyvista as pv
import numpy as np

input_folder = "train_stl"
output_folder = "train_images"

os.makedirs(output_folder, exist_ok=True)

# Función para convertir STL a PNG
def stl_to_png(stl_file, output_folder):
    try:
        # Leer el archivo STL
        mesh = pv.read(stl_file)
        
        # Verificar si la malla está vacía
        if mesh.n_points == 0:
            raise ValueError("La malla está vacía.")

        # Configurar el plotter para renderizado fuera de pantalla
        plotter = pv.Plotter(off_screen=True)
        plotter.add_mesh(mesh, color="white")  # Asumiendo que el color blanco es adecuado
        
        # Definir vectores de vista
        view_vectors = [
            (1, 0, 0),    # Vista lateral
            (0, 1, 0),    # Vista frontal
            (-1, 0, 0),   # Vista lateral opuesta
            (0, -1, 0),   # Vista trasera
            (0, 0, 1),    # Vista superior
            (0, 0, -1),   # Vista inferior
            (1, 1, 1),    # Vista diagonal
            (-1, -1, 1),  # Vista diagonal opuesta
            (1, -1, -1),  # Otra vista diagonal
            (-1, 1, -1),  # Otra vista diagonal opuesta
            (0.5, 0.5, 0), # Vista intermedia frontal-derecha
            (-0.5, 0.5, 0),# Vista intermedia frontal-izquierda
            (0.5, -0.5, 0),# Vista intermedia trasera-derecha
            (-0.5, -0.5, 0),# Vista intermedia trasera-izquierda
            (0.5, 0, 0.5), # Vista intermedia superior-derecha
            (-0.5, 0, 0.5),# Vista intermedia superior-izquierda
            (0.5, 0, -0.5),# Vista intermedia inferior-derecha
            (-0.5, 0, -0.5),# Vista intermedia inferior-izquierda
        ]
        
        # Recorrer cada vector de vista y guardar la captura de pantalla
        for view_vector in view_vectors:
            plotter.view_vector(view_vector)
            file_name = f"{os.path.splitext(os.path.basename(stl_file))[0]}_{view_vector}.png"
            plotter.screenshot(os.path.join(output_folder, file_name))

    except Exception as e:
        print(f"Error procesando archivo {stl_file}: {e}")

# Procesar todos los archivos STL en el folder
for file in os.listdir(input_folder):
    if file.endswith('.stl'):
        stl_path = os.path.join(input_folder, file)
        stl_to_png(stl_path, output_folder)