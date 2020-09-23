# i had to add this entire file
from django.urls import path
from . import views # I needed to add this

urlpatterns = [
	path('', views.home, name= "home"),
	path('secondPage', views.secondPage, name= "secondPage"),
	path('quoteResult', views.quoteResult, name= "quoteResult"),
	path('add_trade', views.add_trade, name= "add_trade"),
	path('watchlist', views.watchlist, name= "watchlist"),
	path('deleteWachlistItem/<watchList_id>',views.deleteWachlistItem, name = "deleteWachlistItem")
]