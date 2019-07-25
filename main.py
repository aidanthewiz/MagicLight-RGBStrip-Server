#!/usr/bin/env python
from bluepy import btle
import datetime
import time
# sudo apt install pkg-config libboost-python-dev libboost-thread-dev libbluetooth-dev libglib2.0-dev python-dev python3-pip
# sudo pip3 install bluepy

class MagicLightRGBStrip:
    def __init__(self, MAC):
        self.effects = {
            'seven_color_cross_fade': 0x25,
            'red_gradual_change': 0x26,
            'green_gradual_change': 0x27,
            'blue_gradual_change': 0x28,
            'yellow_gradual_change': 0x29,
            'cyan_gradual_change': 0x2a,
            'purple_gradual_change': 0x2b,
            'white_gradual_change': 0x2c,
            'red_green_cross_fade': 0x2d,
            'red_blue_cross_fade': 0x2e,
            'green_blue_cross_fade': 0x2f,
            'seven_color_stobe_flash': 0x30,
            'red_strobe_flash': 0x31,
            'green_strobe_flash': 0x32,
            'blue_strobe_flash': 0x33,
            'yellow_strobe_flash': 0x34,
            'cyan_strobe_flash': 0x35,
            'purple_strobe_flash': 0x36,
            'white_strobe_flash': 0x37,
            'seven_color_jumping_change': 0x38
        }
        self.days = {
            'monday': 0x02,
            'tuesday': 0x04,
            'wednesday': 0x08,
            'thursday': 0x10,
            'friday': 0x20,
            'saturday': 0x40,
            'sunday': 0x80
        }
        try:
            print("Connecting to light...")
            connection = btle.Peripheral(MAC).withDelegate(self)
            self.writer = connection.getCharacteristics(uuid = btle.UUID('ffe9'))[0]
            print("Connected")
        except RuntimeError as e:
           print('Connection failed : {}'.format(e))
        self.startupInit()

    def turnOn(self):
        print("Turned light on.")
        return self.writer.write(bytearray([0xCC, 0x23, 0x33]))
    def turnOff(self):
        print("Turned light off.")
        return self.writer.write(bytearray([0xCC, 0x24, 0x33]))
    def setRGB(self, red, green, blue):
        print("Set RGB value to R: " + str(red) + " G: " + str(green) + " B: " + str(blue))
        return self.writer.write(bytearray([0x56, red, green, blue, 0x00, 0xF0, 0xAA]))
    def setBrightness(self, alpha):
        print("Set brightness to " + str(alpha))
        return self.writer.write(bytearray([0x56, 0x00, 0x00, 0x00, alpha, 0x0F, 0xAA]))
    def setEffect(self, effect, speed):
        return self.writer.write(bytearray([0xBB, effect, speed, 0x44]))
    def startupInit(self):
        self.turnOff()
        time.sleep(2)
        self.turnOn()
        self.setRGB(255, 255, 255)
        self.setBrightness(255)

c = MagicLightRGBStrip("10:CE:A9:E1:66:EB")
time.sleep(2)
c.setRGB(0, 255, 0)
