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
    driver.get("https://titan22.com/account/login?return_url=%2Faccount")
    return driver

#extract only the temp value
def clean_text(text):
  output=float(text.split(": ")[1])
  return output

#get the script temp of h2
def main():
    driver = get_driver()
    time.sleep(2)
    element = driver.find_element(by="id",
                                  value="CustomerEmail").send_keys("jg@hotmail.com")
    element=driver.find_element(by='id', value="CustomerPassword").send_keys("password")
    element = driver.find_element(by="xpath", value="/html/body/footer/div/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a").click()
    element=driver.find_element(by='id', value="ContactFormEmail").send_keys("jg@hotmail.com")
    element=driver.find_element(by='id', value="ContactFormFirstName").send_keys("j")
    
print(main())
