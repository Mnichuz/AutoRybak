from pyautogui import *
import pyautogui,time,keyboard,ctypes

print('Kod zacznie działać za 10 sekund.')

#ROZDZIELCZOSC MONITORA
width1 = 1920
height1 = 1080

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

time.sleep(10)
print('Kod działa')
color = [85,172,238] #KOLOR EMOTKI RYBY
pic = pyautogui.screenshot(region = (int(0.25*width1),int(0.2*height1),int(0.4*width1),int(0.35*height1))) #region(left,top,width,height)
pic.save('capturing_probe.png') #PRÓBKA OBSZARU NA KTORYM SZUKANA JEST EMOTKA

def IsColorOnScreen(rgb,pic):
    width, height = pic.size

    done = 0

    for x in range(0, width, 2):
        for y in range(0, height, 2):
            r, g, b = pic.getpixel((x, y))
            if r == color[0] and g == color[1] and b == color[2]:
                done = 1
                time.sleep(0.05)
                break

        if done == 1:
            break
    if done == 1:
        return True
    return False


while keyboard.is_pressed('q') == False:
    flag = 0
    pic = pyautogui.screenshot(region = (int(0.25*width1),int(0.2*height1),int(0.4*width1),int(0.35*height1))) #region(left,top,width,height)

    if IsColorOnScreen(color,pic):
        print('Znaleziono kolor ryby.')
        flag = 1


    if flag == 1:
        pic = pyautogui.screenshot(region = (int(0.25*width1),int(0.2*height1),int(0.4*width1),int(0.35*height1))) #region(left,top,width,height)
        while IsColorOnScreen(color,pic):
            pic = pyautogui.screenshot(region = (int(0.25*width1),int(0.2*height1),int(0.4*width1),int(0.35*height1))) #region(left,top,width,height)
            if keyboard.is_pressed('q') == True:
                break
        else:
            if keyboard.is_pressed('q') == False:
                time.sleep(2.5)
                print('NACISKAM E (ŁAPIĘ RYBE...)')
                PressKey(0x12)
                time.sleep(.1)
                ReleaseKey(0x12)
                time.sleep(.1)

                print('Wyjmuje wędkę...')
                time.sleep(.1)
                PressKey(0x05)
                time.sleep(1)
                ReleaseKey(0x05)
                time.sleep(.1)
