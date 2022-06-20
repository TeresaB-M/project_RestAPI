"""db_software_json URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from software_app.views import (
    SoftwareListView,
    PersonListView,
    PersonView,
    SortOfSoftwareListView,
    SortOfSoftwareView,
    TypeOfSoftwareListView,
    MySoftwareListView,
    TypeOfSoftwareView,
    NySoftwareView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('software_list/', SoftwareListView.as_view(), name='software_list'),
    path('person_list/', PersonListView.as_view(), name='person_list'),
    path('person/<int:pk>/', PersonView.as_view()),
    path('sortofsoftware_list/', SortOfSoftwareListView.as_view(), name='sortofsoftware_list'),
    path('sortofsoftware/<int:pk>/', SortOfSoftwareView.as_view()),
    path('typeofsoftware_list/', TypeOfSoftwareListView.as_view(), name='typeofsoftware_list'),
    path('typeofsoftware/<int:pk>/', TypeOfSoftwareView.as_view()),
    path('mysoftware_list/', MySoftwareListView.as_view(), name='mysoftware_list'),
    path('mysoftware/<int:pk>/', NySoftwareView.as_view()),
]
