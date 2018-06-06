import machine
import time
import onewire

dat = machine.Pin(12)
ds = DS18X20(onewire.OneWire(dat))
roms = ds.scan()

for i in range(10):
    print('temperature : ', end=' ')
    ds.convert_temp()
    time.sleep_ms(750)
    print(ds.read_temp(roms[0]), end=' ')
    print()
