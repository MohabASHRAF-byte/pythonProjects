import requests as req
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
#################################################################
x=input("Enter the problem number\t")
ch = x[-1].upper()
num =int(x[:-1])
##################################################################
url=f"https://codeforces.com/contest/{num}/problem/{ch}"
##################################################################
response =req.get(url)
soup = BeautifulSoup(response.text,"html.parser")
output = soup.find_all("div" ,attrs ={"class","output"})
##################################################################
test=[]
scrapped = []
temp = []
for i in range(len(output)):
    new = output[i].get_text()[6:].strip().split("\n")
    for ii in new:
        temp.append(ii)
    tp=[i.strip() for i in temp]
    scrapped.append(tp)
    temp = []
    tp=[]
##################################################################
test = []
result = []
cnt = len(scrapped)
for i in range(cnt):
    print(f"Enter test {i+1}\n")
    while True:
        x = input()
        if x in (100 * '#') and len(x) > 3:
            break
        test.append(x)
    check = [i.strip() for i in test]
    result.append(check)
    test = []
############################################################################
flag = False

for t_result , t_scrapped in zip(result,scrapped):
    if not(len(t_result)==len(t_scrapped)):
        flag =True
        break
    for i , j in zip(t_result,t_scrapped):
             if not(len(i)==len(j)):
                    flag =True
                    break
             for ii , jj in zip(i,j):
                if  not jj == ii :
                    flag= True
print("ro7 submit yalla !!!!")if not flag else print("fakr tani")
