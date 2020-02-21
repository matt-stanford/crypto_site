from django.shortcuts import render

def home(request):
    import requests
    import json

    # Grab Crypto Price Data
    price_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=GBP')
    price = json.loads(price_request.content)

    # Grab Crypto News
    api_request = requests.get('https://min-api.cryptocompare.com/data/v2/news/?lang=EN')
    api = json.loads(api_request.content)
    return render(request, 'home.html', {'api': api, 'price': price})

def prices(request):
    import requests
    import json

    if request.method == 'POST':
        quote = request.POST['quote']
        crypto_request = requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=' + quote.upper() + '&tsyms=GBP')
        crypto = json.loads(crypto_request.content)
        return render(request, 'prices.html', {'quote': quote, 'crypto': crypto})

    else:
        return render(request, 'prices.html', {})
