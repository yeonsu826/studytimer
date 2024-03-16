from machine import Pin
import time
import network
import urequests
import utime


button = Pin(21, Pin.IN, Pin.PULL_UP)

# Wi-Fi 연결 함수
def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        wlan.connect("infoinno", "yjys6826!")  # Wi-Fi 연결 정보를 입력하세요
        print("Connecting to Wi-Fi", end="")
        while not wlan.isconnected():
            print(".", end="")
            time.sleep(1)
        else:
            print("\nWiFi Connected")
            print(wlan.ifconfig())

connect_to_wifi()
'''
# Firebase에 데이터를 전송하는 함수
def send_data_to_firebase(data):
    firebase_url = "https://study-timer-9744a-default-rtdb.firebaseio.com/test.json" # Firebase URL 입력
    response = urequests.post(firebase_url, json=data)
    
    if response.status_code == 200:
        print("Data sent to Firebase successfully")
    else:
        print("Failed to send data to Firebase")
    
    response.close()
'''
def send_data_to_firebase(data):
    firebase_url = "https://study-timer-9744a-default-rtdb.firebaseio.com/test.json" # Firebase URL 입력
    response = urequests.post(firebase_url, json=data)
    
    if response.status_code == 200:
        print("Data sent to Firebase successfully")
        # 데이터를 전송한 후 반환된 키 확인
        key = response.json().get("name")  # 여기서 "name"은 Firebase가 생성한 고유한 키를 나타냅니다.
        print("Generated Key:", key)
    else:
        print("Failed to send data to Firebase")
    
    response.close()


# 버튼 핀 설정


# 현재 시간을 초 단위로 가져오기
current_time_seconds = utime.time()

# 초 단위 시간을 현재 시간으로 변환
current_time = utime.localtime(current_time_seconds)
'''

while True:
    if button.value() == 0:  # 버튼이 눌리면
        print("sit")
        # 예를 들어, 센서 값을 읽거나 원하는 데이터를 생성
        data_to_send = {"start-time": current_time} # 전송할 데이터 (원하는 데이터로 대체)
        # Firebase에 데이터 전송
        send_data_to_firebase(data_to_send)
        time.sleep(0.5)  # 버튼이 길게 눌리는 것을 방지하기 위한 딜레이
    else:
        print("standing")
        data_to_send = {"stop-time": current_time} # 전송할 데이터 (원하는 데이터로 대체)
        send_data_to_firebase(data_to_send)
        time.sleep(0.5)  # 버튼이 길게 눌리는 것을 방지하기 위한 딜레이

'''

button_pressed = False  # 버튼 눌림 여부를 나타내는 변수

while True:
    if button.value() == 0 and not button_pressed:  # 버튼이 눌리면서 이전에 눌리지 않았을 때
        print("sit")
        button_pressed = True  # 버튼이 눌렸음을 표시
        
        data_to_send = {"start-time": current_time}  # 전송할 데이터 (원하는 데이터로 대체)
        send_data_to_firebase(data_to_send)  # Firebase에 데이터 전송
        
        time.sleep(0.5)  # 버튼이 길게 눌리는 것을 방지하기 위한 딜레이
    
    elif button.value() == 1 and button_pressed:  # 버튼이 떼어지면서 이전에 눌렸을 때
        print("standing")
        button_pressed = False  # 버튼이 떼어졌음을 표시
        
        data_to_send = {"stop-time": current_time}  # 전송할 데이터 (원하는 데이터로 대체)
        send_data_to_firebase(data_to_send)  # Firebase에 데이터 전송
        
        time.sleep(0.5)  # 버튼이 길게 눌리는 것을 방지하기 위한 딜레이



