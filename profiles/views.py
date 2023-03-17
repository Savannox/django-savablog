from django.core.files.storage import default_storage
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from profiles.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from profiles.models import ProfileModel
from django.contrib.auth.models import User

# Create your views here.

def Registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid:
            user = form.save()
            login(request, user)
            return redirect('succes')
    else:
        form = RegistrationForm
        return render(request, 'profiles/register.html', {
            'form':form,
        })

def LoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('blog')
        else:
            error = 'El nombre de usuario o la contraseña son incorrectos'
            return render(request, 'profiles/login.html', {'error':error})
    
    return render(request, 'profiles/login.html')

@login_required
def LogoutView(request):
    logout(request)
    return redirect('home')

@login_required
def ProfileDetail(request):
    user = request.user
    profile = ProfileModel.objects.get(user=user)
    user_model = User.objects.get(username=user)
    if request.method == 'POST':
        user_model.first_name = request.POST['first_name']
        user_model.last_name = request.POST['last_name']
        profile.bio = request.POST['bio']
        if request.POST['birthday']:
            profile.birthday = request.POST['birthday']
        if 'photo' in request.FILES:
            prevoius_image = profile.photo.path
            if default_storage.exists(prevoius_image) and not prevoius_image.endswith('user.png'):
                default_storage.delete(prevoius_image)
            profile.photo = request.FILES['photo']
            profile.save()
        profile.save()
        user_model.save()
        return redirect('public', profile_id=profile.id)

    return render(request, 'profiles/profile.html', {
        'user':user,
        'profile': profile
        })

@login_required
def SuccesView(request):
    user = request.user
    profile = ProfileModel.objects.get(user=user)
    user_model = User.objects.get(username=user)
    if request.method == 'POST':
        if request.POST['birthday']:
            profile.birthday = request.POST['birthday']
        profile.bio = request.POST['bio']
        user_model.first_name = request.POST['first_name']
        user_model.last_name = request.POST['last_name']
        profile.save()
        user_model.save()
        return redirect('blog')
    
    return render(request, 'profiles/succes.html')