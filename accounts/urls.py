from django.urls import path
from accounts.views import CustomLoginView, CustomLogoutView, RegisterUserCreateView

app_name = 'accounts'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterUserCreateView.as_view(), name='register')
]