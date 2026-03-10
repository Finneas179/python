import pyautogui as pg
sc = pg.screenshot(region=(0,600,640,640))
sc.show()
sc.save("screenshot.png")