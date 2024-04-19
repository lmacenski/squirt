int ledPin = 13;
int relay = 3; 

void setup() {
    pinMode(ledPin, OUTPUT);
    pinMode(relay,OUTPUT);
    Serial.begin(9600);
}

void loop() {
    if (Serial.available() > 0) {
        char command = Serial.read();
        if (command == '1') {
            digitalWrite(ledPin, HIGH);
            digitalWrite(relay, HIGH);
  
        }
        if (command == '2') {
            digitalWrite(ledPin, LOW);
            digitalWrite(relay, LOW);
            
        }
    }
}
