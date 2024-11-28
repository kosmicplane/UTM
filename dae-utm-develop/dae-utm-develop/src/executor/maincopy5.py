from ...data.dataset import *
from src.constants.lib import *
import os
import sys
##VARIABLES DE UTILIDAD
global ll, coordenadas, co, f1, f2, i,i_e,i_guide
coordenadas = []
co = []
i_guide = []
f1 = []
i,i_e,f2 = 0,0,[]
ll = np.array(Image.open('med1.png'))
w = open('mimi.txt','w')
###FUNCIONES PRINCIPALES
def actualizar_treeview():
    # Código para actualizar los elementos del Treeview
    # Puedes obtener los nuevos elementos de la lista aquí
    # Borrar todos los elementos actuales del Treeview
    treeview.delete(*treeview.get_children())
    # Agregar los nuevos elementos al Treeview
    for i, elemento in enumerate(mf):
        treeview.insert('', 'end', text=str(i+1), values=tuple(elemento))
    # Volver a programar la actualización del Treeview en 1 minuto
    threading.Timer(60, actualizar_treeview).start()
def redefine_mf():
    global mf
    global mv
    mf = []
    mv = []
    mf1 = vuelos_radar()
    mf1 = list(mf1)
    for i in  range(len(mf1)):
        mf.append(0)
        mv.append(0)
    for i in range(len(mf1)):
        mf[i]=[mf1[i][1],mf1[i][2],mf1[i][5],mf1[i][6]]
        mv[i]=[mf1[i][5],mf1[i][6]]
    for i in range(len(mv)):
        mv[i][0] = round((mv[i][0]+79.32644)/0.02787)
        mv[i][1] = round((mv[i][1]-12.617)/-0.027)
    threading.Timer(30, redefine_mf).start()
def guardar_coordenada(event):
    x = (((event.x)*(5.011160714))/29655.657) - 75.619
    y = (((-event.y)*(5.014195584))/26356.94) + 6.3061
    lon = x
    lat = y
    meteo_list = meteoroligal_values(lat,lon)
    altura = get_altitude(y,x)
    for i in ([altura,lat,lon]):
        meteo_list.append(i)
    treeview1.insert('', 'end', text=0, values=(meteo_list))
    return 
def cerrar():#FUNCION PARA CERRAR EL PROGRAMA
    ventana.destroy()
    sys.exit()
def mostrar_valores(event):
    x = int(event.x*5.011)
    y = int(event.y*5.014)
    x = (((event.x)*(5.011160714))/29655.657) - 75.619
    y = (((-event.y)*(5.014195584))/26356.94) + 6.3061
    valor = obtener_valor_en_posicion(x, y)
    etiqueta_valor.config(text=f"Valor: {valor} y  \n {event.x*5.011} y {event.y*5.014}")
def obtener_valor_en_posicion(x, y):
    return "(Latitud: {}, Longitud: {})".format(y, x)
def mostrar_coordenadas(event):
    x = event.x
    y = event.y
    x =  0.02787*x - 79.32644
    y = -0.027*y + 12.617
    etiqueta_coordenadas.config(text=f"Coordenadas: longitud: {x}, latitud: {y}")
def update_image():
    image_copy = image.copy()
    draw = ImageDraw.Draw(image_copy)
    indicator = Image.open("avion.png").convert("RGBA")
    indicator = indicator.resize((40, 40))
    # Dibujar todos los puntos almacenados en la lista
    draw = ImageDraw.Draw(image_copy)
    for x,y in mv:
        indicator_width, indicator_height = indicator.size
        x -= indicator_width // 2
        y -= indicator_height // 2
        image_copy.paste(indicator, (x, y), indicator)
    photo = ImageTk.PhotoImage(image_copy)
    # Actualizar el lienzo de la imagen en la interfaz
    canvas.itemconfig(image_item, image=photo)
    canvas.image_copy = photo
    threading.Timer(5, update_image).start()
def path_builder(event):
    global coordenadas, i ,co, i_e
    if i > 1:
        reset()
    xi = event.x
    yi = event.y
    co.append(round(5.014195584*yi))
    co.append(round(5.011160714*xi))
    xi = 0.00011904*xi -75.60119
    yi = -0.00019011*yi + 6.306028
    i = i + 1
    coordenadas.append(yi)
    coordenadas.append(xi)
    if i == 2:
        treeview2.insert('', 'end', values=tuple(coordenadas))
        i_e = 0
