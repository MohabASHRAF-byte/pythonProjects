import requests
from bs4 import BeautifulSoup
from subprocess import Popen, PIPE
import subprocess
# takes one parameter first the scrapped input list
def Get_input(codeInput):
    Test_Cases = []
    flag = True
    for test in range(len(codeInput)):
        Get_Test = codeInput[test].find("pre")
        Full_TestCase = []
        for i in range(len(Get_Test)):
            if not (i & 1):
                find = f"test-example-line test-example-line-even test-example-line-{i}"
            else:
                find = f"test-example-line test-example-line-odd test-example-line-{i}"
            lines = Get_Test.find_all("div", attrs={"class": find})
            if len(lines) == 0:
                break
            flag = False
            for line in lines:
                Full_TestCase.append(line.get_text().strip())
        if len(Full_TestCase) == 0:
            break
        Test_Cases.append(Full_TestCase)
    #################
    if flag:
        for i in range(len(codeInput)):
            ff = codeInput[i].find_all("pre")
            for ii in ff:
                cleaned = ii.get_text().strip().split("\n")
                Test_Cases.append(cleaned)
    return Test_Cases
###
def Run_program(Input_Test):
    result = subprocess.run(["g++", "-std=c++20", "test.cpp", "-o", "program"], stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    p = Popen(["program"], stdout=PIPE, stdin=PIPE)
    for line in Input_Test:
        for item in line.split(" "):
            p.stdin.write(item.encode())
            p.stdin.write("\n".encode())
    p.stdin.flush()
    res = p.stdout.readlines()
    program_outputt=[]
    for i in res :
        program_outputt.append(i.decode().strip())
    return program_outputt
###
def Get_Output():
    print("here")
# main
ch = 'd'
num = 1790
# ...............................................................
url = f"https://codeforces.com/contest/{num}/problem/{ch}"
# ................................................................
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
ScrappedInput = soup.find_all("div", attrs={"class", "input"})
output = soup.find_all("div", attrs={"class", "output"})
##
CodeForcesTests = Get_input(ScrappedInput)

program_output=[]

for Test in CodeForcesTests:
    program_output.append(Run_program(Test))
print(program_output)
