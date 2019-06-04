import py_trees

from bt_ui_automation.tests.page_objects.pages import Pages

class SelectLevelTwo(py_trees.behaviour.Behaviour):

    def __init__(self, name="SelectLevelTwo"):
        super(SelectLevelTwo, self).__init__(name)
        self.blackboard = py_trees.blackboard.Blackboard()

    def update(self):
        pages = Pages(self.blackboard.get('driver'))
        try:
            pages.home.select_level('two')
        except Exception as e:
            self.logger.info("Failed to select level two:\n{}".format(e))
            return py_trees.common.Status.FAILURE
        return py_trees.common.Status.SUCCESS


class ClickForVictory(py_trees.behaviour.Behaviour):

    def __init__(self, name="ClickForVictory"):
        super(ClickForVictory, self).__init__(name)
        self.blackboard = py_trees.blackboard.Blackboard()

    def update(self):
        pages = Pages(self.blackboard.get('driver'))
        try:
            pages.level_two.click_for_victory()
            self.logger.info('Clicked for victory!')
        except Exception as e:
            self.logger.info("Failed to click for victory:\n{}".format(e))
            return py_trees.common.Status.FAILURE
        return py_trees.common.Status.SUCCESS