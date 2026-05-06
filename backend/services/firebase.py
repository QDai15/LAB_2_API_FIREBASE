import firebase_admin
from firebase_admin import credentials, firestore

try:
    cred = credentials.Certificate("backend/firebase_admin.json")
    
    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred)
        
    db = firestore.client()
    print("Kết nối Firebase thành công!")
except Exception as e:
    print(f"Lỗi kết nối Firebase: {e}")
    db = None