# urls.py
from django.urls import path
from . views import *

# add new one
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView




urlpatterns = [
# add new one
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    
    path('User/', manage_User),
    path('User/<int:id>/', manage_User),

    path('CrimeType/',manage_CrimeType),
    path('CrimeType/<int:id>/', manage_CrimeType),

    path('Location/', manage_Location),
    path('Location/<int:id>/', manage_Location),

    path('Report/', manage_Report),
     path('Report/<int:id>/', manage_Report),

]
