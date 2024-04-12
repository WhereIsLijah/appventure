from django.contrib import admin
from django.urls import path
from gatekeeper import views 

urlpatterns = [
    path("admin/", admin.site.urls),
    path('home/', views.index, name='index'), #Homepage view
    path('login/', views.user_login, name='login'),  # Login view
    path('signup/', views.user_signup, name='signup'),  # Signup view
]
