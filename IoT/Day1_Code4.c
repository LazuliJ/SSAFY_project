#define LEDC_BASE_FREQ 5000
#define LED_CHANNEL 0
#define LEDC_TIMER_8_BIT 8
#define LED_PIN 17

// PWM 제어로 LED 밝기 변화

void setup() {
  // put your setup code here, to run once:
  ledcAttach(LED_PIN, LEDC_BASE_FREQ, LEDC_TIMER_8_BIT);
}

void loop() {
  // put your main code here, to run repeatedly:
  for (int dutyRate = 0; dutyRate<=255; dutyRate++) {
    ledcWrite(LED_PIN, dutyRate);
    delay(15);
  }
  for (int dutyRate = 255; dutyRate>=0; dutyRate--) {
    ledcWrite(LED_PIN, dutyRate);
    delay(15);
  }
}
