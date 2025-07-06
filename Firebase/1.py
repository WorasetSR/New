import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
# ตรวจสอบให้แน่ใจว่าชื่อไฟล์ตรงกับที่คุณดาวน์โหลดมา
# และไฟล์อยู่ในโฟลเดอร์เดียวกันกับสคริปต์ Python ของคุณ
cred = credentials.Certificate('tryy-bb616-firebase-adminsdk-fbsvc-13049ae1de.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://tryy-bb616.firebaseio.com' # ใช้ databaseURL ที่ถูกต้องของโปรเจกต์คุณ
})

# As an admin, the app has access to read and write all data, regradless of Security Rules
ref = db.reference('restricted_access/secret_document')
print(ref.get())
