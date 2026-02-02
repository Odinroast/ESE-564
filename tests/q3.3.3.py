OK_FORMAT = True

test = {   'name': 'q3.3.3',
    'points': 3,
    'suites': [   {   'cases': [   {'code': '>>> ans_333.shape == (7,)\nTrue', 'failure_message': 'ans_333 does not have the correct shape.', 'hidden': False, 'locked': False, 'points': 0},
                                   {   'code': '>>> np.isclose(np.sum(ans_333[3:] ** 2), 1.0, atol=0.001).item()\nTrue',
                                       'failure_message': 'mocap_quat is not a unit quaternion (q_0^2 q_1^2 + q_2^2 + q_3^2 = 1).',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
