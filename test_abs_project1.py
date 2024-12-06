import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
link = "https://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)
input1 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your name"]')
input1.send_keys("Ivan")
input2 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]')
input2.send_keys("Petrov")
input3 = browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]')
input3.send_keys("qqq@qq.com")
time.sleep(20)
button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
time.sleep(10)
welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
welcome_text = welcome_text_elt.text

class TestAbs(unittest.TestCase):
    
    def test_abs1(self,welcome_text):
   
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Should be absolute value of a number")
        
    
        
if __name__ == "__main__":
    unittest.main()