from django.shortcuts import render
from django.contrib.auth.hashers import make_password

# Create your views here.

def index(request):

    if request.method == 'POST':
        password = request.POST['password']
        print(len(make_password(password)))

    return render(request, 'games/index.html')