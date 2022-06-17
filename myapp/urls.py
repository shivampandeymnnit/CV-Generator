from . import views
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views

# The code Below is for Django Header Customization
admin.site.site_header = "Developer-Swapnil's Administration"
admin.site.site_title = "Swapnil's Admin"
admin.site.index_title="Dashboard of Mr. Swapnil"


urlpatterns = [
    path('',views.index,name='index'),
    path('register/',views.register,name = 'register'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name = 'login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='index.html'),name = 'logout'),
    path('profile',views.profile,name = 'profile'),
    path('dark',views.dark,name = 'dark'),
    path('light',views.light,name = 'light'),
    path('choose',views.choose,name = 'choose'),
]