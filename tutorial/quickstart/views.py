from django.contrib.auth.models import User, Group
from models import Company, Country, City, Customer
from rest_framework import viewsets
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer, CompanySerializer, CountrySerializer, CitySerializer, CustomerSerializer

class UserViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows users to be viewed or edited.
    """ 
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows groups to be viewed or edited.
    """ 
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CountryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = Country.objects.all()
    serializer_class = CountrySerializer	
	
class CityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer		
	
class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows companies to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer		
	