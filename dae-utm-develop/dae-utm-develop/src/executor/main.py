import sys
from dataset import *
from ..constants.lib import *
##VARIABLES DE UTILIDAD
## UTILITY VARIABLES
global ll, coordinates, co, f1, f2, i, i_e, i_guide
coordinates = []
co = []
i_guide = []
f1 = []
i, i_e, f2 = 0, 0, []
ll = np.array(Image.open('med1.png'))
def redefine_mf():
    global mf
    global mv
    mf = []
    mv = []
    mf1 = radar_flights()
    mf1 = list(mf1)
    for i in range(len(mf1)):
        mf.append(0)
        mv.append(0)
    for i in range(len(mf1)):
        mf[i] = [mf1[i][1], mf1[i][2], mf1[i][5], mf1[i][6]]
        mv[i] = [mf1[i][5], mf1[i][6]]
    for i in range(len(mv)):
        mv[i][0] = round((mv[i][0] + 79.32644) / 0.02787)
        mv[i][1] = round((mv[i][1] - 12.617) / -0.027)
def save_coordinate(event):
    x = (((event.x) * (5.011160714)) / 29655.657) - 75.619
    y = (((-event.y) * (5.014195584)) / 26356.94) + 6.3061
    lon = x
    lat = y
    meteo_list = meteorological_values(lat, lon)
    altitude = get_altitude(y, x)
    for i in ([altitude, lat, lon]):
        meteo_list.append(i)
    return
def close_program():
    sys.exit()
def build_path(event):
    global coordinates, i, co, i_e
    if i > 1:
        reset_path()
    xi = event.x
    yi = event.y
    co.append(round(5.014195584 * yi))
    co.append(round(5.011160714 * xi))
    xi = 0.00011904 * xi - 75.60119
    yi = -0.00019011 * yi + 6.306028
    i = i + 1
    coordinates.append(yi)
    coordinates.append(xi)
    if i == 2:
        i_e = 0
def launch():
    global co, f1, f2, i_e, l_c, g_pnt, gx, gy, co2
    print("launching")
    i = 0
    co2 = [0, 0]
    while co[0] != co[2] and co[1] != co[3]:
        l_c = []
        l_cd = []
        for y in range(-5, 6, 1):
            for x in range(-5, 6, 1):
                i_x = co[1] + x
                i_y = co[0] + y
                if i_x == co[0] and i_y == co[1]:
                    None
                else:
                    if ll[i_y][i_x][0] == 255:
                        d = 0.3333 * (abs(i_y - co[2]) + abs(i_x - co[3]))
                        d1 = 0.3333 * ((abs(i_y - co[2]) ** 2 + abs(i_x - co[3]) ** 2) ** 0.5)
                        d2 = 0.3333 * (abs(i_y - gy) + abs(i_x - gx))
                        dt = d + d1 + d2
                        l_c.append([i_y, i_x])
                        l_cd.append(dt)
                        if co2[0] == l_c[l_cd.index(min(l_cd))][0] and co2[1] == l_c[l_cd.index(min(l_cd))][1]:
                            co[0] = co[2]
                        else:
                            co2[0] = co[0]
                            co2[1] = co[1]
                            co[0] = l_c[l_cd.index(min(l_cd))][0]
                            co[1] = l_c[l_cd.index(min(l_cd))][1]
                            i_guide.append(((co[1] * (5.011160714)) / 29655.657 - 75.619,
                                            ((-co[0] * (5.014195584)) / 26356.94) + 6.3061))
        i = i + 1
    else:
        print("done")
        kml = simplekml.Kml()
        line = kml.newlinestring(name="Route", description="Route Description", coords=i_guide)
        line.extrude = 1
        line.altitudemode = simplekml.AltitudeMode.relativetoground
        output_file = "route.kml"
        kml.save(output_file)
def reset_path():
    global i
    coordinates.clear()
    co.clear
    i_guide.clear()
    i = 0
def rgb(l):
    global color_abs
    color_abs = (l[0] + l[1] + l[2]) / 255
    if color_abs > 0.5:
        return 1
    else:
        print("Invalid Selection")
        return 0
def red_filter():
    global ava, ll, co, g_pnt, g_d, gx, gy
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
                ava.append([y, x])
                d = abs(ix - x) + abs(iy - y)
                ava_min.append(d)
    i_ava = ava[ava_min.index(min(ava_min))]
    co[0] = i_ava[0]
    co[1] = i_ava[1]
    ava.clear()
    ava_min.clear()
    for y in range(len(ll)):
        for x in range(len(ll[0])):
            if ll[y][x][0] == 255:
                ava.append([y, x])
                d = abs(ix1 - x) + abs(iy1 - y)
                ava_min.append(d)
    i_ava = ava[ava_min.index(min(ava_min))]
    co[2] = i_ava[0]
    co[3] = i_ava[1]
    for y in range(len(ll)):
        for x in range(len(ll[0])):
            ag = ll[y][x][1]
            if ag == 255:
                g_pnt.append([y, x])
                gy = abs(y - co[2])
                gx = abs(x - co[3])
                g_d.append([gy + gx])
    gx = g_pnt[g_d.index(min(g_d))][1]
    gy = g_pnt[g_d.index(min(g_d))][0]
    print(co, "new vectors", gy, gx)
def calculate_path():
    global i_guide
    red_filter()
    i_guide = []
### FIXED TEXT IN THE MODULE