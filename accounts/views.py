from django.shortcuts import render, render_to_response,redirect, HttpResponseRedirect, reverse,HttpResponse
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,

)
User =  get_user_model()
from .forms import UserLoginForm, UserRegisterForm
from .idgenerator import id, random_string_generator
from gpasystem.models import IndividualGrading
def login_view(request):
	title = 'Login'
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		email = form.cleaned_data.get('email')
		password = form.cleaned_data.get('password')
		user =authenticate(email=email,password=password)
		login(request, user)
		idg = random_string_generator()
		print(request.user.is_authenticated)
		url = reverse('profile', kwargs={'id': idg })
		return HttpResponseRedirect(url)
	return render(request, "accounts/form.html", {"form":form,"title":title})
def signup_view(request):
	title = 'Sign Up'
	form  = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user =form.save(commit=False)
		password = form.cleaned_data.get('password2')
		user.CSU_ID = id()
		user.set_password(password)
		user.save()
		new_user = authenticate(email=user.email,password=password)
		login(request,new_user)
		return redirect('/gpasystem/')
	return render(request, "accounts/form.html", {"form":form,"title":title})
def logout_view(request):
	logout(request)
	return redirect('/')

def profile_view(request, id):	
	queryset = IndividualGrading.objects.filter()
	context = {
		"individual_grading": queryset,
	}
	return render(request,'accounts/user.html',context)
