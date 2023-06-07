from django.urls import path
# from .views import home
from .views import AddressView

#app_name = 'addresses'

urlpatterns = [
   # path('home/', home, name='home'),
   path('', AddressView.as_view(), name='home'),
]