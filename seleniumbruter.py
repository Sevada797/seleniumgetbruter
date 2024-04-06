from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time
import os
import sys


pwd = os.getcwd()
options = webdriver.ChromeOptions()

chrome_binary_path = pwd+"/chrome_binaries/chrome-linux64/chrome"
options.binary_location = chrome_binary_path  # Set the custom Chrome binary path


service = Service(executable_path=pwd+"/chrome_binaries/chromedriver-linux64/chromedriver")





os.system("clear")
print("NOTE: Edit source code for changing wordlist (don't want too much inputs here))\ndefault is wlist.txt\n")
print("Started ultimate get parameter bruter by Eth3rnal_AKA_Sevada <3\n")
url=input("Enter url: ")
print("NOTE: for multiple cookies you are gonnna use manual input from console,\ntype 1 for setting multiple cookies, and leave blank for not setting any")
cookie=input("Enter cookie (like you would in JS ex. a=b; expires=Never...): ")
rcount=int(input("Enter how many reflections should be ignored: "))
value=input("Enter value for parameter(leave blank for default, default is-NoWayThisCouldBeInHTML64f27e18356fa): ")
querySign=input("Choose eighter ? or & (if there is ? in url choose &, default is ?): ")
if (value==""):
    value="NoWayThisCouldBeInHTML64f27e18356fa"
if (querySign==""):
    querySign="?"



driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 5)
#driver.set_page_load_timeout(7)


onlyUrl=url[0 : url.find("/")+2+( (url[url.find("/")+1:])[(url[url.find("/")+1:]).find("/")+1:] ).find("/")]

if (cookie!="" and cookie!="1"):
    driver.get(onlyUrl)
    driver.execute_script("document.body.innerHTML=\"<h1 style=\\\"font-size: 38px\\\">Setting up cookies, you will be redirected now</h1>\"; document.cookie='{}'; ".format(cookie))
    time.sleep(2)
elif cookie=="1":
    driver.get(onlyUrl)
    driver.execute_script("window.a=\"\";window.Continue=()=>{window.a=\"continue\";}")
    driver.execute_script("document.body.innerHTML='<h1 style=\"font-size: 38px;\">Please insert cookies manually from console, <br>When finished run \"Continue()\" or \"window.Continue()\" in console<br>Warning don\\'t change location of current page, if you need to set cookie for other path use JS cookie\\'s path= attribute or open new tab and do whatever you need </h1>'")
    while not (driver.execute_script("return window.a==\"continue\"")):
        continue
    driver.execute_script("console.log('Continuing script master')")
else:
    driver.execute_script("document.body.innerHTML='<h1 style=\"font-size: 38px;\">Starting the script</h1>'")
    time.sleep(2)





with open("wlist.txt", "r") as file:
    for line in file:
        print("testing url: "+url+querySign+"{}={}".format(line.strip(), value))
        driver.get(url+querySign+"{}={}".format(line.strip(), value))
        while driver.execute_script("/*document.readyState !== 'interactive' ||*/ document.readyState !== 'complete'/*uncommnet all for fast mode, but minus is XSS check not on full page load*/"):
            continue
        html=driver.execute_script('return document.documentElement.outerHTML')

        def findReflections(n, rcount, value, html):
            if (n==0):
                splited_html=html
            else:
                splited_html=html[int(html.find(value)+len(value)):]
            if(n==rcount):
                return splited_html.find(value)!=-1
            else:
                n=n+1
                return findReflections(n, rcount, value, splited_html)
        if findReflections(0, rcount, value, html):
            print("\nFound reflections for parameter - {}".format(line.strip()))
            f=open("getfound.txt", "a")
            f.write("{}".format(line.strip())+"\n")
            f.close()

