from django.http import JsonResponse
import json
from django.contrib.auth.models import User
import re
from django.views.decorators.csrf import csrf_exempt

def validate_email(email):
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(email_regex, email) is not None

@csrf_exempt
def user_register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        errors = {}
        # username, email and password validation
        if 'username' not in data or not data['username']:
            errors['username'] = 'Username is required'
        elif User.objects.filter(username=data['username']).exists():
            errors['username'] = 'Username is already taken'

        if 'email' not in data or not data['email']:
            errors['email'] = 'Email is required'
        elif not validate_email(data['email']):
            errors['email'] = 'Invalid email format'
        elif User.objects.filter(email=data['email']).exists():
            errors['email'] = 'Email is already registered'

        if 'password' not in data or not data['password']:
            errors['password'] = 'Password is required'
        elif len(data['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters long'

        if errors:
            return JsonResponse(errors, status=400)

        username = data['username']
        email = data['email']
        password = data['password']
        new_user = User.objects.create_user(username=username, email=email)
        new_user.set_password(password)
        new_user.save()

        return JsonResponse({'message': 'user created successfully'})
    return JsonResponse({'error': 'invalid request method'})
