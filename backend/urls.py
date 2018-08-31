"""hackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from backend import views

backend_patterns = [
    path('test', views.TestAPI.as_view(), name='test'),

    path('code/add', views.AddCode.as_view(), name='add'),
    path('code/view/<str:unique_code>', views.ViewSingleCode.as_view(), name='view-code'),
    path('code/count/<str:unique_code>', views.AddCount.as_view(), name='add-count'),
    path('code/all', views.GetAllCode.as_view(), name='get-all-code'),
    path('code/delete/<str:unique_code>', views.DeleteCode.as_view(), name='delete-code'),
    path('code/status/<str:unique_code>', views.ChangeStatus.as_view(), name='change-status'),

]
