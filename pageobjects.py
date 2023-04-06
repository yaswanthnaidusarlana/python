from selenium.webdriver.common.by import By
class loginpage:
    myaccountlink="my Account"
    loginlink="login"
    emailid="input-email"
    password="input-password"
    submitb0utton="//button[@type='submit']"
    def __init(self,driver);
        self.driver=driver
    def clickonmyaccountlink(self):
        self.driver.find_element(By.LINK_TEXT,self.myaccountlink_).click()
    def clickonloginlink(self):
        self.driver.find_element(By.LINK_TEXT, self.loginlink).click()
    def enteremail(self,username)
        self.driver.find_element(By.ID, self.emailid).send_keys(username)
    def enterpassword(self, password)
        self.driver.find_element(By.ID, self.password).send_keys(password)
    def clickonsubmit(self)
        self.driver.find_element(By.XPATH, self.submitbutton_).click()
