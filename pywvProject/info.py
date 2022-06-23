import os
from dotenv import load_dotenv

load_dotenv()
EMAIL_USE_TLS = True
EMAIL_HOST = 'mail.privateemail.com'
EMAIL_HOST_USER = 'info@pywv.org'
EMAIL_HOST_PASSWORD =os.getenv("EMAIL_HOST_PASSWORD") 
EMAIL_PORT = 587
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'