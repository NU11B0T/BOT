from selenium import webdriver
import time

number = 5 #Number of times
start_time = time.clock()
url = 'https://_______.sarahah.com/'
mes ='YOUR MESSAGE'


def Nu11B0T(url,mes):
    chromedriver = webdriver.Firefox(executable_path='YOUR PATH FOR CHROME DRIVER')#Example :D:\firefoxdriver\geckodriver.exe
    chromedriver.get(url)
    time.sleep(2)
    message = chromedriver.find_element_by_xpath('//*[@id="Text"]')
    message.click()
    message.send_keys(mes)
    send = chromedriver.find_element_by_xpath('//*[@id="Send"]')
    send.click()
    time.sleep(5)
    chromedriver.quit()

for i in xrange(0,number):
    Nu11B0T(url,mes)

print time.clock() - start_time, "seconds"
