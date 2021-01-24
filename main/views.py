from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import models
from . models import Tutorial,Category,Series
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm

# Create your views here.


def single_slug(request, single_slug):
	categories = [c.category_slug for c in Category.objects.all()]
	if single_slug in categories:
		matching_series = Series.objects.filter(tutorial_category__category_slug=single_slug)
		
		series_urls = {}
		for m in matching_series.all():
			part_one = Tutorial.objects.filter(tutorial_series__tutorial_series=m.tutorial_series).earliest("Tut_Date")
			series_urls[m]=part_one.tutorial_slug
		return render(request=request, template_name="main/category.html",context={"tutorial_series":matching_series,"part_ones":series_urls})

	tutorials =[t.tutorial_slug for t in Tutorial.objects.all()]

	if single_slug in tutorials:
		this_tutorial = Tutorial.objects.get(tutorial_slug=single_slug)
		tut_frm_series = Tutorial.objects.filter(tutorial_series__tutorial_series=this_tutorial.tutorial_series).order_by('Tut_Date')
		this_tut_idx = list(tut_frm_series).index(this_tutorial)

		return render(request=request,template_name="main/tutorial.html",context={"tutorial":this_tutorial,"sidebar":tut_frm_series,"tut_idx":this_tut_idx})
	return HttpResponse(f"{single_slug} does not mean anything")



def homepage(request):
	return render(request=request,template_name="main/categories.html",context={"categories":Category.objects.all})

def register(request):
	if request.method == 'POST':
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username=form.cleaned_data.get('username')
			messages.success(request,f"New Account Created:{username}")
			login(request,user)
			return redirect("main:homepage")
		else:
			for msg in form.error_messages:
				messages.error(request,f"{msg}:{form.error_messages[msg]}")
			return render(request=request,template_name="main/register.html",context={"form":form})
	form = NewUserForm()
	return render(request=request,template_name="main/register.html",context={"form":form})

def logout_request(request):
	logout(request)
	messages.info(request,f'Logout Successfully!')
	return redirect("main:homepage")

def login_request(request):
	if request.method == 'POST':
		form = AuthenticationForm(request= request,data=request.POST)
		if form.is_valid():
			username= form.cleaned_data.get('username')
			password= form.cleaned_data.get('password')
			user = authenticate (username=username,password=password)
			if user is not None:
				login(request,user)
				messages.info(request,f'You are now logged in as {username}')
				return redirect("main:homepage")
			else:
				messages.error(request,f'Invalid username or password')
		else:
			messages.error(request,f'Invalid username or password')
	form = AuthenticationForm()
	return render(request=request,template_name="main/login.html",context={"form":form})





