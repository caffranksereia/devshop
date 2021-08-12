from . import views
from django.urls import path
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('/All_search_users', views.All_search_users, name='All_search_users')
]