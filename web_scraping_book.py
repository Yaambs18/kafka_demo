import requests
import bs4

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'
# res = requests.get(base_url.format(1))

# soup = bs4.BeautifulSoup(res.text,'lxml')

# products = soup.select('.product_pod')

# example = products[0]

# print(example.select('.star-rating.Three'))

# print([]==example.select('.star-rating.Two'))

# print(example.select('a')[1]['title'])

tw_star_rating = []
for i in range(1,5):
    scrape_url = base_url.format(i)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select('.product_pod')
    for book in books:
        if book.select('.star-rating.Two')!=0:
            book_title = book.select('a')[1]['title']
            tw_star_rating.append(book_title)
# print(tw_star_rating)

