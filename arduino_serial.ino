char command;

void setup() {
  Serial.begin(9600);
  pinMode(5, OUTPUT); // Left motor
  pinMode(6, OUTPUT); // Right motor
}

void loop() {
  if (Serial.available()) {
    command = Serial.read();

    if (command == 'F') {
      digitalWrite(5, HIGH);
      digitalWrite(6, HIGH);
    } else if (command == 'S') {
      digitalWrite(5, LOW);
      digitalWrite(6, LOW);
    } else if (command == 'R') {
      digitalWrite(5, HIGH);
      digitalWrite(6, LOW);
    } else if (command == 'L') {
      digitalWrite(5, LOW);
      digitalWrite(6, HIGH);
    }
  }
}
