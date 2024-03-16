from machine import Pin
import time
import network
import urequests

# Wi-Fi 연결 함수
def connect_to_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        wlan.connect("your_wifi_ssid", "your_wifi_password")  # Wi-Fi 연결 정보를 입력하세요
        print("Connecting to Wi-Fi", end="")
        while not wlan.isconnected():
            print(".", end="")
            time.sleep(1)
        else:
            print("\nWiFi Connected")
            print(wlan.ifconfig())

# Firebase에 데이터를 전송하는 함수
def send_data_to_firebase(data):
    firebase_url = "https://your-project-id.firebaseio.com/your-path.json"  # Firebase URL 입력
    response = urequests.post(firebase_url, json=data)
    
    if response.status_code == 200:
        print("Data sent to Firebase successfully")
    else:
        print("Failed to send data to Firebase")
    
    response.close()

# 버튼 핀 설정
button = Pin(2, Pin.IN, Pin.PULL_DOWN)

# Wi-Fi 연결
connect_to_wifi()

while True:
    if button.value() == 1:  # 버튼이 눌리면
        print("Button pressed")
        
        # 여기에 데이터 생성 또는 수집하는 작업을 추가
        # 예를 들어, 센서 값을 읽거나 원하는 데이터를 생성
        
        data_to_send = {"start": "button"}  # 전송할 데이터 (원하는 데이터로 대체)
        
        # Firebase에 데이터 전송
        send_data_to_firebase(data_to_send)
        
        time.sleep(0.5)  # 버튼이 길게 눌리는 것을 방지하기 위한 딜레이

