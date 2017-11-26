# VERTICES = [
#     [-100, -100, -100],
#     [-100, 100, -100],
#     [-100, -100, 100],
#     [-100, 100, 100],
#     [100, -100, -100],
#     [100, 100, -100],
#     [100, -100, 100],
#     [100, 100, 100]
# ]

# EDGES =  [
#     [0, 1, 2, 4],
#     [3, 1, 2, 7],
#     [5, 1, 4, 7],
#     [6, 2, 4, 7]
# ]

# FACES = [
#     [1, 3, 7, 5, 1],
#     [0, 2, 6, 4, 0],
#     [2, 3, 1, 0, 2],
#     [3, 2, 6, 7, 3],
#     [7, 6, 4, 5, 7],
#     [5, 4, 0, 1, 5]
# ]
VERTICES = [
    [-125, -50, -100],
    [-125, 0, -100],
    [-75, 0, -100],
    [-75, 50, -100],
    [-25, 100, -100],
    [-25, 150, -100],
    [25, 150, -100],
    [25, 100, -100],
    [75, 50, -100],
    [75, 0, -100],
    [125, 0, -100],
    [125, -50, -100],
    [75, -50, -100],
    [25, -100, -100],
    [25, -150, -100],
    [-25, -150, -100],
    [-25, -100, -100],
    [-75, -50, -100],
    [-125, -50, 100],
    [-125, 0, 100],
    [-75, 0, 100],
    [-75, 50, 100],
    [-25, 100, 100],
    [-25, 150, 100],
    [25, 150, 100],
    [25, 100, 100],
    [75, 50, 100],
    [75, 0, 100],
    [125, 0, 100],
    [125, -50, 100],
    [75, -50, 100],
    [25, -100, 100],
    [25, -150, 100],
    [-25, -150, 100],
    [-25, -100, 100],
    [-75, -50, 100]
]

FACES = [
    [36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19],
    [1, 19, 20, 2],
    [2, 20, 21, 3],
    [3, 21, 22, 4],
    [4, 22, 23, 5],
    [5, 23, 24, 6],
    [6, 24, 25, 7],
    [7, 25, 26, 8],
    [8, 26, 27, 9],
    [9, 27, 28, 10],
    [10, 28, 29, 11],
    [11, 29, 30, 12],
    [12, 30, 31, 13],
    [13, 31, 32, 14],
    [16, 34, 35, 17],
    [18, 36, 19, 1],
    [17, 35, 36, 18],
    [14, 32, 33, 15],
    [15, 33, 34, 16],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
]

class GeometryStructure():

    def __init__(self):
        self.vertices = VERTICES
        # self.edges = EDGES
        self.faces = FACES