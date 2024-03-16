import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Firebase 프로젝트의 서비스 계정 키 파일 경로
cred = credentials.Certificate('https://study-timer-9744a-default-rtdb.firebaseio.com/sit.json')

# Firebase 앱 초기화
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://study-timer-9744a-default-rtdb.firebaseio.com'

})

# Firebase 데이터베이스의 레퍼런스 가져오기
ref = db.reference('/sit')  # 데이터를 가져올 경로 설정

# 데이터 읽기
data = ref.get()
print(data)  # 데이터 출력 또는 활용
