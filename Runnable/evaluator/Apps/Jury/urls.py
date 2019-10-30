from django.urls import path
from Apps.Jury.views import index 
urlpatterns = [
    path('', index)
]
