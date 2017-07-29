from nose.tools import *
import Game.engine
import Game.health
import Game.inventory
import Game.scene_director
import Game.scenes

def setup():
    print("SETUP!")

def teardown():
    print("TEAR DOWN!")

def test_basic():
    print("I RAN!", end='')
