import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_graphql.settings")
django.setup()

try:
    from django.contrib.auth.models import User
    from django.contrib.auth.hashers import make_password

    password = make_password('nothing1234', salt=None, hasher='default')
    if not User.objects.filter(username='admin'):
        User.objects.create_superuser(username='admin', password=password)
        print('User creation successfully')
except Exception as e:
    print(e)
