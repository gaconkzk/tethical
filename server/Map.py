from panda3d.core import loadPrcFile
loadPrcFile("Config.prc")
from panda3d.core import *
import json

GAME = ConfigVariableString('game', 'fft').getValue()

def load(name):
    f = open(GAME+'/maps/'+name+'.json', 'r')
    m = json.loads(f.read())
    f.close()

    tiles = [ [ [ None for z in range(m['z']) ] for y in range(m['y']) ] for x in range(m['x']) ]
    for t in m['tiles']:
        tiles[int(t['x'])][int(t['y'])][int(t['z'])] = t

    m['tiles'] = tiles

    return m