def launch():
    #FILTRO 1
    global co,f1,f2, i_e, l_c,g_pnt,gx,gy,co2
    print("arrancamos")
    red()
    i_g = []
    i = 0
    co2 = [0,0]
    while co[0]!=co[2] and co[1]!=co[3]:
        l_c = []
        l_cd = []
        for y in range (-3,4,1):
            for x in range (-3,4,1):
                i_x = co[1] + x
                i_y = co[0] + y
                if i_x == co[0] and i_y == co[1]:
                    None
                else: 
                    if ll[i_y][i_x][0]==255:
                        d = 0.3333*(abs(i_y-co[2])+abs(i_x-co[3]))
                        d1 = 0.3333*((abs(i_y-co[2])**2+abs(i_x-co[3])**2)**0.5)
                        d2 = 0.3333*(abs(i_y-gy)+abs(i_x-gx))
                        dt = d + d1 + d2
                        l_c.append([i_y,i_x])
                        l_cd.append(dt)
                        if co2[0] == l_c[l_cd.index(min(l_cd))][0] and co2[1] == l_c[l_cd.index(min(l_cd))][1]:
                            print(dt,d2,d1,d,l_c)
                        else:
                            co2[0] = co[0]
                            co2[1] = co[1]
                            co[0] = l_c[l_cd.index(min(l_cd))][0]
                            co[1] = l_c[l_cd.index(min(l_cd))][1]
                        i_g.append([co[0],co[1]])
                        gps.config(text=str(f"ubicacion del dron{co}"))
        i = i + 1    
    else:
        w.write(str(i_g))
        print("done")
def reset():
        global i
        coordenadas.clear()
        co.clear
        i_guide.clear()
        treeview2.delete(*treeview2.get_children())
        i  = 0
def r_g_b(l):
    global color_abs
    color_abs = (l[0] + l[1] + l[2])/255
    if color_abs > 0.5:
        return 1
    else:
        print("invalid SELECTION")
        return 0
def red(heigth: float) -> dict:
    global ava,ll,co, g_pnt,g_d,gx,gy
    ava = [] 
    ava_min = []
    g_pnt = []
    g_d = []
    ix = co[1]
    iy = co[0]
    ix1 = co[3]
    iy1 = co[2]
    for y in range(len(ll)):
        for x in range(len(ll[0])):
            if ll[y][x][0] == 255:
                ava.append([y,x])
                d = abs(ix-x)+abs(iy-y)
                ava_min.append(d)
    i_ava = ava[ava_min.index(min(ava_min))]
    co[0] = i_ava[0]
    co[1] = i_ava[1]
    ava.clear()
    ava_min.clear()
    for y in range(len(ll)):
        for x in range(len(ll[0])):
            if ll[y][x][0] == 255:
                ava.append([y,x])
                d = abs(ix1-x)+abs(iy1-y)
                ava_min.append(d)
    i_ava = ava[ava_min.index(min(ava_min))]
    co[2] = i_ava[0]
    co[3] = i_ava[1]
    for y in range(len(ll)):
        for x in range(len(ll[0])):
            ar = ll[y][x][0]
            ag = ll[y][x][1]
            ab = ll[y][x][2]
            if ar == 255 and ag == 255 and ab == 0:
                g_pnt.append([y,x])
                gy = abs(y-co[2])
                gx = abs(x-co[3])
                g_d.append([gy+gx])
    gx = g_pnt[g_d.index(min(g_d))][1]
    gy = g_pnt[g_d.index(min(g_d))][0]
    print(co,"nuevos vectores",gy,gx)
def coco():
    thread1.start()
