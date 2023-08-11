from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('form/', views.form_view, name='form'),
    path('confirmation/', views.confirmation_view, name='confirmation'),
    path('new_page/', views.new_page, name='new_page'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
