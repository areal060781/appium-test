class Main:
    def __init__(self, driver):
        self.driver = driver
        self.welcome_message = driver.find_element_by_id('textview_first')

    def validate_welcome_message(self, username):
        assert self.welcome_message.text == 'Hello ' + username
