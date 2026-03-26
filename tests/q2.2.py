OK_FORMAT = True

test = {   'name': 'q2.2',
    'points': 20,
    'suites': [   {   'cases': [   {   'code': '>>> net = FCNN_11(23, 7, 32, 2)\n'
                                               ">>> env = gymnasium.make('Pusher-v5')\n"
                                               '>>> X_normalizer = Normalizer_12(X)\n'
                                               '>>> Y_normalizer = Normalizer_12(Y)\n'
                                               '>>> rewards = run_policy_22(net, env, X_normalizer, Y_normalizer, seed=0)\n'
                                               '>>> np.issubdtype(type(rewards), np.floating) or np.issubdtype(type(rewards), np.integer)\n'
                                               'True',
                                       'failure_message': 'Does not return a scalar reward.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
