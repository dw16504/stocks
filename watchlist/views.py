from django.shortcuts import render

# Create your views here.


def watchlist(request):


	#watchListItem = watchListItem.objects.all()
	return render (request, 'home.html', {})