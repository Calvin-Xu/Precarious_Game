import Game.inventory

def test_add_item():
    val = Game.inventory.Inventory.gear
    assert val == []
    Game.inventory.backpack.add_item("test1","test2")
    assert val == ["test1","test2"]

def test_remove_item():
    val = Game.inventory.Inventory.gear
    assert val == ["test1","test2"]
    Game.inventory.backpack.remove_item("test1")
    assert val == ["test2"]
