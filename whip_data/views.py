from django.shortcuts import render_to_response
from whip.settings import HOME_URL
from whip_data import forms

def index(request):
	zipcode_form = forms.SelectLocationForm()
	return render_to_response(
			'main.html', 
			{ 
				'zipcode_form': zipcode_form,
				'home_url': HOME_URL,
			},
			context_instance=RequestContext(request)
		)

def zipcode_view(request, locations):
	return render_to_response(
			'view_report.html',
			{
				'home_url': HOME_URL,
			},
			context_instance=RequestContext(request)
		)
