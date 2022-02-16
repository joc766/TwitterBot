import botometer

twitter_app_auth = {
    'consumer_key':"5XCSYuQrM6drq8sUCE3KtqyB5",
    'consumer_secret':"HTgoUyg3uPyjl8IIEnjGk8QLTu9h1l21vi8CUQCK0HfgHTdiZZ",
    'access_token':"1488596326455693314-meMb01EzUGpuoBop1VQXF9Ez1aXHKw",
    'access_token_secret':"wHuykQWGzdxn6DgF7d81VQtc08sNSYVVCaXw9nMC9fZNJ"
    } 

botometer_api_url = "botometer-pro.p.rapidapi.com"
rapidapi_key = "27d58fdb5amshe852f1856da4cf6p141d39jsn742483a097cd"

botom = botometer.Botometer(
                wait_on_ratelimit = True,
                rapidapi_key = rapidapi_key,
                **twitter_app_auth)
result = botom.check_account('JackOCo64130255')
print(result)