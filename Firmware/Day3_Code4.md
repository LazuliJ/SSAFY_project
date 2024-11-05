# LED Switch

## Hardware
- renesas FPB-RA6E1 * 1  
- Switch * 2, LED * 4  
  
## Connect
- p302 > SW_1
- p402 > SW_2
  
- P303 > LEDr
- P105 > LEDy
- P107 > LEDg
- P108 > LEDb
  
## Summary
- 재귀호출을 사용하여 구현한다.
- LED 4개를 차례로 연결한다.
- xxxx는 꺼진 상태이다.
- oooo는 모두 켜진 상태를 뜻한다.

- xxxx부터 oooo까지 모든 조합을 0.1초에 한번씩 LED 4개로 표현한다.
- 모든 조합을 보여주었다면, 아무것고 하지 않고 버튼 눌리기를 대기한다.

- Switch 1: Play를 처음부터 시작한다.
- Switch 2: 즉시 일시정지를 한다. 한번 더 누르면 재개한다.
