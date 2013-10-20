from django.shortcuts import render_to_response
from whip.settings import HOME_URL
from whip_data import forms

def index(request):
	zipcode_form = forms.SelectLocationByZipcodeForm()
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
				'hidden_zipcode_form': hidden_zipcode_form,
				'zipcode_get_string': '?%s' % (urlencode( [('zipcode', zipcode)] )),
				'zipcode': zipcode,
				'scope_get_string': '&%s' % (urlencode( [('scope', scope)] )),
				'scope': scope,
				'not_location_get_string': '&%s' % (urlencode([('not_location', l) for l in not_locations])),
				'not_locations': not_locations,
				'variety_get_string': '&%s' % (urlencode([('variety', v) for v in varieties])),
				'varieties': varieties,
				'year_get_string': '&%s' % (urlencode( [('year', curyear)] )),
				'year_url_bit': year_url_bit,
				'curyear': curyear,
				'maxyear': maxyear,
				'page': page,
				'message': message,
				'years': years,
				'blurbs' : unit_blurbs,
				'curfield' : fieldname,
				'show_appendix_tables': False,
			},
			context_instance=RequestContext(request)
		)
