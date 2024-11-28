'''DESCRIPCION:
ESTE CODIGO PERMITE NORMALIZAR LA IMAGEN EN UN VECTOR O MATRIZ PARA SU POSTERIOR ALMACENAMIENTO'''
from src.constants.lib import *##IMPORTA LAS LIBRERIAS
from src.constants.imt import *#IMPORTA EL ARCHIVO DE LA IMAGEN DEL MAPA
def actualizacion_mapa():
    lx = 2245 ###ESTE PARAMETRO NO SE DEBE MOVER YA QUE ES EL ESCALADO DEL MAPA DE RUTAS
    ly = 3179 ###MISMO CASO PARA ESTE, ES MEJOR DEJARLOS ASI
    a = np.array(Image.open('med.png').convert('L'))/255####ACA SE ABRE LA IMAGEN PARA NORMALIZAR
    #a = matriz #ACTIVAR ESTA LINEA SI DESEA PROBAR SI LA IMAGEN DEL MAPA LA CARGO POR PRIMERA VEZ   
    for x in range (lx): ###ESTE BUCLE ES EL ENCARGADO DE FILTRAR LAS RUTAS POR UN FACTOR DE OPACIDAD, PARA QUE NO SE TOMEN EN CUENTA GRADIENTES DE SOMBRA
        for y in range(ly):
            if a[y][x] <= 0.4:###ENTRE MAS ALTO SE PONGA ESTE PARAMETRO MAS SE DESPRECIARAN RUTAS DE BAJA OPACIDAD
                a[y][x] = 1
            else:
                a[y][x]=0
    print("Listo")
    mi = a ### VARIABLE ARBITRARIA PARA ASIGNAR LA IMAGEN YA VECTORIZADA 
    plt.imshow(mi, cmap='jet')###MAPEA LA IMAGEN
    plt.show()####MUESTRA EL MAPA
    mi = mi*255###debemos hacer esto para devolver el formato original a la imagen
    mi = Image.fromarray(mi.astype(np.uint8))#se pasa un imagen tipo array a una imagen tipo jpg
    mi.save('med.png')##nombre con el que se guardara el archivo entre comillas
######EJES COORDENADOS
##PARAMETROS ARBITRARIOS PARA INTERPOLACION GEOMETRICA
def mat_to_geo (pix,piy):
    con_lon = (pix/29655.657) - 75.619
    con_lat = (piy/26356.94) + 6.3061
    return con_lon,con_lat
def geo_to_mat (long,lat):
    pix = (75.619+long)*29655.657
    piy = -(-6.3061+lat)*26356.94 
    return pix,piy