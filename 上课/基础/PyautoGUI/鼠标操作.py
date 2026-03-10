import pyautogui as pg
import random
#moveto 是从原点到你设置的点位，然后原点就是电脑左上角
#但是据我实践我发现，我这个原点是我鼠标当前的位置
# pg.moveTo(100,200,8)
#ctrl+f2结束
for i in range(10):
    pg.moveTo(random.randint(0,2560),random.randint(0,1600),1)

#单击鼠标：左键left，右键right，中间键：middle
#click(x,y.Button="哪一个按键"）
#doubleclick这个就是双击

pg.doubleClick(100,100,button="right")

#按住操作:mouseDown(x,y,button="")，释放操作:mouseUp

