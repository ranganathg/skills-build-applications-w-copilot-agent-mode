import os
import django
from octofit_tracker.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

try:
    User.objects.create(username='testuser', email='testuser@example.com', password='password123')
    print("User inserted successfully.")
except Exception as e:
    print(f"Error inserting user: {e}")
