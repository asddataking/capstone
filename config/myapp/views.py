from django.shortcuts import render
from .forms import SignupForm

def index(request):
    return render(request, 'myapp/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')
 
            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
 
            # redirect user to home page
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})