from smbus2 import SMBus
from mlx90614 import MLX90614
import pytemperature

def tempfun():
    bus = SMBus(1)
    sensor = MLX90614(bus, address=0x5A)
    obj_cel=sensor.get_object_1()+2
    bus.close()
    return pytemperature.c2f(obj_cel)

