// 시리얼 통신을 통해 LED 제어
int led1 = 17;

void setup() {
  // put your setup code here, to run once:
  pinMode(led1, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available()) {
    char a = Serial.read();
    if (a == 'o') {
      digitalWrite(led1, HIGH);
      Serial.println("ON");
    }
    else if (a == 'f') {
      digitalWrite(led1, LOW);
      Serial.println("OFF");
    }
  }
  delay(100);
}
