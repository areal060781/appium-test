class Login:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = driver.find_element_by_id('username')
        self.password_input = driver.find_element_by_id('password')
        self.login_button = driver.find_element_by_id('login')

    def login(self, username, password):
        self.username_input.send_keys(username)
        self.password_input.send_keys(password)
        self.login_button.click()

    def validate_button_disabled_when_bad_password(self):
        assert self.login_button.is_enabled() == False
