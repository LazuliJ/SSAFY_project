int led1 = 17;
int btn1 = 18;

void setup() {
  // put your setup code here, to run once:
  pinMode(led1, OUTPUT);
  pinMode(btn1, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (digitalRead(btn1) == LOW) {
    digitalWrite(led1, HIGH);
  }
  else {
    digitalWrite(led1, LOW);
  }
  delay(100);
}
