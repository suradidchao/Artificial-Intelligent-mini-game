#Resources in the map
TREE = 0
DIRT = 1
CAR = 2
STATION = 3
EXIT = 4
EMPTY = ''
#Important dimensions
TILESIZE = 50
MAPWIDTH = 18
MAPHEIGHT = 15


#Tile MAP
tilemap = [ [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY],
            [TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE],
            [TREE, DIRT, DIRT, DIRT, TREE, DIRT, DIRT, DIRT, TREE, DIRT, DIRT, DIRT, TREE, DIRT, DIRT, DIRT, TREE, EXIT],
            [TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT],
            [TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT],
            [TREE, DIRT, TREE, DIRT, STATION, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT],
            [TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, STATION, DIRT, TREE, DIRT],
            [TREE, DIRT, DIRT, DIRT, TREE, DIRT, DIRT, DIRT, TREE, DIRT, DIRT, DIRT, TREE, DIRT, DIRT, DIRT, TREE, DIRT],
            [TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT],
            [TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, STATION, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT],
            [TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT],
            [TREE, DIRT, TREE, DIRT, TREE, DIRT, DIRT, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT],
            [TREE, DIRT, STATION, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT, TREE, DIRT],
            [TREE, DIRT, TREE, DIRT, DIRT, DIRT, TREE, DIRT, DIRT, DIRT, TREE, DIRT, DIRT, DIRT, TREE, DIRT, DIRT , DIRT],
            [CAR, DIRT, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE, TREE] ]