from selenium import webdriver
from bs4 import BeautifulSoup


brower = webdriver.Chrome('./chromedriver.exe')
url = 'https://www.instagram.com/explore/tags/%EC%9D%B8%EC%83%9D%EB%84%A4%EC%BB%B7%ED%8F%AC%EC%A6%88/'
brower.get(url)

html = brower.page_source

soup = BeautifulSoup(html, 'html.parser')
post = soup.select('div._aagv > img')[0]['src']
print(post)

