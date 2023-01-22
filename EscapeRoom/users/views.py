from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from testER.models import EscapeRoom

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            role = form.cleaned_data.get('type')
            Profile.objects.create(user=user,user_type=role)
            messages.success(request, f'Account created for {username}! Now You can log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form' : form})

@login_required()
def profile(request):
    #roomsy = EscapeRoom.objects.get(wlasc_id=request.user.profile)
    #print(roomsy.nazwa)

    return render(request, 'users/profile.html')