#include <Servo.h>

enum states {
  RUN,
  SCREAM
};


states state = RUN;
static const int servoPin = 2;
const byte buttonPin = 18;
const byte piezoPin = 19;

Servo servo1;
int counter = 0;

int freq = 2000;
int channel = 2;
int resolution = 8;
float msByDegree = 60 * 1000 / 180;
bool screaming = false;

void setup() {
  servo1.attach(servoPin);

  pinMode(buttonPin, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(buttonPin), resetCounter, RISING);

  ledcSetup(channel, freq, resolution);


  Serial.begin(115200);
  Serial.print("hello");
}

void loop() {
  switch(state) {
  case RUN:
    Serial.print("RUN");
    ledcDetachPin(piezoPin);
    while(counter < 180){
      counter++;
      servo1.write(counter);
      delay(msByDegree);
    }
    Serial.print("ENDOFrun");
    state = SCREAM;
    break;
  case SCREAM:
    if(!screaming){
      Serial.print("SCREAM");
      ledcAttachPin(piezoPin, channel);
      ledcWrite(channel, 125);
      ledcWriteTone(channel, 400);
      screaming = true;
    }
    break;
  }

  //ledcWriteTone(channel, 400);
  //for(int posDegrees = 0; posDegrees <= 180; posDegrees++) {
    //Serial.println(msByDegree);
  //}

}

void resetCounter() {
  counter = 0;
  state = RUN;
  screaming = false;
}
