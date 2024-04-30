#include <Servo.h>

//Define relay
int relay = 3;

// Define servo 
Servo servoHorizontal; // servo for left/right movement
Servo servoVertical;   // servo for up/down movement

// Define positions
int posHorizontal = 90; // initial position for servoHorizontal (centered)
int posVertical = 90;   // initial position for servoVertical (centered)
int increment = 5;     // amount to increment servo position

// Define limits
int minHorizontal = 0;   // minimum position for servoHorizontal
int maxHorizontal = 180; // maximum position for servoHorizontal
int minVertical = 0;     // minimum position for servoVertical
int maxVertical = 180;   // maximum position for servoVertical

void setup() {
  Serial.begin(9600);
  // Attach servos to pins
  servoHorizontal.attach(9); // attach servoHorizontal to pin 0
  servoVertical.attach(10);   // attach servoVertical to pin 1
  pinMode(relay, OUTPUT);
}

void loop() {
  //Init serial commands
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == '1') { //Relay High
      digitalWrite(relay, HIGH);
      }
    if (command == '2') { //Relay Low
      digitalWrite(relay, LOW);      
      }
    if (command == 'l') { //Relay Left
      left();
      }
    if (command == 'r') { //Relay Right
      right();
      }
    if (command == 'u') { //Relay Up
      up();
      }
    if (command == 'd') { //Relay Down
      down();
      }
  }
}

void right() {
  if (posHorizontal + increment <= maxHorizontal) {
    posHorizontal += increment;
    servoHorizontal.write(posHorizontal);
    delay(5); 
  }
}

void left() {
  if (posHorizontal - increment >= minHorizontal) {
    posHorizontal -= increment;
    servoHorizontal.write(posHorizontal);
    delay(5); 
  }
}

void up() {
  if (posVertical + increment <= maxVertical) {
    posVertical += increment;
    servoVertical.write(posVertical);
    delay(5); 
  }
}

void down() {
  if (posVertical - increment >= minVertical) {
    posVertical -= increment;
    servoVertical.write(posVertical);
    delay(5); 
  }
}
