from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


myUrl = 'http://cimaclub.com/'
uClient = uReq(myUrl)
pageHtml = uClient.read()
uClient.close()

pageSoup = soup(pageHtml, "html.parser")
movies = pageSoup.findAll("div", {"class": "movie"})

file = "todayHomepage.csv"
saveFile = open(file, "w")
headers = "title, description, category, view, movieUrl\n"
saveFile.write(headers)

for movie in movies:

    titleList = movie.findAll("div", {"class": "boxcontentFilm"})
    title = titleList[0].h2.text
    description = titleList[0].p.text

    categoryList = movie.findAll("span", {"class": "category"})
    category = categoryList[0].text

    viewsList = movie.findAll("span", {"class": "views"})
    view = viewsList[0].text

    movieUrl = movie.a["href"]

    print("title: " + title)
    print("description: " + description)
    print("category: " + category)
    print("views: " + view)
    print("movieUrl: " + movieUrl)

    saveFile.write(title.replace(",", " ") + ", " + description.replace(",", " ") + ", " +
                   category.replace(",", " ") + ", " + view.replace(",", " ") + ", " + movieUrl.replace(",", " ") + "\n")

saveFile.close()
