OK_FORMAT = True

test = {   'name': 'q2.3.1',
    'points': 10,
    'suites': [   {   'cases': [   {   'code': '>>> grid = [[0, 0, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 0, 0, 0]]\n'
                                               '>>> start = (0, 0)\n'
                                               '>>> goal = (4, 4)\n'
                                               '>>> plan, visited = astar_231(grid, start, goal)\n'
                                               '>>> plan == [(0, 0), (1, 0), (2, 1), (2, 2), (3, 3), (4, 4)] and visited == [(0, 0), (1, 0), (2, 1), (2, 2), (3, 3), (4, 4)]\n'
                                               'True',
                                       'failure_message': 'The expected plan was [(0,0), (1,0), (2,1), (2,2), (3,3), (4,4)]',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> grid = [[0, 0, 1, 0, 0], [0, 1, 0, 0, 0], [0, 0, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 0, 0, 0]]\n'
                                               '>>> start = (0, 0)\n'
                                               '>>> goal = (4, 4)\n'
                                               '>>> plan, visited = dijkstra_231(grid, start, goal)\n'
                                               '>>> plan == [(0, 0), (0, 1), (1, 2), (2, 2), (3, 3), (4, 4)] and visited == [(0, 0), (1, 0), (0, 1), (2, 0), (1, 2), (2, 1), (1, 3), (3, 1), (2, 2), '
                                               '(0, 3), (1, 4), (4, 1), (4, 0), (2, 4), (3, 3), (4, 2), (0, 4), (3, 4), (4, 3), (4, 4)]\n'
                                               'True',
                                       'failure_message': 'The expected plan was [(0,0), (0,1), (1,2), (2,2), (3,3), (4,4)]',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
