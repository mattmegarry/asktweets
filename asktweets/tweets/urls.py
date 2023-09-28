from django.urls import path
from .views import ListMPs

urlpatterns = [
    path('mps', ListMPs.as_view(), name='mps'),
]