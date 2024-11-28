from lib import *
from PIL import Image
imagen = Image.open('med.jpg')
imagen = imagen.convert('L')
matriz = np.array(imagen)/255
