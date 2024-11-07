int pot = A0;

// 가변 저항값을 읽는다.

void setup() {
  // put your setup code here, to run once:
  pinMode(pot, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int value = analogRead(A0);
  Serial.print("Original: "); Serial.print(value); // 원래 값

  int m_value = map(value, 0, 4095, -90, 90);
  Serial.print(" | map Value : "); Serial.print(m_value); // 0 ~ 4095를 -90에서 90까지 바꿀 수 있음.

  int c_value = constrain(m_value, 0, 90);
  Serial.print(" | constrain Value : "); Serial.println(c_value); // 0 ~ 90까지의 값만 표기
  delay(300);
}