ventana = tk.Toplevel()
redefine_mf()#retirarlo por falla de api opensky
treeview = ttk.Treeview(ventana, columns=('columna1', 'columna2', 'columna3','columna4'), height=1)
treeview.heading('#0', text='Índice')
treeview.heading('columna1', text='MATRICULA')
treeview.heading('columna2', text='PAIS')
treeview.heading('columna3', text='LONGITUD')
treeview.heading('columna4', text='LATITUD')
treeview.column('#0', width=50)
treeview.column('columna1', width=100)
treeview.column('columna2', width=100)
treeview.column('columna3', width=100)
treeview.column('columna4', width=100)
##puntos de inicio y partida
treeview2 = ttk.Treeview(ventana, columns=('col1', 'col2', 'col3', 'col4'), height=1)
treeview2.heading('#0', text='in')
treeview2.heading('col1', text='lat origen')
treeview2.heading('col2', text='lon origen')
treeview2.heading('col3', text='lon origen')
treeview2.heading('col4', text='lon destino')
treeview2.column('#0', width=20)
treeview2.column('col1', width=100)
treeview2.column('col2', width=100)
treeview2.column('col3', width=100)
treeview2.column('col4', width=100)
actualizar_treeview()#retirarlo por falla de api opensky
treeview1 = ttk.Treeview(ventana, columns=('c1', 'c2', 'c3','c4','c5','c6','c7','c8','c9','c10','c11'), height=1)
treeview1.heading('#0', text='indice')
treeview1.heading('c1', text='CIUDAD')
treeview1.heading('c2', text='CLIMA')
treeview1.heading('c3', text='Desc')
treeview1.heading('c4', text='°C')
treeview1.heading('c5', text='Kpa')
treeview1.heading('c6', text='m/s')
treeview1.heading('c7', text='Hum%')
treeview1.heading('c8', text='Visc')
treeview1.heading('c9', text='Alt')
treeview1.heading('c10', text='lat')
treeview1.heading('c11', text='lon')
treeview1.column('#0', width=20)
treeview1.column('c1', width=60)
treeview1.column('c2', width=60)
treeview1.column('c3', width=60)
treeview1.column('c4', width=40)
treeview1.column('c5', width=50)
treeview1.column('c6', width=40)
treeview1.column('c7', width=50)
treeview1.column('c8', width=50)
treeview1.column('c9', width=55)
treeview1.column('c10', width=55)
treeview1.column('c11', width=50)
####TEXTO FIJO EN EL MODULO
etiqueta_texto = tk.Label(ventana, text="BIENVENIDO A LA INTERFAZ DE CONTROL DE VARIABLES PARA RUTAS DE DRONES")
etiqueta_texto.place(x=20,y=20)
title = tk.Label(ventana, text = "INFORMACION DE LAS AERONAVES EN VUELO")
gps = tk.Label(ventana, text="UBICACION DEL DRON")
guide = tk.Label(ventana, text="BIENVENIDO A LA INTERFAZ, EN EL MAPA DE LA DERECHA PUEDE HACER CLICK IZQUIERDO PARA CONOCER \n INFORMACION ATMOSFERICO O CLICK DERECHO EN DOS PUNTOS PARA INICIAR UNA RUTA")
gps.place(x=500,y=280)
###aca solo se carga el mapa de rutas
imagen_original = Image.open("med.jpg")
imagen_original = imagen_original.resize((224*2, 317*2))
ancho, alto = imagen_original.size
imagen_tk = ImageTk.PhotoImage(imagen_original)
lienzo = tk.Canvas(ventana, width=ancho, height=alto)
imagen_lienzo = lienzo.create_image(0, 0, image=imagen_tk, anchor=tk.NW)
lienzo.place(x=20,y=40)
etiqueta_valor = tk.Label(ventana, text="Valor: ")
etiqueta_valor.place(x=20,y=700)
lienzo.bind("<Motion>", mostrar_valores)
lienzo.bind("<Button-1>", guardar_coordenada)
lienzo.bind("<Button-3>", path_builder)
###configuracion de los botones
cerrar_option = tk.Button(ventana, text="OPRIMA ACA PARA CERRAR EL CODIGO", command=cerrar)
lanzar = tk.Button(ventana, text="INICIAR", command=coco)
####HILOS
thread1 = threading.Thread(target=launch)
stop_flag = threading.Event()
###POSICIONAMIENTO
cerrar_option.place(x=580, y=700)
lanzar.place(x=930,y=200)
title.place(x=500, y=60)
treeview.place(x=500, y=90)
treeview1.place(x=500, y=150)
treeview2.place(x=500, y=200)
##IMAGENES DE AERONAVES EN EL MAPA SEGUN COORDENADAS
image_path = "MACOL.jpg" 
image = Image.open(image_path)
image = image.resize((224*2, 317*2))
width, height = image.size
canvas = tk.Canvas(ventana, width=width, height=height)
canvas.place(x=1100,y=40)
guide.place(x=500,y=300)
image_tk = ImageTk.PhotoImage(image)
image_item = canvas.create_image(0, 0, anchor="nw", image=image_tk)
canvas.bind("<Motion>", mostrar_coordenadas)
etiqueta_coordenadas = tk.Label(ventana, text="Coordenadas:")
etiqueta_coordenadas.place(x=1150, y=700)
update_image()#retirarlo por falla de api opensky
##CIERRE DE VENTANA DE INTERFAZ
ventana.mainloop()
