from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from exchange.models import Exchange
from .models import Stock
from .serializers import StockSerializer

resultData = []

@api_view(['GET'])
def getAllStocks(request):
    
    exchangeName = ['NASDAQ', 'NYSE']
    
    url = "https://twelve-data1.p.rapidapi.com/stocks"
    for exchange in exchangeName:
        querystring = {"exchange": exchange, "format": "json"}
        headers = {
            "X-RapidAPI-Key": "c7363c18fbmsh19cafb5d660de9ap103768jsnac4fb27f97dc",
            "X-RapidAPI-Host": "twelve-data1.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        count = 0
        stockList = ''
        for stock in response.json()['data']:
            count += 1
            if count<=200:
                stockList = stockList + stock['symbol'] + ','
            else:
                stockList
                callNextAPI(stockList[:-1], exchange)
                stockList = stock['symbol'] + ','
                count = 1
        if len(stockList) !=0:
            callNextAPI(stockList[:-1], exchange)
    # callNextAPI(None, '')
    # totalPercent = 0
    # for item in resultData:

    #     totalPercent += item["regularMarketChangePercent"]
        
    # resultData = [
    #     {
    #         "symbol": 'CCAIW',
    #         "name": 'Cascadia Acquisition Corp.',
    #         "marketCap": 100000,
    #         "exchange": 'Nasdaq',
    #         "preMarketChangePercent": 20.23,
    #         "postMarketChangePercent": 45.56,
    #         "regularMarketPrice": 8.36,
    #         "regularMarketChangePercent": 8.0
    #     },
    #     {
    #         "symbol": 'LQR',
    #         "name": 'LQR House Inc.',
    #         "marketCap": 14252868,
    #         "exchange": 'NYSE',
    #         "preMarketChangePercent": 1.02,
    #         "postMarketChangePercent": 21.54,
    #         "regularMarketPrice": 12.07,
    #         "regularMarketChangePercent": 0.1703
    #     }
    # ]
    
    return Response(sorted([stock for stock in resultData if stock['regularMarketChangePercent'] is not None], key=lambda x: x['regularMarketChangePercent'], reverse=True))
    # return Response("Total Percent: " + str(totalPercent))

def callNextAPI(stockList, exchangeName):
    # stockList = "META, SNAP,CRM,EBAY,TTD,APPS,HUBS,NYT,FLNT,NTES,SCOR,BZUN,Y,OMC,NWSA,IPG,NWS,LAMR,WPP,ILLM,NCMI"
    url = "https://mboum-finance.p.rapidapi.com/qu/quote"
    querystring = {"symbol":stockList}
    headers = {
        "X-RapidAPI-Key": "c7363c18fbmsh19cafb5d660de9ap103768jsnac4fb27f97dc",
        "X-RapidAPI-Host": "mboum-finance.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    

    for result in response.json():
        data = {
                "symbol": '',
                "name": '',
                "marketCap": 0,
                "exchange": exchangeName,
                "preMarketChangePercent": 0,
                "postMarketChangePercent": 0,
                "regularMarketPrice": 0,
                "regularMarketChangePercent": 0
            }
        
        if 'symbol' in result:
            data['symbol'] = result['symbol']
        if 'longName' in result:
            data['name'] = result['longName']
        if 'marketCap' in result:
            data['marketCap'] = result['marketCap']
        if 'preMarketChangePercent' in result:
            data['preMarketChangePercent'] = result['preMarketChangePercent']
        if 'postMarketChangePercent' in result and 'postMarketChangePercent' != None:
            data['postMarketChangePercent'] = result['postMarketChangePercent']
        if 'regularMarketPrice' in result:
            data['regularMarketPrice'] = result['regularMarketPrice']
        if 'regularMarketChangePercent' in result:
            data['regularMarketChangePercent'] = result['regularMarketChangePercent']

        resultData.append(data)
            
        stock = Stock.objects.create(**data)
        serializer = StockSerializer(stock, many=False)