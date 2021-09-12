from django import forms 
from hospital.models import instruments
from hospital.models import departments
from hospital.models import contracts
from hospital.models import order
from hospital.models import stock

class instrumentsform(forms.ModelForm):
	class Meta:
		model= instruments
		fields= "__all__"

class departmentsform(forms.ModelForm):
	class Meta:
		model=departments
		fields="__all__"

class contractsform(forms.ModelForm):
	class Meta:
		model=contracts
		fields="__all__"

class orderform(forms.ModelForm):
	class Meta:
		model=order
		fields="__all__"

class stockform(forms.ModelForm):
	class Meta:
		model=stock
		fields="__all__"
