from django.shortcuts import render
from rest_framework import generics

from .serializers import ServicesSerializer,CustomServicesSerializer, ProectedServicesSerializer, TeamSerializer,FeedbackSerializer,FeedbackCreateListSerializer
from .models import Services,Customers, Proect , Team, Feedback


#Services
class ServicesCreateListView(generics.ListCreateAPIView):
    serializer_class = ServicesSerializer
    queryset = Services.objects.all()
    
    
class ServicesDeleteView(generics.DestroyAPIView):
    serializer_class = ServicesSerializer
    queryset = Services.objects.all()
    
    
#Customers  
class CustomersCreateListView(generics.ListCreateAPIView):
    serializer_class = CustomersSerializer
    queryset = Customers.objects.all()
    
    
class CustomersDeleteView(generics.DestroyAPIView):
    serializer_class = CustomersSerializer
    queryset = Customers.objects.all()
    
    
    
#Proect   
class ProectCreateListView(generics.ListCreateAPIView):
    serializer_class = ProectSerializer
    queryset = Proect.objects.all()

class ProectDeleteView(generics.DestroyAPIView):
    serializer_class = ProectSerializer
    queryset = Proect.objects.all()



#Team
class TeamCreateListView(generics.CreateTeamAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    
class TeamDeleteView(generics.DestroyTeamAPIView):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

#Instrumets
class InstrumentsCreateListView(generics.CreateInstrumentsAPIView):
    serializer_class = InstrumentsSerializer
    queryset = Instruments.objects.all()
    
class InstrumentsDeleteView(generics.DestroyInstrumentsAPIView):
    serializer_class = InstrumentsSerializer
    queryset = Instruments.objects.all()
    
    
#TechnologiesCategory
class TechnologiesCategoryCreateListView(generics.CreateTechnologiesAPIView):
    serializer_class = TechnologiesCategorySerializer
    queryset = Technologies.objects.all()

class TechnologiesDeleteView(generics.DestroyTechnologiesAPIView):
    serializer_class = TechnologiesCategorySerializer
    queryset = Technologies.objects.all()
    
    
#Technologies
class TechnologiesCreateListView(generics.CreateTechnologiesAPIView):
    serializer_class = TechnologiesCategorySerializer
    queryset = Technologies.objects.all()
    
class TechnologiesDeleteView(generics.DestroyTechnologiesAPIView):
    serializer_class = TechnologiesCategorySerializer
    queryset = Technologies.objects.all()

#Feedback
class FeedbackCreateListView(generics.CreateFeedbackAPIView):
    serializer_class = FeedbackCategorySerializer
    queyset = Feedback.objects.all()
    
class FeedbackDeleteView(generics.DestroyFeedbackAPIView):
    sirializer_class = FeedbackCategorySerializer
    queryset = Feedback.objects.all()