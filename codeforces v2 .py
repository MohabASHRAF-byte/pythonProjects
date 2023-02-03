import requests
import csv
from bs4 import BeautifulSoup
import subprocess


def DG(x):
    for xxx in x:
        print(xxx)


def DT(x):
    for xxx in x:
        print(xxx.get_text())


def DS(x):
    for xxx in x:
        print(xxx.get_text().strip())


def run():
    cpp_file = "test.cpp"
    input_file = "input.txt"
    output_file = "output.txt"

    result = subprocess.run(["g++", cpp_file, "-o", "program"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode == 0:
        with open(input_file, "r") as input_data, open(output_file, "w") as output_data:
            result = subprocess.run(["./program"], stdin=input_data, stdout=output_data, stderr=subprocess.PIPE)
            if result.returncode != 0:
                print("The C++ program returned an error:")
                print(result.stderr.decode())
    else:
        print("Error compiling the C++ program:")
        print(result.stderr.decode())


def read_output():
    temp = []
    with open("output.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            temp.append(line.strip())
    return temp


x = input("Enter the problem number\t")
ch = x[-1].upper()
num = int(x[:-1])
# ...............................................................
url = f"https://codeforces.com/contest/{num}/problem/{ch}"
# ................................................................
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
codeInput = soup.find_all("div", attrs={"class", "input"})
output = soup.find_all("div", attrs={"class", "output"})
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
inputs=[]
temp=[]
lines=0;
for i in range(len(codeInput)):
        ff =codeInput[i].find("pre")
        for i in range(0,1000):
            if not i&1:
                find=f"test-example-line test-example-line-even test-example-line-{i}"
            else :
                find=f"test-example-line test-example-line-odd test-example-line-{i}"
            fff =ff.find_all("div" ,attrs={"class" :find})
            if len(fff)==0:
                break
            ffff=[i.get_text().split() for i in fff]
            temp.append(ffff)
            lines+=1
        inputs.append(temp)
##################################################################################################
if lines==0:
    for i in range(len(codeInput)):
            ff =codeInput[i].find("pre")
            inputs.append(ff.get_text().strip().split("\n"))

cpp_file = "test.cpp"
input_file = "input.txt"
output_file = "output.txt"

result = subprocess.run(["g++", cpp_file, "-o", "program"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if result.returncode == 0:
    with open(input_file, "r") as input_data, open(output_file, "w") as output_data:
        result = subprocess.run(["./program"], stdin=input_data, stdout=output_data, stderr=subprocess.PIPE)
        if result.returncode != 0:
            print("The C++ program returned an error:")
            print(result.stderr.decode())
else:
    print("Error compiling the C++ program:")
    print(result.stderr.decode())
Program_output=[]
if not lines==0:
           for i in inputs:
                with open("input.txt", "w") as file:
                    for ii in i:
                        for iii in ii:
                            if len(iii) == 0:
                                continue
                            for iiii in iii:
                                file.write(str(iiii)+" ")
                            file.write("\n")
                    file.write(str(50 * '*'))
                run()
                Program_output.append(read_output())

else:
    for i in inputs:
        with open("input.txt", "w") as file:
                if len(i)==0:
                    continue
                for ii in i:
                    file.write(ii+"\n")
                file.write(50*'*'+"\n")
        run()
        Program_output.append(read_output())
flag = False
for t_result , t_scrapped in zip(Program_output,scrapped):
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
