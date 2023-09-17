import firebase_admin, os
from firebase_admin import credentials

if not firebase_admin._apps:
    cred = credentials.Certificate(os.getenv('GOOGLE_APPLICATION_CREDENTIALS')) 
    default_app = firebase_admin.initialize_app(cred)