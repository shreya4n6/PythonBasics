from turtle import title
import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

# 1 Get the HTML

r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# 2 Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify())

# 3 HTML Tree Traversal
"""
Commonly used type of objects :
1. Tag : 
 print(type(title))

2. NavigableString :
# print(type(title.string))

3. BeautifulSoup :
# print(type(soup))

4. Comment :
markup = "<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup)
print(type(soup2.p.string))

"""
# Get title of HTML Page
# title = soup.title
# Get all the paras from the page
# paras =  soup.find_all('p')
# print(paras)

# Get first element in HTML
# print(soup.find('p'))
# Get class of any element in HTML
# print(soup.find('p')['class'])
# Find all the elements with class lead
# print(soup.find_all("p", class_="lead"))
# Get text from the elemets
# print(soup.find('p').get_text())
# print(soup.get_text())
# Get all the anchor tags from the page
anchors =  soup.find_all('a')
# print(anchors)

# Get all the links on the page 
# all_links = set()
# for link in anchors:
#     if(link.get('href') != '#'):
#         linkText = "https://codewithharry.com" + link.get('href')
#         all_links.add(link)
#         print(linkText)

""" 
.contents :  A tag's are available as a list (contents are stored in memory)
.children :  A tag's children are available as generator (children are not stored in memory)

"""
searchtoggle = soup.find(id='search-toggle')
# for elem in searchtoggle.strings:
#     print(elem)
# for item in (searchtoggle.parents) :
#     print(item)
#     print(item.name)
# print(searchtoggle.previous_sibling)
# CSS selector
elem = soup.select('#nav-content')
print(elem)