
import requests
from bs4 import BeautifulSoup

res = requests.get("https://stackoverflow.com/questions")

soup = BeautifulSoup(res.text, "html.parser")

questions = soup.select(".question-summary")

for que in questions:
    q = que.select_one('.question-hyperlink').getText()
    print(q)

for que in questions:
    user=que.select_one('.user-details').getText()
    print(user)









