import requests
from bs4 import BeautifulSoup

# Get weather in Vienna from Google
data = requests.get("https://www.google.com/search?q=weather+in+vienna&oq=weather+in+vienna&aqs=edge..69i57j0i512l7j69i64.3603j1j1&sourceid=chrome&ie=UTF-8").content
soup = BeautifulSoup(data, 'html.parser')
div = soup.find("div", {"class":"BNeawe iBp4i AP7Wnd"})
weatherAustria = div.text
# Get weather in Budapest from Google
data = requests.get("https://www.google.com/search?q=weather+in+budapest&sxsrf=AJOqlzWktfEP8HZEvtmB1J83laUgcJg82Q%3A1678321067694&ei=qyUJZJv6KbKcptQP5rOAuAw&ved=0ahUKEwjb-7uYyc39AhUyjokEHeYZAMcQ4dUDCBE&uact=5&oq=weather+in+budapest&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQA0oECEEYAFAAWABgAGgAcAF4AIABAIgBAJIBAJgBAKABAQ&sclient=gws-wiz-serp").content
soup = BeautifulSoup(data, 'html.parser')
div = soup.find("div", {"class":"BNeawe iBp4i AP7Wnd"})
weatherBudapest = div.text


print("Vienna, Austria, is %s degrees today. Budapest, Hungary, is %s degrees today" % (weatherAustria, weatherBudapest))