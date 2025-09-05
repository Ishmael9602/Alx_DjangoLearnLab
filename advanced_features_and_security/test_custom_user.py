import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from accounts.models import CustomUser
from datetime import date

# Test creating a user
user = CustomUser.objects.create_user(
    username='testuser',
    email='test@example.com',
    password='testpassword',
    date_of_birth=date(1990, 1, 1)
)

print(f"Created user: {user}")
print(f"Date of birth: {user.date_of_birth}")
print(f"Profile photo: {user.profile_photo}")
