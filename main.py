from bs4 import BeautifulSoup
import requests

web_page = "https://news.ycombinator.com/news"
response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)



article = soup.find_all(name="span", class_="titleline")
# print(article)
# final_article_tag = article_tag.find_all(name="a")
article_texts = []
article_links = []
scores = []

for article_tag in article:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.find(name="a").get("href")
    article_links.append(link)

# article_upvote = soup.find(name="span", class_="score").getText() #can't use gettext() because using find_all gives you a list
article_upvote = soup.find_all(name="span", class_="score")
for vote in article_upvote:
    score = int(vote.getText().split(" ")[0])
    scores.append(score)

print(article_texts)
print(article_links)
print(scores)
# print(int(scores[0].split(" ")[0]))

largest_numer = max(scores)
print(largest_numer)
largest_index = scores.index(largest_numer)
print(scores.index(largest_numer))
print(article_texts[largest_index])














# import lxml
#
# with open("website.html", encoding='utf-8') as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# # below are example of using different tag names
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup)
# # print(soup.prettify())
#
# # print(soup.a) #provide the first anchor tag that it finds in our website
# # print(soup.li)
# # print(soup.p) #proivde the first "p tags" paragraph that it finds in our website
#
# #provide all of the anchor tags in our website
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
#
# #provide all of the paragraphs in our website
# all_paragraph_tags = soup.find_all(name="p")
# print(all_paragraph_tags)
#
# #how to extract just the text?
# for tag in all_anchor_tags:
#     print(tag.getText())
#
# #how to get all the links?
# for tag in all_anchor_tags:
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# print(section_heading.getText()) # if we wanted to get hold of the text that's contained in that h3, then we simply use the getText method,
# print(section_heading.name) # if we want to know the name of that particular tag
# print(section_heading.get("class")) #if we want to get hold of the value of an attribute, for example, get the class value,
#
#
#
# # What's unique about this particular anchor tag?
# # Well,it sits inside a strong tag and it sits inside an emphasis tag and it sits inside a paragraph tag, which itself is in the body.
# # We can narrow it down using these steps.
# # <body>
# # 	<h1 id="name">Angela Yu</h1>
# # 	<p><em>Founder of <strong><a href="https://www.appbrewery.co/">The App Brewery</a></strong>.</em></p>
# # <body>
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# #You can also use the class or the ID in your CSS selector. So let's say we want to get hold of this h1, which has an ID of name,
# name = soup.select_one(selector="#name")
# print(name)
#
#
# # finally you can use a CSS selector to select an element by class and FIND all class with heading tag
# headings = soup.select(selector=".heading")
# print(headings)
#
# #ORIGINAL ANSWER using the internet:
# # contents = open("website.html", "rt")
# # print(contents.read())