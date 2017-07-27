import engine
import scene_director

Scene_instances = scene_director.SceneDirector('welcome')

game = engine.Engine(Scene_instances)

game.play()
