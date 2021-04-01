from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")  # get webpage source html code

yc_webpage = response.text
articles_text = []
articles_links = []
articles_scores = []
soup = BeautifulSoup(yc_webpage, "html.parser")

titles = soup.find_all(name="a", class_="storylink")

for title in titles:
    articles_text.append(title.getText())
    articles_links.append(title.get("href"))

scores = soup.find_all(name="span", class_="score")
for score in scores:
    articles_scores.append(int(score.getText().split(" ")[0]))

print(articles_text) # the indices in each list are corresponding
print(articles_links)
print(articles_scores)

# Printing the article title, link with the highest score

counter_score = 0
for article_score in articles_scores:  # finding the highest score
    if int(article_score) > counter_score:
        counter_score = int(article_score)
    else:
        continue

highest_upvote = articles_scores.index(counter_score)  # finds the index of the highest score

print(articles_text[highest_upvote])
print(articles_links[highest_upvote])
print(articles_scores[highest_upvote])






# import lxml
#
#
# with open("website.html",'r', encoding="utf-8") as file:   # open the html file and stores its contents into a variable
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")  # first arguments is the html file contents second is what language
#
# # The soup object represents our entire HTML code
# # Beautiful SOup is essentially drilling down in the HTML file and finding the html tag we are interested in
# # and getting hold of the name of the tag or the actual text inside the tag
#
# # print(soup.title)  # prints the entire title tag in the html file
# # print(soup.title.name) # prints the name of the tag, which is title
# # print(soup.title.string)  # prints the contents aka the string inside the title tag
# # print(soup.prettify()) prints entire HTML code
# # print(soup.a)  # prints the entire first anchor tag
#
# all_anchor_tags = soup.find_all(name="a")
# # print(all_anchor_tags)  # prints a list of all anchor tags in the html file
#
# for tag in all_anchor_tags:
#     # print(tag.getText())  prints the text inside every anchor tag
#     print(tag.get("href"))  # prints all the href attribute in every anchor tag
#
#
# # Search a particular element
# heading = soup.find(name="h1", id="name")  warning: this returns only the first element with such name and id
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
#
# company_url = soup.select_one(selector="p a ") # gets hold a particular anchor tag, the one nested in a paragraph
# # we can also use as selectors the id name (with # in front) or class name (with . in front)
# print(company_url)
#
# headings = soup.select(selector=".heading")
# print(headings)
