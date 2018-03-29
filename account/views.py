from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from account.forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
# Create your views here.
def home(request):
	numbers = [1,2,3,4,5,6]
	name = 'AMBER GAUTAM'
	args = {'myname' : name, 'numbers' : numbers}
	return render(request, 'account/home.html', args) #dictionary object


def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/account')
	else:
		form = RegistrationForm
		args = {'form' : form}
		return render(request, 'account/reg_forms.html', args)


def profile(request):
	args = {'user' : request.user}
	return render(request, 'account/profile.html', args)

def edit_profile(request):
	if request.method == 'POST':
		form = UserChangeForm(request.POST, instance = request.user)
		if form.is_valid():
			form.save()
			return redirect('/account/profile')
	else:
		#blank form
		form = UserChangeForm(instance = request.user)
		args = {'form' : form}
		return render(request, 'account/edit_profile.html', args)

