import Game.health

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
