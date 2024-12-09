from django.urls import path
from .views import handle_mpesa, get_response

# url_patterns

urlpatterns = [
    path('mpesa/', handle_mpesa, name='mpesa'),
    path('response/', get_response, name='response'),
]