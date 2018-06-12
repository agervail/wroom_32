import time
from machine import I2C, Pin, PWM
from ht16k33_seg import Seg7x4

class Application:
    def __init__(self):
        self.state = 'RUN'
        self.i2c = I2C(scl=Pin(22), sda=Pin(21))
        self.seg = Seg7x4(self.i2c)
        self.seg.fill(False)
        self.seg.show()
        self.count = 50
        self.running = True
        self.but = Pin(18, Pin.IN, Pin.PULL_UP)
        self.but.irq(trigger=Pin.IRQ_FALLING, handler=self._but_press)

    def MainLoop(self):
        while True:
            if self.state == 'RUN':
                while self.count > 0:
                    s = str(self.count / 10)
                    s = ''.join([' ' * (5 - len(s))]) + s
                    self.seg.text(s)
                    self.seg.show()
                    self.count -= 1
                    time.sleep(0.1)
                self.state = 'SCREAM'
            elif self.state == 'SCREAM':
                self._blink()
                self._siren()

    def _siren(self):
        def up(buz):
            for i in range(200, 2000, 20):
                buz.freq(i)
                time.sleep(0.005)
        def down(buz):
            for i in range(2000, 200, -20):
                buz.freq(i)
                time.sleep(0.005)
        buz = PWM(Pin(19))
        buz.duty(512)
        up(buz)
        down(buz)
        buz.deinit()

    def _blink(self):
        for i in range(4):
            self.seg.put('-', i)
        self.seg.show()
        self.seg.blink_rate(1)

    def _but_press(self, p):
        self.count = 600
        self.state = 'RUN'
        self.seg.blink_rate(0)

#app = Application()
#app.MainLoop()
'''

from led_backpack import Application
app = Application()
app.MainLoop()

'''
