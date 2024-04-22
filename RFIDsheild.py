import board
import adafruit_st25dv16
from digitalio import DigitalInOut, Direction, Pull

class rfid:
    def __init__(self):
        self.i2c = board.I2C()
        self.eeprom = adafruit_st25dv16.EEPROM_I2C(self.i2c)
    
    def write(self,to_write,head=0x04):
        str=to_write
        l=len(str)
        buf = bytearray ([0xe1, 0x40, 0x40, 0x05, 0x03, 0x00, 0xd1, 0x01, 0x00, 0x55])
        buf[5] = (l+5)
        buf[8] = (l+1)
        self.eeprom[0:len(buf)]=buf
        self.eeprom[len(buf)]=head
        k=len(buf)+1
        self.eeprom[k:k+l]=bytearray(str)
        self.eeprom[k+l]=0xfe

        for i in range(0, 5):
            j = i * 16
            hex_string = ":".join("%02x" % b for b in self.eeprom[j:j+15])
            print(j, "> ", hex_string, "> ", self.eeprom[j:j+15])

class button:
    def __init__(self,button):
        if button == 1:
            self.button = DigitalInOut(board.D9)
        if button == 0:
            self.button = DigitalInOut(board.D8)
        self.button.direction = Direction.INPUT
        self.button.pull = Pull.UP
    
    def get_press(self):
        if not self.button.value:
            return True
        else:
            return False

class led_array:
    def __init__(self):
        self.list = []
        led1 = DigitalInOut(board.D0)
        led1.direction = Direction.OUTPUT
        self.list.append(led1)
        led2 = DigitalInOut(board.D1)
        led2.direction = Direction.OUTPUT
        self.list.append(led2)
        led3 = DigitalInOut(board.D2)
        led3.direction = Direction.OUTPUT
        self.list.append(led3)
        led4 = DigitalInOut(board.D3)
        led4.direction = Direction.OUTPUT
        self.list.append(led4)
        led5 = DigitalInOut(board.D4)
        led5.direction = Direction.OUTPUT
        self.list.append(led5)
        led6 = DigitalInOut(board.D5)
        led6.direction = Direction.OUTPUT
        self.list.append(led6)
        led7 = DigitalInOut(board.D6)
        led7.direction = Direction.OUTPUT
        self.list.append(led7)
        led8 = DigitalInOut(board.D7)
        led8.direction = Direction.OUTPUT
        self.list.append(led8)

    def fill(self):
        for led in self.list:
            led.value = True
    
    def clear(self):
        for led in self.list:
            led.value = False
    
    def activate(self,led):
        if type(led) == int:
            self.list[led].value = True
        if type(led) == list:
            for light in led:
                self.list[light].value = True
    
    def deactivate(self,led):
        if type(led) == int:
            self.list[led].value = False
        if type(led) == list:
            for light in led:
                self.list[light].value = False

    def toggle(self,led):
        if type(led) == int:
            if self.list[led].value == True:
                self.list[led].value = False
            else:
                self.list[led].value = True
        if type(led) == list:
            for light in led:
                if self.list[light].value == True:
                    self.list[light].value = False
                else:
                    self.list[light].value = True