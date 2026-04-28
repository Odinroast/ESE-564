OK_FORMAT = True

test = {   'name': 'q2.3',
    'points': 15,
    'suites': [   {   'cases': [   {   'code': '>>> grid = [[0, 1, 1], [0, 1, 1], [0, 0, 0]]\n'
                                               '>>> start = (0, 0)\n'
                                               '>>> goal = (2, 2)\n'
                                               '>>> plan, visited = astar_grid_search_23(grid, start, goal, PriorityQueue_21(), eight_connected_cost_221, manhattan_heuristic_222)\n'
                                               '>>> plan == [(0, 0), (1, 0), (2, 1), (2, 2)] and visited == [(0, 0), (1, 0), (2, 1), (2, 2)]\n'
                                               'True',
                                       'failure_message': 'The expected plan was [(0,0), (1,0), (2,0), (2,1), (2,2)]',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
