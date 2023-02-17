from selenium.webdriver.common.by import By


class LoginPage:
    user_name_text_box_id = "user-name"
    password_text_box_id = "password"
    login_button_text_name = "login-button"
    button_options_text_id = "react-burger-menu-btn"
    logout_option_text_name = "login-button"


    def __init__(self,driver):
        self.driver = driver


    def setUserName(self,username):
        self.driver.find_element(By.ID,self.user_name_text_box_id).clear()
        self.driver.find_element(By.ID,self.user_name_text_box_id).send_keys(username)


    def setPassword(self,password):
        self.driver.find_element(By.ID,self.password_text_box_id).clear()
        self.driver.find_element(By.ID,self.password_text_box_id).send_keys(password)


    def clickLogin(self):
        self.driver.find_element(By.NAME,self.login_button_text_name).click()






