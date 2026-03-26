import vgamepad
import time

gamepad = vgamepad.VX360Gamepad()

def moveR():
    gamepad.left_joystick_float(x_value_float=1.0, y_value_float=0)
    gamepad.update()
    time.sleep(5)
    gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)
    gamepad.update()

def moveL():
    gamepad.left_joystick_float(x_value_float=-1.0, y_value_float=0)
    gamepad.update()
    time.sleep(5)
    gamepad.left_joystick_float(x_value_float=0.0, y_value_float=0.0)
    gamepad.update()

def press_a():
    gamepad.press_button(button=vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()

def Release_a():
    gamepad.release_button(button=vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()

def press_x():
    gamepad.press_button(button=vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_X)
    gamepad.update()

def Release_x():
    gamepad.release_button(button=vgamepad.XUSB_BUTTON.XUSB_GAMEPAD_X)
    gamepad.update()

def spam_a():
    for i in range(30):
        press_a()
        time.sleep(0.05)
        Release_a()
        time.sleep(0.05)

def upgrade():
    press_x()
    time.sleep(0.1)
    Release_x()
    time.sleep(0.3)
    spam_a()

def main():
    while True:
        spam_a()
        moveL()
        spam_a()
        moveR()
        upgrade()

if __name__ == "__main__":
    main()