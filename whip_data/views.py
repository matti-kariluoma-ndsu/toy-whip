from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from whip.settings import HOME_URL
from whip_data import forms, util

def index(request):
	zipcode_form = forms.SelectLocationForm()
	
	return render_to_response(
			'main.html', 
			{
				'home_url': HOME_URL,
				'zipcode_form': zipcode_form,
			},
			context_instance=RequestContext(request)
		)

def get_report(request):
	if request.method != 'GET':
		return HttpResponseRedirect(HOME_URL)
	
	zipcode_form = forms.SelectLocationForm(request.GET)
	if zipcode_form.is_valid():
		locations = util.the_locations_near(zipcode_form.cleaned_data['zipcode'])
	else:
		locations = None
	
	return render_to_response(
			'view_report.html',
			{
				'home_url': HOME_URL,
				'locations': locations,
				'variety_trials': util.trials_at(locations),
			},
			context_instance=RequestContext(request)
		)
