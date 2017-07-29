import Game.engine
import Game.scene_director

Scene_instances = Game.scene_director.SceneDirector('welcome')

game = Game.engine.Engine(Scene_instances)

game.play()
