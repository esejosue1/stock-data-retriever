from selenium import webdriver
import time

#set options to make browsing easier
def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")  #access max version of browser
    options.add_argument("disable-dev-shm-usage")  #avoid issues in lenux
    options.add_argument("no-sandbox")  #access prviligaes
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com")
    return driver


def main():
    driver = get_driver()
    time.sleep(2)
    element = driver.find_element(by="xpath",
                                  value="/html/body/div[1]/div/h1[2]")
    return element.text


print(main())
