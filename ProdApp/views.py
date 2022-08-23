from django.shortcuts import render,redirect
from django.http import HttpResponse
from . forms import ProductForm,ProdForm  
#from django.template import loader
from . models import Product
from django.contrib import messages

# Create your views here.

def index(request):
    return HttpResponse("Hello world!")
    
def prod_view(request):
    
    form = ProductForm()
   
    context={'form':form}
    
    if request.method == 'POST':
        
        form = ProductForm(request.POST)
        
        if form.is_valid():
            
            uom = form.cleaned_data.get('uom') # here you get the selected uom
            prod_desc = form.cleaned_data.get('prod_desc')
           
            product = Product.objects.all()
            mydata = Product.objects.filter(prod_desc__icontains=prod_desc,uom=uom).values()    
            rdata =  Product.objects.raw("SELECT id,prod_id, prod_desc  FROM ProdApp_Product WHERE prod_desc LIKE 'RED%' ")
            #template = loader.get_template('ProdApp/template.html')
            context={
                'products' : product,
                'data' :mydata,
                'rdata':rdata,
                
            }
            
    
    return render(request, "ProdApp/prod_view.html", context)
    #return HttpResponse(template.render(context, request)) 


def create_Prod(request):
    
    form = ProdForm()

    if request.method == 'POST':
       
        form = ProdForm(request.POST)
        
        if form.is_valid():
           
            form.save()

            return redirect('ProdApp:prod-view')

    context = {'form': form}
    return render(request, "ProdApp/prod_form.html", context)
    