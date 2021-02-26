from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)


username = input("Enter username: ")
passwd = input("Enter password: ")

driver.get("https://moodle.iitd.ac.in/login/index.php")
print(driver.title)

uname = driver.find_element_by_id("username")
uname.send_keys(username)
pwd = driver.find_element_by_id("password")
pwd.send_keys(passwd)
captcha = driver.find_element_by_id("valuepkg3")
a1 = driver.find_element_by_id("login")
a2 = a1.text
ref = a2[a2.find('b')+20 : a2.find('F')-3]
for x in ref:
    if(x.isdigit()):
        pos = ref.find(x)
        break
num = ref[pos:]
n1 = int(num[:num.find(' ')])
n2 = int(num[num.find(' ')+3:])
if (ref.find('add')!=-1):
    captcha.send_keys(n1 + n2)
if (ref.find('subtract')!=-1):
    captcha.send_keys(n1 - n2)
if (ref.find('first')!=-1):
    captcha.send_keys(n1)
if (ref.find('second')!=-1) :
    captcha.send_keys(n2)

button = driver.find_element_by_id("loginbtn")
button.click()
#command to leave the window to user
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)