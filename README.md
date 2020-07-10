# Behavior Trees to Simulate User Interaction

## Concept
Creating a UI test automation agent can roughly be likened to creating an [NPC](https://en.wikipedia.org/wiki/Non-player_character) for the app under test. Since [behavior trees](https://en.wikipedia.org/wiki/Behavior_tree_(artificial_intelligence,_robotics_and_control)) are a powerful and flexible way to model NPCs, why not use them to model UI automation tests?

## Note
This is an early proof of concept; all code is provisional.

## Dependencies
* Install pip dependencies: `pip install -r requirements.txt`
* Firefox (used by Selenium)

## Usage
* Start the small app-under-test server process
* Run the tests via `py.test`

**Caution:** The server process will intentionally kill any Firefox processes to demonstrate the fault tolerance of the behavior tree tests. Be careful if Firefox is your default browser otherwise you might lose work!

## Illustration
Here's an example of a behavior tree test:

```python
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
```

Here's the corresponding diagram generated from the `diagram_tree(tree)` call:

![Behavior tree diagram](images/level_three.png?raw=true)

## Todo
- [ ] Better explanation of concept
- [ ] Better explanation of implementation and test cases
- [ ] Provide containerized execution environment
- [ ] Experiment with asyncio implementation?