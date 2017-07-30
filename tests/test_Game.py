import Game.engine
import Game.health
import Game.inventory
import Game.scene_director
import Game.scenes

def test__add_item():
    val = Game.inventory.Inventory.gear
    Game.inventory.backpack.add_item("test1","test2")
    assert val == ["test1","test2"]

def test__remove_item():
    val = Game.inventory.Inventory.gear
    Game.inventory.backpack.remove_item("test1")
    assert val == ["test2"]
