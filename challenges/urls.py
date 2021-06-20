from django.urls import path
from . import views

urlpatterns = [
    path('<int:month>', views.monthly_challenges_by_number, name='month_challenge'),
    path('<str:month>', views.monthly_challenges)
]
