from django.shortcuts import render, redirect
import locale
import requests
import json
from .models import watchListItem
from django.contrib import messages
from .forms import watchListForm



locale.setlocale( locale.LC_ALL, '' );

# Create your views here.

# API KEY:  pk_3a0a055c39624e9bb16fd1d5c04d7cce

headerSPY = {}
headerDIA = {}

spyAPI_request = requests.get("https://cloud.iexapis.com/stable/stock/spy/quote?token=pk_3a0a055c39624e9bb16fd1d5c04d7cce")
diaAPI_request = requests.get("https://cloud.iexapis.com/stable/stock/dia/quote?token=pk_3a0a055c39624e9bb16fd1d5c04d7cce")


headerSPY = json.loads(spyAPI_request.content);
headerDIA = json.loads(diaAPI_request.content);


def home (request):

	import requests ### this is to enable internet requests for API, this was required to be downloaded
	import json

	
	dougsAPI_request = requests.get("https://cloud.iexapis.com/stable/stock/jblu/quote?token=pk_3a0a055c39624e9bb16fd1d5c04d7cce")
	

	try:
		result = json.loads(dougsAPI_request.content)
		headerSPY = json.loads(spyAPI_request.content);
		headerDIA = json.loads(diaAPI_request.content);
		
	except Exception as e:
		result =  "This didnt freeking work!"



	return render (request, 'home.html', {'result': result, 'place_holder': 'spanoosh!', 'quantity': '10', 'headerDIA':headerDIA,'headerSPY': headerSPY})

def secondPage(request):
	return render (request, 'secondPage.html', {'headerSPY':headerSPY})

def quoteResult(request):

	import requests ### this is to enable internet requests for API, this was required to be downloaded
	import json

	marketCap = "void"
	capLable = "No Data"
	roundedMarketCap = 0
	absluteChange = 0
	roundedChangePercent = 1
	passDictionary ={}
	errorCode = 0;


	if request.method == "POST":

		requestedStock = request.POST['ticker']

		API_request = requests.get("https://cloud.iexapis.com/stable/stock/"+requestedStock+"/quote?token=pk_3a0a055c39624e9bb16fd1d5c04d7cce")


		try:
			result = json.loads(API_request.content)

			passDictionary['companyName']= result.get('companyName');
			passDictionary['change']= result.get('change');
			passDictionary['latestPrice']= result.get('latestPrice');



			if result.get('marketCap') > 1000000000000:
				passDictionary["roundedMarketCap"] = round(result.get('marketCap')/1000000000000,2)
				passDictionary["capLable"] = "Trillion"
			elif (result.get('marketCap') > 1000000000 and result.get('marketCap') < 1000000000000):
				passDictionary["roundedMarketCap"]= round(result.get('marketCap')/1000000000,2)
				passDictionary["capLable"] = "Billion"
			elif (result.get('marketCap') > 1000000 and result.get('marketCap') < 1000000000):
				passDictionary["roundedMarketCap"] = round(result.get('marketCap')/1000000,2)
				passDictionary["capLable"] = "Milion"

			passDictionary["absoluteChange"] = abs(result.get('change'))
			passDictionary["roundedChangePercent"] = abs((round(result.get('changePercent'),3))*100)

			passDictionary['result'] = result;
			###marketCap = locale.currency(result.get('marketCap'), grouping = True)

		
		
		except Exception as e:
			result =  "No Data Found for that Symbol "+ requestedStock+""

		return render (request, 'quoteResult.html', passDictionary,)
	else:

		errorCode = 1;
		passDictionary ["errorCode"] = errorCode
		return render (request, 'quoteResult.html', passDictionary,)	


def add_trade(request):
	return render (request, 'add_trade.html', {})

def watchlist(request):

	if request.method == "POST":
		form = watchListForm(request.POST or None)

		if form.is_valid():
			form.save()
			alertType =0
			messages.success(request, ("The watchlist item has been added!"))
			
			return redirect('watchlist')

			

	else:	
		item = watchListItem.objects.all()
		return render (request, 'watchlist.html', {'watchListItem':item})



def deleteWachlistItem(request, watchList_id):

	item = watchListItem.objects.get(pk=watchList_id);
	item.delete();
	alertType = 1
	messages.success(request, ("The watchlist item has been deleted"));
	return redirect('watchlist')



