import Game.engine
import Game.health
import Game.inventory
import Game.scene_director
import Game.scenes

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

def test_hpplus():
    val = Game.health.Health.hp
    assert val == 6
    Game.health.player.hpplus(1)
    val = Game.health.Health.hp
    assert val == 7

def test_hpminus():
    val = Game.health.Health.hp
    assert val == 7
    Game.health.player.hpminus(2)
    val = Game.health.Health.hp
    assert val == 5

def test_opening_scene():
    scene = Game.scene_director.SceneDirector('welcome')
    scene_instance = scene.opening_scene()
    assert isinstance(scene_instance, type(Game.scenes.Welcome()))

def test_next_scene():
    scene = Game.scene_director.SceneDirector('welcome')
    scene_instance = scene.next_scene('boss')
    assert isinstance(scene_instance, type(Game.scenes.Boss()))
