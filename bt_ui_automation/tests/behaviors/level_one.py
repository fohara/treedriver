import py_trees

from bt_ui_automation.tests.page_objects.pages import Pages

IMPLICIT_WAIT = 5

class SelectLevelOne(py_trees.behaviour.Behaviour):

    def __init__(self, name="SelectLevelOne"):
        super(SelectLevelOne, self).__init__(name)
        self.blackboard = py_trees.blackboard.Blackboard()

    def update(self):
        pages = Pages(self.blackboard.get('driver'))
        try:
            pages.home.select_level('one')
        except Exception as e:
            self.logger.info("Failed to select level one:\n{}".format(e))
            return py_trees.common.Status.FAILURE
        return py_trees.common.Status.SUCCESS