# this file needs to be mirrored.

# i had to add this entire file
from django.urls import path
from . import views # I needed to add this

urlpatterns = [
	path('watchlist', views.watchlist, name= "watchlist")
]
