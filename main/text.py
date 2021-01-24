from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import models
from . models import Tutorial,Category,Series
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm


def Singleslug(request,single_slug):
	categories = [c.categorySlug for c in Category.objects.all()]
	if single_slug in categories:
		matchFilter = Series.objects.filter(categoryName__categorySlug = single_slug)

		series_url = {}
		for m in matchFilter.objects.all():
			partOne = Tutorial.objects.filter(seriesName__seriesName = m.seriesName).earlist('Publishdate')
			series_url[m] = partOne.tutorialSlug

		return render(request= request, template_name="category.html",context='tutorialSeries':matchFilter,'partOne':series_url)

	tutorials = [t.tutorialSlug for t in Tutorial.objects.all()]
	if single_slug in tutorials:
		disTut = Tutorial.objects.get(tutorialSlug=single_slug)
		Tutseris = Series.objects.filter(seriesName__seriesName=disTut.seriesName).order_by('Publishdate')
		Tutindex = list(Tutseris).index(disTut)
		return render(request=request,template_name="tutorial.html",context="tutorial":disTut,"sidebar":Tutseris,"Tutdex":Tutindex)


def single_slug(request,single_slug):
	categories = [c.category_slug for c in Category.objects.all()]
	if single_slug in categories:
		match_series = Series.objects.filter(tutorialCategory__category_slug = single_slug)

		series_urls = {}
		for m in match_series.objects.all():
			onePart = Tutorial.objects.filter(tutorialSeries__tutorialSeries=m.tutorialSeries).earlist('Publishdate')
			series_url[m] = onePart.tutorial_slug
		return render(request = request,template_name="category.html",context="Tutorialseries":match_series,"partyzone":series_urls)

	tutorials = [t.tutorial_slug for t in Tutorial.objects.all()]
	if single_slug in tutorials:
		thisTut = Tutorial.objects.get(tutorial_slug = single_slug)
		TutSeries =Series.objects.filter(tutorialSeries__tutorialSeries=thisTut.tutorialSeries).order_by('Publishdate')
		Tutindex = list(TutSeries).index(thisTut)
		return render(request=request,template_name="tutorial.html",context="tutorial":thisTut,"sidebar":TutSeries,"index":Tutindex)
