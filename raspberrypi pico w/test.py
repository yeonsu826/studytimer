from machine import Pin
import time

# GPIO 13번 핀을 버튼 입력으로 설정
button = Pin(21, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value() == 1:  # 버튼이 눌렸을 때
        print("Button pressed")
        # 원하는 동작 수행
        

    time.sleep(0.1)  # 반복문 속도를 위해 잠시 대기

