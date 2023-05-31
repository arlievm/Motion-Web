from .models import Services
from rest_framework import serializers as s


class Services(s.Serializer):
    
    class Meta:
        model = Services
        fields = 'sourcing', 'design_one','mobileappl_one', 'design_two', 'design_three', 'mobileappl_two'
    
    
class CustomServices(s.Serializer):
    
    class Meta: 
        model = Custom
        fields = 'photo','title_en','title_ru'


class Proect(s.Serializer):
    
    class Meta:
         
        model = Proect
        fields = 'photo','title_ru_pro','url'

class Team(s.Serializer):
    
    class Meta:
        
        model = Team 
        fields = 'photo','title_ru_name','designer','whatapp','instagram','linkedin'
        
        
        
class Instruments(s.Serializer):
    
    class Meta:
        model = Instruments
        fields = 'title_ru_tehnol','parent_instrument','name'
        

class TechnologiesCategory(s.Serializer):
    
    class Meta:
        model = TechnologiesCategory
        fields = 'title'
        
        
class Technologies(s.Serializer):
    class Meta:
        model = Technologies
        fields = 'category','name','image'


class Feedback(s.Serializer):
    
    class Meta:
        model = Feedback
        fields = 'name_one', ' iphone', 'email'