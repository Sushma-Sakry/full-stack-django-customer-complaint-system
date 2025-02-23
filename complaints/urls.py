
# complaints/urls.py
from django.urls import path
from .views import submit_complaint, success, complaint_list  # Import your views

urlpatterns = [
    path('', complaint_list, name='complaint_list'),  # 👈 Root path for complaints/
    path('submit/', submit_complaint, name='submit_complaint'),
    path('success/', success, name='success'),
]