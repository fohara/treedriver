from selenium.common.exceptions import NoSuchElementException


class Base:

    def __init__(self, driver):
        self.driver = driver

    def has_success_message(self):
        try:
            self.driver.find_element_by_css_selector('article.message.is-success')
            return True
        except NoSuchElementException as e:
            return False
