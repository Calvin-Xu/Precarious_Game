import Game.scene_director
import Game.scenes

def test_opening_scene():
    scene = Game.scene_director.SceneDirector('welcome')
    scene_instance = scene.opening_scene()
    assert isinstance(scene_instance, type(Game.scenes.Welcome()))

def test_next_scene():
    scene = Game.scene_director.SceneDirector('welcome')
    scene_instance = scene.next_scene('boss')
    assert isinstance(scene_instance, type(Game.scenes.Boss()))
