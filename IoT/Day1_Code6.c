hw_timer_t *ledTimer = NULL;

int led =  17;
void ARDUINO_ISR_ATTR onTimer() {
  digitalWrite(led, !digitalRead(led)); // led toggle
}

int ms = 1000;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(led, OUTPUT);

  ledTimer = timerBegin(1000000); // 1초에 한번 onTimer 실행
  timerAttachInterrupt(ledTimer, &onTimer);
  timerAlarm(ledTimer, 500000, true, 0);

  timerStart(ledTimer);
}

int cnt = 0;
void loop() {
  // put your main code here, to run repeatedly:
  cnt++;
  if (cnt > 20) {
    timerEnd(ledTimer);
    Serial.println("timer end!");
  }
  Serial.print(cnt); Serial.println(" : BBQ");
  delay(500);
}
