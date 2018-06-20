# wroom_32

## Flash the board with Micropython

First you need to download the latest revision of the firmware.
http://micropython.org/download#esp32

Then to flash it on the esp32 run those commands (change the binary name)

```
pip install esptool
esptool.py --port /dev/ttyUSB0 erase_flash
esptool.py --chip esp32 -p /dev/ttyUSB0 write_flash -z 0x1000 esp32-20180530-v1.9.4-106-gc60589c0.bin
```

(complete instructions here : http://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html#deploying-the-firmware)

## Access the board from the command line

You need to use a serial prompt, if you don't want to use screen you can download picocom
```
sudo apt install picocom
```

then connect to the board

```
picocom /dev/ttyUSB0 -b115200
```

You know have a python interpreter that runs commands directly on the board.

To exit picocom first Ctrl-D (to stop the board) then Ctrl-A Ctrl-Q.

## Run code on the board

If you only want to run your python code on the esp32 you can use this command :
```
ampy -p /dev/ttyUSB0 run my_code.py
```

This works if the program ends, if not you'll want to add the --no-output option and open a picocom in another terminal to see qhat the board is printing.

## Add code on the board

There are two files that are executed at the start "boot.py" then "main.py".
To upload them on the board you can use ampy, an adafruit software that handle the files transfers.
```
sudo pip3 install adafruit-ampy
```
You can get or add a file with those two commands
```
ampy -p /dev/ttyUSB0 get boot.py
ampy -p /dev/ttyUSB0 put boot.py
```

## Links

Esp8266 doc (almost the same as esp32)

http://docs.micropython.org/en/v1.8.2/esp8266/esp8266/quickref.html

Micropython home page

http://micropython.org/

Projects idea

https://hackaday.io/search?term=esp32&tag=ESP32
