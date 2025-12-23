from django.urls import path
from risk_app.views import home
urlpatterns = [
    path('',home,name='home'),
]