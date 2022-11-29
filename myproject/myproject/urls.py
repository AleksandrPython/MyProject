"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path
from testing import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('profile', views.profile),
    path('pagetesting', views.pagetesting),
    path('newquestion', views.newquestion),
    path('pagequestion/<int:id>', views.pagequestion),
    path('pagetest', views.pagetest),
    path('pageeditquest/<int:id>', views.pageeditquest),
    path('saveeditquest/<int:id>', views.saveeditquest),
    path('pagedeletquest/<int:id>', views.pagedeletquest),
    path('pagereg', views.pagereg),
    path('pagein', views.pagein),
    path('checkboxes', views.checkboxes),


]
