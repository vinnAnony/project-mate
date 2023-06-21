import django_filters
from .models import Project

class ProjectFilter(django_filters.FilterSet):
     
   
     class Meta:
         model = Project
         fields = {
            'name': ['icontains'],
            'created_at':['lt', 'gt']
          }