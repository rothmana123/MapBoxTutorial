from django.shortcuts import render
from .models import Address
from django.views.generic.edit import CreateView



# Create your views here.
class AddressView(CreateView):

    model = Address
    fields = ['address', 'name']
    template_name = 'addresses/home.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mapbox_access_token'] = 'pk.eyJ1IjoidHVuYWhvYmJ5IiwiYSI6ImNra3IwaDNxcTBtbzAycm81dTFpOWhvcjAifQ.8ixXcuSDUuAlDSlazSLMCA'
        context['addresses'] = Address.objects.all()
        return context

# def home(request):
#     addresses = Address.objects.all()  # Fetch all addresses from the database
#     for address in addresses:
#         print(address.address)  
#     context = {'addresses': addresses}  # Create a context dictionary with the addresses
#     return render(request, 'addresses/home.html', context)