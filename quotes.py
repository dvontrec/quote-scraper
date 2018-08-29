import requests
from bs4 import BeautifulSoup
from csv import writer
import random
url = "http://quotes.toscrape.com/"
quoteChoices = []
# While loop that will run forever unless broken
while True:
  # requests the data from the url
  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")
  nextL = soup.select(".next a")
  quotes = soup.select(".quote")
  for quote in quotes:
    words = quote.find("span").getText()
    speaker = quote.select(".author")[0].getText()
    quoteChoices.append({"quote": words, "author": speaker})
  # If the page has a next button
  if nextL:
    # change the url to the next page
    url = "http://quotes.toscrape.com/" + nextL[0]["href"]
  else:
    # Breaks the while loop
    break

while True:
  play = input("Hello, Would you like a new quote (y/n): ")
  if play == "y":
    selected = quoteChoices[random.randint(0, len(quoteChoices) - 1)]
    print(f"{selected['author']}, once said {selected['quote']}")
  elif play == "n":
    break
  else:
    print("Please type a Y or an N")
