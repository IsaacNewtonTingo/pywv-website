import os
from django.conf.global_settings import EMAIL_USE_SSL
from dotenv import load_dotenv

load_dotenv()
EMAIL_USE_SSL = True
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD =os.getenv("EMAIL_HOST_PASSWORD") 
EMAIL_PORT = os.getenv("EMAIL_PORT") 
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'