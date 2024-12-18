from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    WebDriverWait(browser, 15).until(EC. text_to_be_present_in_element((By.ID, "price"),"$100"))

        
    button=browser.find_element(By.CSS_SELECTOR, "#book")
    button.click()
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text
    y = calc(x)
    
    
    ans = browser.find_element(By.CSS_SELECTOR, "#answer")
    ans.send_keys(y)

    
    ans3 = browser.find_element(By.CSS_SELECTOR, "#solve")
    ans3.click()
    
    
    

   
    

    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла