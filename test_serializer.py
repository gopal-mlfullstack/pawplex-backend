import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from accounts.serializers import RegisterSerializer

data = {
    'username': 'test@test.com',
    'email': 'test@test.com',
    'password': 'password123',
    'password2': 'password123',
    'role': 'vet',
}

s = RegisterSerializer(data=data)
if not s.is_valid():
    print("Errors:", s.errors)
else:
    print("Valid!")
