from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='StockMarket/')),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('StockMarket/', views.StockMarket, name='StockMarket'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='home.html'), name='logout'),
    path('load/', views.load_more, name='load'),
    path('details/<int:id_num>', views.details, name='details'),
    path('query/<int:id_num>', views.query, name='query'),

]
