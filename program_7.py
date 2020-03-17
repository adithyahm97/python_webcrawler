import requests
from bs4 import BeautifulSoup

res = requests.get("https://stackoverflow.com/questions")

soup = BeautifulSoup(res.text, "html.parser")

questions_data = {
    "questions": []
}

questions = soup.select(".question-summary")

for que in questions:
    q = que.select_one('.question-hyperlink').getText()
    print(q)




