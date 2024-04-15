from django.urls import path
from . import views
from django.contrib import admin
#from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/',admin.site.urls),
    path('',views.index,name='index'),
    path('counter',views.counter,name='counter'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('post/<str:pk>',views.post,name='post')
    #path('logout/', LogoutView.as_view(), name='logout'),
]