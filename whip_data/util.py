from whip_data import models
from math import sin, cos, atan2, radians, sqrt

def the_locations_near(zipcode):
	locations = models.Location.objects.all()
	try:
		zipcode_query = models.Zipcode.objects.filter(zipcode=zipcode)
		zipcode = zipcode_query.get() # should only be one result
	except (ValueError, models.Zipcode.DoesNotExist) as instance:
		raise models.Zipcode.DoesNotExist(instance)
	lat1 = float(zipcode.latitude) 
	lon1 = float(zipcode.longitude)
	"""
	From http://www.movable-type.co.uk/scripts/latlong.html
	Haversine formula:
	"""
	distances = {} # location: it's distance from this zipcode
	R = 6378137.0 # Earth's median radius (meters)
	for location in locations: 
		lon2 = float(location.zipcode.longitude)
		lat2 = float(location.zipcode.latitude)
		delta_lon = radians(lon2 - lon1)
		delta_lat = radians(lat2 - lat1)
		lon1r = radians(lon1)
		lat1r = radians(lat1)
		lon2r = radians(lon2)
		lat2r = radians(lat2)
		a = sin(delta_lat / 2.0)**2.0 + cos(lat1r)*cos(lat2r)*sin(delta_lon / 2.0)**2.0
		c = 2*atan2(sqrt(a), sqrt(1.0-a))
		d = R * c
		distances[location] = d
	return sorted(distances, key=lambda location: distances[location])
