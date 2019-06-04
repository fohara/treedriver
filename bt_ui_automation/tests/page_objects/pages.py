from bt_ui_automation.tests.page_objects.home import Home
from bt_ui_automation.tests.page_objects.level_one import LevelOne
from bt_ui_automation.tests.page_objects.level_two import LevelTwo
from bt_ui_automation.tests.page_objects.level_three import LevelThree

class Pages:

    def __init__(self, driver):
        self.home = Home(driver)
        self.level_one = LevelOne(driver)
        self.level_two = LevelTwo(driver)
        self.level_three = LevelThree(driver)
