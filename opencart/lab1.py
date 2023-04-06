import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://demo.opencart.com/")
driver.find_element(By.LINK_TEXT,"My Account").click()
driver.find_element(By.LINK_TEXT,"Register").click()
time.sleep(5)
print(driver.title)

driver.find_element(By.ID,"input-firstname").send_keys("yash")
driver.find_element(By.ID,"input-firstname").send_keys("s")
driver.find_element(By.ID,"input-email").send_keys("yash@gmail.com")
driver.find_element(By.ID,"input-password").send_keys("apple")
driver.find_element(By.ID,"input-newsletter-yes").click()
driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
driver.find_element(By.XPATH,"//button[@type='submit']").click()
