from pyautogui import * 
currentMouseX, currentMouseY = position()
browuserPosit = [520, 844]
moveTo(browuserPosit)
click(browuserPosit)
dot1 = [ 850, 440]
moveTo(dot1)
drag(-150, 0, 0.5, button = "left")
drag(0, 300, 0.5, button = "left")
drag(-150, 0, 0.5, button = "left")
move(0, -300)
drag(0, 150, 0.5, button = "left")
drag(300, 0, 0.5, button = "left")
drag(0, 150, 0.5, button = "left")
print(position())
print(currentMouseX)
alert("hello world")



