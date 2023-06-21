import uuid
from django.db import models
from django.conf import settings
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.urls import reverse


from .utils import unique_slug_generator

# Create your models here.
PROJECT_PLATFORM_TYPE_CHOICES = (
    ('Web', 'Web'),
    ('Mobile', 'Mobile')
)

class Project(models.Model):
    class ProjectStatus(models.TextChoices):
        Initiated = 'Initiated'
        Planning = 'Planning'
        InProgress = 'In-Progress'
        OnHold = 'On-Hold'
        Completed = 'Completed'
        Cancelled = 'Cancelled'
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    name = models.CharField( max_length=255,unique=True)
    slug = models.SlugField(max_length=100,unique=True)
    description = models.TextField(blank=True,null=True)
    platform = models.CharField( max_length=255,choices=PROJECT_PLATFORM_TYPE_CHOICES)
    repository_url = models.CharField(max_length=300) #project git repository
    production_url = models.CharField(max_length=200,null=True,blank=True) #app package_name or web url or public ip address of the project
    parent_project = models.ForeignKey('self', on_delete=models.CASCADE,null=True,blank=True,related_name='customized_projects')
    status = models.CharField( max_length=55,choices=ProjectStatus.choices,default=ProjectStatus.Initiated)
    commence_date = models.DateField(auto_now=False, auto_now_add=False)
    completion_date = models.DateField(auto_now=False, auto_now_add=False,null=True)
    release_date = models.DateField(auto_now=False, auto_now_add=False,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = ("Project")
        verbose_name_plural = ("Projects")
        ordering = ('-created_at',)

    def __str__(self):
        return self.name
    
    @property #make project a child if it has a parent project
    def is_child(self):
        if self.parent_project is not None:
            return False
        return True
    
    def get_absolute_url(self):
        return reverse("project-detail", kwargs={"pk": self.pk})
    
    @receiver(pre_save, sender='project.Project')
    def auto_slug(sender, instance, **kwargs):
        """Auto populates slug from name for the Project model"""
        instance.slug = unique_slug_generator(instance)
    
