import requests
def requestApi():
    response = requests.get('http://203.150.95.65/shops/')
    print('response = ' + response.text)
requestApi()