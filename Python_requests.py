from pydoc import locate
from urllib import request
import requests

# GET REQ
# query = input("What u wanna search ? ")
# payload = {"q": query}
# r=requests.get("https://ahmia.fi/search/", params=payload)
# print(r.content)

# POST REQ

# query = input("What u wanna search ? ")
# payload = {"q": query}
# r=requests.post("https://ahmia.fi/search/", data=payload)
# print(r.text)

# HTTP Headers

# headers = {'content-type' : 'application/json'}
# r = requests.post('https://httpbin.org/post', headers=headers)

# print(r.request.headers['content-type'])

# HTTP Cookies used for :
# Session management
# User Personalization
# Tracking User Behaviour

# url = "https://httpbin.org/cookies"
# cookies = {'location' : 'New York'}
# r =  requests.get(url, cookies=cookies)
# print(r.text)

# r2 = requests.get('https://google.com')
# print(r2.cookies['1P_JAR'])

# requestsJar = requests.cookies.RequestsCookieJar()
# requestsJar.set("userId", "Shreya30", domain="httpbin.org", path = "/cookies")
# requestsJar.set("cartItem", "Iphone", domain="httpbin.org", path = "/cart")
# r3 = requests.get(url, cookies=requestsJar)
# print(r3.text)

# r = requests.get("https://httpbin.org/status/timeout=0.1")
# r.raise_for_status()

# REDIRECTION

# r = requests.get('http://github.com')# Github will automatically redirect to https
# # r = requests.get('http://github.com', allow_redirects= False)# Doesnt allow redirection
# # print(r.url)
# # print(r.status_code)
# print(r.history)

# SESSIONS

# Creates a new request session object
s = requests.Session()
userName = {'userName':'Shreya'}
location = {'location':'NewYork'}

setCookieUrl = 'https://httpbin.org/cookies/set' # New cookie creation where we will save data
getCookiesUrl = 'https://httpbin.org/cookies' # Return all cookies setup in the server for session

s.get(setCookieUrl, params=userName)
s.get(setCookieUrl, params=location)

r = s.get(getCookiesUrl)
print(r.text)