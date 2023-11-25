from stl import mesh
import numpy as np

def stl_to_array(file_path):
    mesh_data = mesh.Mesh.from_file(file_path)
    vertices = mesh_data.vectors.reshape((-1, 3))
    stl_array = np.array(vertices)
    return stl_array

stl_file_path = 'tu_archivo.stl'

stl_array = stl_to_array(stl_file_path)

print(stl_array)