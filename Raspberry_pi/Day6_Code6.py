from gpiozero import Button

from sense_hat import SenseHat
from signal import pause
from time import sleep
import copy

x = 0
y = 0
map_num = 0
sense = SenseHat()
btn = Button(14)

X = [0, 0, 0]
O = [4, 114, 77]
R = [52, 37, 47]

MAP = [
X, O, X, X, X, X, X, X,
X, O, O, O, O, O, O, X,
X, X, X, X, X, X, O, X,
X, O, O, O, O, X, O, X,
X, X, O, X, X, X, O, X,
X, X, O, X, O, O, O, X,
X, O, O, X, X, X, X, X, 
X, X, X, X, O, O, O, X]

MAPS = []

diry = [1, 0, -1, 0]
dirx = [0, 1, 0, -1]

def DFS(now_MAP, now_y, now_x):
    if (now_y == 7 and now_x == 7):
        MAPS.append(copy.deepcopy(now_MAP))
        return
    if (now_y == y and now_x == x):
        now_MAP[now_y*8+now_x] = R
    for i in range(4):
        ny = now_y + diry[i]
        nx = now_x + dirx[i]
        if (ny < 0 or ny >= 8 or nx < 0 or nx >= 8):
            continue
        if (now_MAP[ny*8+nx] == O):
            continue
        if (now_MAP[ny*8+nx] == R):
            continue
        now_MAP[ny*8+nx] = R
        DFS(now_MAP, ny, nx)
        now_MAP[ny*8+nx] = X

def clamp(value, min_value=0, max_value=7):
    return min(max_value, max(min_value, value))

def def_map():
    global map_num
    if (map_num!=(len(MAPS)-1)):
        map_num = map_num+1
    else:
        map_num = 0
    map_num = min(len(MAPS), max(0, map_num))

def pushed_up():
    global y
    if (y != 0 and MAP[(y-1)*8+x] == X):
        y = clamp(y-1)

def pushed_down():
    global y
    if (y != 7 and MAP[(y+1)*8+x] == X):
        y = clamp(y+1)

def pushed_left():
    global x
    if (x != 0 and MAP[y*8+(x-1)] == X): 
        x = clamp(x-1)

def pushed_right():
    global x
    if (x != 7 and MAP[y*8+(x+1)] == X):
        x = clamp(x+1)

def refresh():
    global MAPS, map_num
    MAPS = []
    tmp_MAP = copy.deepcopy(MAP)
    DFS(tmp_MAP, y, x)
    sense.clear()
    map_num = min(map_num, len(MAPS)-1)
    sense.set_pixels(MAPS[map_num])
    sense.set_pixel(0, 0, 6, 90, 130) # start
    sense.set_pixel(7, 7, 6, 90, 130) # end
    sense.set_pixel(x, y, 210, 171, 153)

while(True):
    acceleration = sense.get_accelerometer_raw()
    dx = acceleration['x']
    dy = acceleration['y']

    dx = round(dx, 0)
    dy = round(dy, 0)

    if (dx == 0 and dy == 1):
        pushed_down()
    elif (dx == 0 and dy == -1):
        pushed_up()
    elif (dx == -1 and dy == 0):
        pushed_left()
    elif (dx == 1 and dy == 0):
        pushed_right()
    elif (btn.is_pressed == True):
        def_map()

    print("x={0}, y={1}".format(dx, dy))

    refresh()
    sleep(0.1)
