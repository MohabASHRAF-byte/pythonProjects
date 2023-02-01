
import requests as req
import csv
from bs4 import BeautifulSoup
def DG(x):
    for xxx in x:
        print(xxx)
def DT(x):
    for xxx in x:
        print(xxx.get_text())
def DS(x):
    for xxx in x:
        print(xxx.get_text().strip())

data=[]
dataset=[]
page_number=1
check=False
while True :
    url=f"https://diwanegypt.com/product-category/books/arabic-books/page/{page_number}/"
    response =req.get(url)
    soup = BeautifulSoup(response.text,"html.parser")
    books =soup.find("ul",attrs = {"class":"products columns-5"})
    try:
        book = books.find_all("li")
    except :
        print(page_number)
        check =True
    if check :
        break
    for i in range(len(book)):
        temp=[]
        title = book[i].find('h2').get_text()
        price = book[i].find('bdi').get_text()[3:]
        author =book[i].find('span' , attrs={"class":"author"}).get_text()
        img= book[i].find('img')['src']
        temp.append(title)
        temp.append(author)
        temp.append(price)
        temp.append(img)
        data.append(temp)
    page_number+=1
    print(page_number)
    for i in data:
        dataset.append(i)


with open(f"Books3.csv" ,'w',newline="",encoding='UTF-8') as wr:
    writer =csv.writer(wr)
    header=["Title" ,"Author","Price","Image"]
    writer.writerow(header)
    writer.writerows(dataset)






