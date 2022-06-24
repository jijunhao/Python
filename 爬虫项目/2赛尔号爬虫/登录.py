import win32gui
import win32con
import win32api
import cv2
from PIL import ImageGrab
from ctypes import *
from ctypes.wintypes import *
import numpy as np
import time
import pyperclip

window = win32gui.FindWindow("WTWindow","MG风神登录器 [当前未启用鼠标连点,按下CTRL+1启用]")
while not window:
    print('定位游戏窗体失败，5秒后重试...')
    time.sleep(5)
    window = win32gui.FindWindow("WTWindow","MG风神登录器 [当前未启用鼠标连点,按下CTRL+1启用]")

# 定位到游戏窗体
def get_window_rect(hwnd):
    try:
        f = ctypes.windll.dwmapi.DwmGetWindowAttribute
    except WindowsError:
        f = None
    if f:
        rect = ctypes.wintypes.RECT()
        DWMWA_EXTENDED_FRAME_BOUNDS = 9
        f(ctypes.wintypes.HWND(hwnd),
          ctypes.wintypes.DWORD(DWMWA_EXTENDED_FRAME_BOUNDS),
          ctypes.byref(rect),
          ctypes.sizeof(rect)
          )
        return rect.left, rect.top, rect.right, rect.bottom

win32gui.SetForegroundWindow(window)
time.sleep(0.05)
pos = get_window_rect(window)
pos_init = win32gui.GetWindowRect(window)
print("定位到游戏窗体：" + str(pos))

def search(pic):
    print('捕获屏幕截图...')
    scim = ImageGrab.grab(bbox =pos)  # 屏幕截图，获取到的是Image类型对象
    img1 = cv2.cvtColor(np.asarray(scim),cv2.COLOR_RGB2BGR)
    img2 = cv2.imread(pic)

    print('搜索位置...')
    result = cv2.matchTemplate(img2,img1,cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= 0.95)
    res = list(zip(locations[0], locations[1]))
    point = (res[0][1]+pos_init[0], res[0][0]+pos_init[1])
    return point
"""
point = search("1.png")
win32api.SetCursorPos(point)
time.sleep(0.5)
print('模拟点击...')
# 左点击
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, point[0],point[1], 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, point[0],point[1], 0, 0)
time.sleep(1)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, point[0],point[1], 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, point[0],point[1], 0, 0)
"""

point = search("1.png")
win32api.SetCursorPos(point)
time.sleep(1)
print('模拟输入...')
# 左点击
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, point[0],point[1], 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, point[0],point[1], 0, 0)
time.sleep(1)
pyperclip.copy("TANZRXPFG3X6E872")

win32api.keybd_event(17,0,0,0)  #ctrl键位码是17
win32api.keybd_event(86,0,0,0)  #v键位码是86
win32api.keybd_event(86,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)


point = search("1.png")
win32api.SetCursorPos(point)
time.sleep(1)
print('模拟输入...')
# 左点击
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, point[0],point[1], 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, point[0],point[1], 0, 0)
time.sleep(1)
pyperclip.copy("sunyuxing10yue")

win32api.keybd_event(17,0,0,0)  #ctrl键位码是17
win32api.keybd_event(85,0,0,0)  #v键位码是86
win32api.keybd_event(85,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)
