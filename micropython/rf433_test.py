import machine
import ssd1306

screen_width = 128
screen_height = 64
col_width = 8
nb_cols = int(screen_width / col_width)
nb_sample = 100.0
 
p13 = machine.Pin(13, machine.Pin.IN)
 
i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))
oled = ssd1306.SSD1306_I2C(screen_width, screen_height, i2c)
 
avg_l = [0] * nb_cols
while True:
  moy = 0
  for i in range(nb_sample):
    moy += p13.value()

  print("total " + str(moy))
  moy = int(moy / nb_sample * screen_height)

  avg_l.pop()
  avg_l.insert(0, moy)
  #print(avg_l)
  oled.fill(0)
  for i in range(nb_cols):
    oled.rect(i * col_width, 64 - avg_l[i], col_width, avg_l[i], 0xffff)
  oled.show()
