from bluepy import btle
# sudo apt install pkg-config libboost-python-dev libboost-thread-dev libbluetooth-dev libglib2.0-dev python-dev python3-pip
# sudo pip3 install bluepy

def turnOn():
    return writeRGB.write(bytearray([0xCC, 0x23, 0x33]))
def turnOff():
    return writeRGB.write(bytearray([0xCC, 0x24, 0x33]))
def setRGB(r, g, b):
    return writeRGB.write(bytearray([0x56, r, g, b, 0x00, 0xF0, 0xAA]))
def setBrightness(a):
    return writeRGB.write(bytearray([0x56, 0x00, 0x00, 0x00, a, 0x0F, 0xAA]))

try:
    connection = btle.Peripheral("10:CE:A9:E1:66:EB")
    writeRGB = connection.getCharacteristics(uuid = btle.UUID('ffe9'))[0]
except RuntimeError as e:
    print('Connection failed : {}'.format(e))