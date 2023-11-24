# Informes para el ptoyecto final Machine Learning UPC

![Logo UPC](https://th.bing.com/th/id/OIP.uI-98YWzIvsuhXVyKRkv9gHaHk?pid=ImgDet&rs=1)

## Integrantes
#### - Humbser Meza, Diego Fernando		u202012711
#### - Charapaqui Reluz, Alcides Rommel		u202021294
#### - Llaguento de la Cruz, Marlon Omar		u20201B055

# Tarea Académica 3: Desarrollo Integral de GAN para la Transformación de Modelos 3D

# Introducción

La transición de diseños digitales a objetos físicos mediante la impresión 3D es un proceso que combina precisión técnica con creatividad. Comienza con la elección de modelos tridimensionales, como camas en el formato .OFF, un estándar para geometrías 3D detalladas. Estos modelos son transformados en BinVoxels, una representación voxelizada que optimiza la manipulación de los datos en tres dimensiones.

Mediante la implementación de Redes Generativas Antagónicas (GAN), tecnologías de aprendizaje profundo avanzadas, se procesan y generan nuevos modelos en Bin Voxels. Este proceso permite la creación de variantes estructuradas y refinadas de los modelos originales, demostrando las capacidades predictivas y creativas de la GAN.

El último paso es convertir estos modelos generados en formato .STL, esencial para la impresión 3D. Este formato permite una transferencia precisa de los modelos digitales a la impresora 3D, culminando así el proceso de diseño y fabricación digital. La metodología establece una fusión entre el modelado avanzado y la manufactura aditiva, una verdadera representación de cómo los conceptos se materializan en el mundo real.


## Configuración del Entorno de Entrenamiento

### Repositorio:
- **Creación del Repositorio**
  - Implementar un repositorio en GitHub o similar, con una estructura clara.
  - Incluir directorios separados para scripts, datasets, documentación y resultados de entrenamiento.
- **Gestión con Issues**
  - Asignar tareas detalladas utilizando issues.
  - Categorizar issues con etiquetas por urgencia, tipo (bug, mejora, tarea), y asignar responsables.
- **Definición de Milestones**
  - Establecer milestones para reflejar el progreso cronológico.
  - Definir fechas específicas y objetivos a corto y largo plazo.

### Gestión de Tareas

#### Objetivos:

- **Definición de Milestones**
  - Establecer hitos que indiquen progresos importantes como la adquisición de datos, conversión de datos, y fases iniciales de entrenamiento y prueba de la GAN.

- **Búsqueda y Adquisición de Dataset**
  - Descargar [ModelNet10](https://vision.princeton.edu/projects/2014/3DShapeNets/ModelNet10.zip), enfocándose en modelos 3D de camas en formato .off.

- **Conversión de Datos**
  - Transformar modelos 3D de camas de .off a Binvoxels, y luego a STL.

- **Preparación para la GAN**
  - Crear una primera versión de la GAN que utilice datos STL para generar nuevos modelos 3D de camas.
  - Desarrollar la arquitectura inicial de la GAN, seleccionando hiperparámetros adecuados.
  - Implementar una pipeline de datos que gestione la entrada/salida de modelos 3D y se encargue del preprocesamiento y normalización de los mismos.

## Metodología

La transformación y procesamiento de modelos 3D comienza con modelos en formato .OFF, específicamente de camas, que representan el punto de partida de nuestro flujo de trabajo. Estos modelos 3D son transformados a un formato intermedio o representación de voxelización conocida como "BinVoxels".

![diagrama del modelo](https://cdn.discordapp.com/attachments/1159637113541759146/1177698207573217341/ditfFBumg.png?ex=657373ed&is=6560feed&hm=34de3fbebdc0412c6828b66c2e16a1daab1f50b30790425c72acc220a1bdba57&)

A continuación, los BinVoxels se utilizan como entrada para una Red Generativa Antagónica (GAN), que procesa los datos y genera un nuevo modelo 3D en formato Bin Voxels. Este nuevo modelo generado se convierte finalmente al formato .STL, que es un estándar comúnmente utilizado para la impresión 3D y otras aplicaciones de modelado 3D.

![Vizualización del stl](https://cdn.discordapp.com/attachments/1159637113541759146/1177720245608267806/bed_0001_0.5_-0.5_0_3.png?ex=65738873&is=65611373&hm=382008d12db50d9675c04b8dfa49d0c91a2cf0725c42332a6123e6dc6d98de93&)

# Impresión 3D

El software utilizado para la impresión y visualización del resultado en formato .stl es PrusaSlicer 2.7.0. A continuación, se presentan imágenes que muestran el proceso y el resultado final:

![Bed.stl](https://cdn.discordapp.com/attachments/1159637113541759146/1177725721519591556/image.png?ex=65738d8d&is=6561188d&hm=4d80a46dca56054fae3a1771c064bedbbcbcdc6bd393eaed010d7eab87413998&)

En la siguiente imagen se puede apreciar un soporte para la impresión generado por el mismo software:

![3d model with supports](https://cdn.discordapp.com/attachments/1159637113541759146/1177726994859962388/image.png?ex=65738ebc&is=656119bc&hm=3da52e78c7ee0d25172e8163f393943c146f32d8e4588da65df030fa9a0d6a39&)

Una vez preparado el modelo, se procede a exportarlo en formato .gcode, que es el utilizado para la impresión 3D en las máquinas de la UPC.

![foto UPC](https://cdn.discordapp.com/attachments/1159637113541759146/1177729941383680120/IMG_0097_3.jpg?ex=6573917b&is=65611c7b&hm=b25d688b3e1b3b39c170f3a75494aae95b0619bcba5d8e3501fe4f9a75331da5&)
