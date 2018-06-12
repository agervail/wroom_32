## Installation

```
sudo pip install platformio
```

## Usage

To upload the binary on your board you'll need to run :
```
platformio run --target upload
```
If you then want to connect to the serial port you can use :
```
platformio device monitor -b 115200
```

## Additionnal informations

If you want to recreate a project you'll need to run those commands :
```
platformio init --board esp32dev
```
