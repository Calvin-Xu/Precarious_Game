import Game.scenes

class SceneDirector(object):

    scene_match = {
        'welcome': Game.scenes.Welcome(),
        'dungeon_ent': Game.scenes.DungeonEntrance(),
        'hallway': Game.scenes.Hallway(),
        'room1': Game.scenes.Room1(),
        'room2': Game.scenes.Room2(),
        'room3': Game.scenes.Room3(),
        'trap_hallway': Game.scenes.TrapHallway(),
        'combat_room': Game.scenes.CombatRoom(),
        'boss': Game.scenes.Boss(),
        'death': Game.scenes.Death(),
        'win': Game.scenes.Win()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        scene_instance = SceneDirector.scene_match.get(scene_name)
        return scene_instance

    def opening_scene(self):
        return self.next_scene(self.start_scene)
