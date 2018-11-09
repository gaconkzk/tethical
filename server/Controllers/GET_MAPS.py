from panda3d.core import loadPrcFile
loadPrcFile("Config.prc")
from panda3d.core import ConfigVariableString
import os
import Map
GAME = ConfigVariableString('game', 'fft').getValue()

# Return map list to a client
def execute(server, iterator, source):
    server.playersinlobby.remove(source)

    mapnames = [m.split('.')[0] for m in os.listdir(GAME+'/maps')]

    maps = []
    for mapname in mapnames:
        mp = Map.load(mapname)
        del mp['tiles']
        maps.append(mp)

    server.send.MAP_LIST(maps, source)