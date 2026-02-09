OK_FORMAT = True

test = {   'name': 'q2.2.4',
    'points': 10,
    'suites': [   {   'cases': [   {   'code': '>>> ik = IK_224(l1=1, x=1.5, y=1.5, theta=np.pi / 6)\n>>> type(ik) is list and type(ik[0]) is tuple and (len(ik[0]) == 3)\nTrue',
                                       'failure_message': 'Did not return a list of 3-tuples',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> l1 = 4.43\n'
                                               '>>> x = 10 - 5.57\n'
                                               '>>> y = 8.66\n'
                                               '>>> theta1 = np.pi / 2\n'
                                               '>>> ik1 = IK_224(l1, x, y, theta1)\n'
                                               '>>> theta2 = -np.pi / 2\n'
                                               '>>> ik2 = IK_224(l1, x, -y, theta2)\n'
                                               '>>> (len(ik1) == 1 or (not np.isclose(ik1[0][0], ik1[1][0]) or not np.isclose(ik1[0][1], ik1[1][1]) or (not np.isclose(ik1[0][2], ik1[1][2])))) and '
                                               '(len(ik2) == 1 or (not np.isclose(ik2[0][0], ik2[1][0]) or not np.isclose(ik2[0][1], ik2[1][1]) or (not np.isclose(ik2[0][2], ik2[1][2]))))\n'
                                               'True',
                                       'failure_message': 'Returned multiple equivalent solutions',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> l1 = 4.43\n'
                                               '>>> x = 10 - 5.57\n'
                                               '>>> y = 8.66\n'
                                               '>>> theta1 = np.pi / 2\n'
                                               '>>> ik1 = IK_224(l1, x, y, theta1)\n'
                                               '>>> theta2 = -np.pi / 2\n'
                                               '>>> ik2 = IK_224(l1, x, -y, theta2)\n'
                                               '>>> (len(ik1) == 1 or (0 <= ik1[0][1] <= 2 * np.pi and 0 <= ik1[0][2] <= 2 * np.pi and (0 <= ik1[1][1] <= 2 * np.pi) and (0 <= ik1[1][2] <= 2 * '
                                               'np.pi))) and (len(ik2) == 1 or (0 <= ik2[0][1] <= 2 * np.pi and 0 <= ik2[0][2] <= 2 * np.pi and (0 <= ik2[1][1] <= 2 * np.pi) and (0 <= ik2[1][2] <= 2 '
                                               '* np.pi)))\n'
                                               'True',
                                       'failure_message': 'Returned solutions with angles outside of [0, 2pi]',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> l1 = 4.43\n'
                                               '>>> x = 0\n'
                                               '>>> y = 0\n'
                                               '>>> theta = np.pi / 3\n'
                                               '>>> ik = IK_224(l1, x, y, theta)\n'
                                               '>>> np.array(len(ik) == 1 and ik[0][2] >= 0 or (ik[0][2] >= 0 and ik[1][2] >= 0)).item()\n'
                                               'True',
                                       'failure_message': 'Returned solutions with negative d',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
