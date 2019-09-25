from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from django.template.response import TemplateResponse
from django.template import loader, Context,RequestContext
from .models import Store
from .forms import ListingForm

def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")

def template(request):
	return TemplateResponse(request, 'homepage.html',)
	
def contact(request):
	return TemplateResponse(request, 'contacts.html',)

def howitworks(request):
	return TemplateResponse(request, 'howitworks.html',)
	
def article(request):
	return TemplateResponse(request, 'blog-single.html',)
	
def stores(request):
	store_list = Store.objects.all()
	context = {'store_list': store_list}
	return render(request, 'stores.html', context)

@csrf_exempt
def List_New_Store(request):
    if request.method == 'POST':
        print(request.POST.getlist)
        form = ListingForm(request.POST)
        print(form, form.errors)
    try:
        val = request.POST['email']
        print(val)
    except:
        # Redisplay the question voting form.
        return render(request,{
            'error_message': "You input something invalid.",
        })
    else:
        if form.is_valid():
            New = Store(Name = form.cleaned_data['Name'], Description = form.cleaned_data['description'], Price = form.cleaned_data['price'])
            New.save()
        print("Done")
        return HttpResponseRedirect('../contact/')

def storeDetails(request, store_id):
    try:
        thatStore = Store.objects.get(pk=store_id)
    except thatStore.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'store.html', {'store': thatStore})