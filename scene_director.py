import scenes

class SceneDirector(object):

    scene_match = {
        'welcome': scenes.Welcome(),
        'dungeon_ent': scenes.DungeonEntrance(),
        'hallway': scenes.Hallway(),
        'room1': scenes.Room1(),
        'room2': scenes.Room2(),
        'room3': scenes.Room3(),
        'trap_hallway': scenes.TrapHallway(),
        'combat_room': scenes.CombatRoom(),
        'boss': scenes.Boss(),
        'death': scenes.Death(),
        'win': scenes.Win()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        scene_instance = SceneDirector.scene_match.get(scene_name)
        return scene_instance

    def opening_scene(self):
        return self.next_scene(self.start_scene)
