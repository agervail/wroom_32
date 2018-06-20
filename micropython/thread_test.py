import machine, ssd1306
import _thread, time

def thread_entry(n):
  global n_finished, oled
  for i in range(0,123,3):
    oled.fill_rect(5, 5 + n * 10, i, 8, 0xffff)
    oled.show()
    time.sleep(0.1)
  with lock:
    n_finished += 1


i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.fill(0)
for i in range(6):
  oled.rect(5, 5 + i * 10, 120, 8, 0xffff)
oled.show()

lock = _thread.allocate_lock()
n_thread = 6
n_finished = 0

for i in range(n_thread):
  _thread.start_new_thread(thread_entry, (i, ))

while n_finished < n_thread:
  pass

print('done')
