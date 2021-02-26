from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

driver = webdriver.Firefox(executable_path=r'C:\Program Files (x86)\geckodriver.exe')
#tested on contests 1471, 1478, 1481
userval = input()
filename = userval[0: len(userval)-5]
con = userval[len(userval)-4:]
os.rename(os.path.basename(__file__), filename)
driver.get("https://codeforces.com/contest/" + con)
os.mkdir(con)
os.chdir(os.getcwd() + "/" +con)
path = os.getcwd()

rows = driver.find_elements_by_xpath("//table[@class='problems']/tbody/tr")
num = len(rows)
temp0 = driver.find_element_by_xpath("/html/body/div[6]/div[4]/div[2]/div[2]/div[6]/table/tbody/tr["+str(2)+"]/td[1]/a")
acode = ord(temp0.text)
for i in range(2 , num+1):
    name = chr(acode+i-2)
    #creating problem dir
    os.mkdir(name)
    #moving to problem dir
    os.chdir(os.getcwd()+"/" +name)

    temp1 = "//table[@class='problems']/tbody/tr["+ str(i) +"]/td[2]/div/div[1]/a"
    linktxt = driver.find_element_by_xpath(temp1)
    linktxt.click()
    pstmt = driver.find_element_by_class_name("problem-statement")
    pstmt.screenshot("problem.png")
    #finding no. of input-output examples
    dat = driver.find_elements_by_xpath("/html/body/div[6]/div[4]/div[2]/div[3]/div[2]/div/div[5]/div[2]/div[1]/pre")
    num1 = len(dat)
    #iterating over all examples
    for j in range(1, num1+1):
        inpt = driver.find_element_by_xpath("/html/body/div[6]/div[4]/div[2]/div[3]/div[2]/div/div[5]/div[2]/div[1]/pre["+str(j)+"]")
        f = open("input"+str(j)+".txt", "a")
        f.write(inpt.text)
        f.close()
        opt = driver.find_element_by_xpath("/html/body/div[6]/div[4]/div[2]/div[3]/div[2]/div/div[5]/div[2]/div[2]/pre["+str(j)+"]")
        t = open("output"+str(j)+".txt", "a")
        t.write(opt.text)
        t.close()

    #moving back in webdriver
    driver.back()
    #changing dir back to contest dir
    os.chdir(path)

print("Tasks done!")