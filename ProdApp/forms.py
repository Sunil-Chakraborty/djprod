from django import forms
from django.forms import ModelForm, widgets
from django.forms import ValidationError
from django.http import HttpResponse
from . models import Product
  
class ProductForm(forms.Form):
    uom = forms.CharField(label='U.O.M', max_length=5)
    prod_desc = forms.CharField(label='Short Desc.', max_length=50)
    
   
class ProdForm(forms.ModelForm):    
    class Meta:
        model = Product
        fields = "__all__"
        
    def clean_prod_id(self):
        prod_id = self.cleaned_data.get('prod_id')
        prd_id = Product.objects.filter(prod_id=prod_id)
        
        if prd_id:
            raise forms.ValidationError(
                    "Prod id is taken"
                )
        return prod_id        