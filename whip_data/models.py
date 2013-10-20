from django.db import models
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.
class Variety(models.Model):
	name						= models.CharField(max_length=200, help_text='')
	description_url = models.CharField(max_length=200, blank=True, null=True, help_text='A link to a resource that describes this variety.')
	picture_url		 = models.CharField(max_length=200, blank=True, null=True, help_text='A link to a small picture of this variety.')
	# agent_origin, year_released, straw_length, maturity, grain_color, seed_color, beard, wilt, diseases
	
	def __unicode__(self):
		return self.name
	
	def natural_key(self):
		return (self.name,);
	
	class Meta:
		ordering = ["-name"]

class VarietyManager(Variety):
	def get_by_natural_key(self, lookup):
		return self.get(name=lookup)

class Zipcode(models.Model):
	zipcode					= models.PositiveIntegerField()
	city						 = models.CharField(max_length=200)
	state						= models.CharField(max_length=2)
	latitude				 = models.DecimalField(decimal_places=10, max_digits=13)
	longitude				= models.DecimalField(decimal_places=10, max_digits=13)
	timezone				 = models.SmallIntegerField()
	daylight_savings = models.SmallIntegerField()
	
	def __unicode__(self):
		return str(self.zipcode).zfill(5) + ": " + self.city + ", " + self.state

class Location(models.Model):
	name			= models.CharField(max_length=200, help_text='')
	zipcode	 = models.ForeignKey(Zipcode, help_text='Format: 12345, The five-digit zipcode of this location.')
	
	def __unicode__(self):
		return self.name

class Date(models.Model):
	date	= models.DateField(help_text='Format: MM/DD/YYYY')
	
	def __unicode__(self):
		return str(self.date)
		
class Trial_Entry(models.Model):
	bushels_acre         = models.DecimalField(decimal_places=5, max_digits=10, help_text='Format: 37.4, Bushels per Acre')
	protein_percent      = models.DecimalField(decimal_places=5, max_digits=8, blank=True, null=True, help_text='Format: 12.1, Percentage of protein per pound')
	test_weight          = models.DecimalField(decimal_places=5, max_digits=10, blank=True, null=True, help_text='Format: 50.1, Pounds per bushel')
	planting_method_tags = models.CharField(max_length=200, blank=True, null=True, help_text='Comma-separated list of planting methods')
	previous_crop        = models.CharField(max_length=200, blank=True, null=True, help_text='Name of the previous crop at this location')
	lsd_05               = models.DecimalField(decimal_places=5, max_digits=10, blank=True, null=True, help_text='Bushels per Acre LSD at a=0.05 (for the entire location in this year)')
	lsd_10               = models.DecimalField(decimal_places=5, max_digits=10, blank=True, null=True, help_text='Bushels per Acre LSD at a=0.10 (for the entire location in this year)')
	hsd_10               = models.DecimalField(decimal_places=5, max_digits=10, blank=True, null=True, help_text='Bushels per Acre HSD at a=0.05 (for the entire location in this year)')
	plant_date           = models.ForeignKey(Date, related_name='plant_date', blank=True, null=True, help_text='Date this trial was planted')
	harvest_date         = models.ForeignKey(Date, related_name='harvest_date', help_text='Date this trial was harvested')
	location             = models.ForeignKey(Location, help_text='Name of location')
	variety              = models.ForeignKey(Variety, help_text='Name of variety')
	#kernel_weight, plant_height, days_to_head, lodging_factor, jday_of_head, winter_survival_rate, shatter, seeds_per_round, canopy_density, canopy_height, days_to_flower, seed_oil_percent, moisture_basis, seeding_rate
	
	def __unicode__(self):
		return '%s at %s, %s' % (self.variety, self.location, self.harvest_date.date.year)
		
class Trial_Entry_History(models.Model):
	username     = models.CharField(max_length=200)
	created_date = models.DateField()
	trial_entry  = models.ForeignKey(Trial_Entry, on_delete=models.DO_NOTHING)
	
	def __unicode__(self):
		try:
			trial = str(self.trial_entry)
		except ObjectDoesNotExist:
			trial = None
		except:
			trial = None
		return '%s by %s on %s' % (trial, self.username, self.created_date)
