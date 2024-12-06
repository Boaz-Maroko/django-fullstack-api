from django.urls import path
from .views import StudentList
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# urlpatterns
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('students/', StudentList.as_view(), name='student-list'),
]
