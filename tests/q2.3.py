OK_FORMAT = True

test = {   'name': 'q2.3',
    'points': 25,
    'suites': [   {   'cases': [   {   'code': ">>> trained_policy = torch.load('trained_pusher_policy.pt', map_location='cpu')\n"
                                               ">>> hid_size = trained_policy['hid_size']\n"
                                               ">>> num_layers = trained_policy['num_layers']\n"
                                               '>>> net = FCNN_11(23, 7, hid_size, num_layers)\n'
                                               ">>> _ = net.load_state_dict(trained_policy['net'])\n"
                                               ">>> net = net.eval().to('cpu')\n"
                                               ">>> env = gymnasium.make('Pusher-v5')\n"
                                               ">>> X_normalizer = Normalizer_12(torch.zeros((2, trained_policy['X_mean'].shape[0])))\n"
                                               ">>> X_normalizer.mean = trained_policy['X_mean']\n"
                                               ">>> X_normalizer.std = trained_policy['X_std']\n"
                                               ">>> Y_normalizer = Normalizer_12(torch.zeros((2, trained_policy['Y_mean'].shape[0])))\n"
                                               ">>> Y_normalizer.mean = trained_policy['Y_mean']\n"
                                               ">>> Y_normalizer.std = trained_policy['Y_std']\n"
                                               '>>> reward = run_policy_22(net, env, X_normalizer, Y_normalizer, seed=0)\n'
                                               '>>> np.issubdtype(type(reward), np.floating) or np.issubdtype(type(reward), np.integer)\n'
                                               'True',
                                       'failure_message': 'Cannot load your trained policy and run it.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
