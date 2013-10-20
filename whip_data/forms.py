from django import forms

# forms for the report view
class SelectLocationForm(forms.Form):
	zipcode = forms.CharField(
			max_length=5, 
			required=True,
			help_text=''
		)
	#scope, year, not_location, variety

# Custom forms to populate our database
class VarietyForm(forms.ModelForm):
	class Meta:
		model = Variety
		
class Trial_EntryForm(forms.ModelForm):
	class Meta:
		model = Trial_Entry
		# exclude any ForeignKey or ManyToMany fields
		# and/or don't allow the user to effect certain fields
		#exclude = (,)
		
class LocationForm(forms.ModelForm):
	class Meta:
		model = Location
		
class DateForm(ModelForm):
	class Meta:
		model = Date
