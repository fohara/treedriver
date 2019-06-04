import py_trees
from py_trees.common import Status

from bt_ui_automation.tests.util import run_tree, diagram_tree
from bt_ui_automation.tests.behaviors.common import Driver, CloseDriver, NavigateToHome, CheckForSuccess
from bt_ui_automation.tests.behaviors.level_one import SelectLevelOne
from bt_ui_automation.tests.behaviors.level_two import SelectLevelTwo, ClickForVictory
from bt_ui_automation.tests.behaviors.level_three import SelectLevelThree, DestroyDarkPatterns, DismissModal


def test_level_one():
    tree = py_trees.composites.Sequence("Level One")
    tree.add_children([
        Driver(),
        NavigateToHome(),
        SelectLevelOne(),
        CheckForSuccess(),
        CloseDriver()])
    tree.setup_with_descendants()
    run_tree(tree)

    assert tree.status == Status.SUCCESS
    diagram_tree(tree)


def test_level_two():
    tree = py_trees.composites.Sequence("Level Two")
    sub_tree = py_trees.composites.Sequence("Victory Click")
    sub_tree.add_children([ClickForVictory(), CheckForSuccess()])
    victory_click = py_trees.decorators.Condition(child=sub_tree)

    tree.add_children([
        Driver(),
        NavigateToHome(),
        SelectLevelTwo(),
        victory_click,
        CloseDriver()])
    tree.setup_with_descendants()
    run_tree(tree)

    assert tree.status == Status.SUCCESS
    diagram_tree(tree)


def test_level_three():
    tree = py_trees.composites.Sequence("Level Three")
    sub_tree = py_trees.composites.Selector("Destroy Dark Patterns")
    dismiss_modal_if_any = py_trees.decorators.Inverter(child=DismissModal())
    sub_tree.add_children([DestroyDarkPatterns(), dismiss_modal_if_any])
    destroy_darkness = py_trees.decorators.Condition(child=sub_tree)

    tree.add_children([
        Driver(),
        NavigateToHome(),
        SelectLevelThree(),
        destroy_darkness,
        CloseDriver()])
    tree.setup_with_descendants()
    run_tree(tree)

    assert tree.status == Status.SUCCESS
    diagram_tree(tree)
