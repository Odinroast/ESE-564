OK_FORMAT = True

test = {   'name': 'q1.1',
    'points': 15,
    'suites': [   {   'cases': [   {   'code': '>>> net = FCNN_11(10, 3, 32, 2)\n'
                                               '>>> num_layers = 0\n'
                                               '>>> for layer in net.modules():\n'
                                               '...     if isinstance(layer, nn.Linear):\n'
                                               '...         num_layers += 1\n'
                                               '>>> num_layers == 3\n'
                                               'True',
                                       'failure_message': 'The number of linear layers in your network is incorrect.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> num_params = sum((p.numel() for p in net.parameters()))\n>>> num_params == 10 * 32 + 32 * 32 + 32 * 3 + 2 * 32 + 3\nTrue',
                                       'failure_message': 'The total number of parameters in your network is incorrect.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> X = torch.randn(200, 10)\n'
                                               '>>> random_net = nn.Sequential(nn.Linear(10, 5), nn.ReLU(), nn.Linear(5, 3))\n'
                                               '>>> Y = random_net(X)\n'
                                               '>>> net = FCNN_11(10, 3, 32, 2)\n'
                                               '>>> output = net(X)\n'
                                               '>>> output.shape == (200, 3)\n'
                                               'True',
                                       'failure_message': "The shape of your network's output is incorrect.",
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': '>>> X = torch.randn(200, 10)\n'
                                               '>>> net = FCNN_11(10, 3, 32, 2)\n'
                                               '>>> out = net(X)\n'
                                               '>>> loss = out.mean()\n'
                                               '>>> loss.backward()\n'
                                               '>>> all_used = True\n'
                                               '>>> for name, param in net.named_parameters():\n'
                                               '...     if param.grad is None:\n'
                                               '...         all_used = False\n'
                                               '...         break\n'
                                               '>>> all_used\n'
                                               'True',
                                       'failure_message': 'The forward pass through your model does not use all parameters.',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
