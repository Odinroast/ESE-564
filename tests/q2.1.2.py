OK_FORMAT = True

test = {   'name': 'q2.1.2',
    'points': 10,
    'suites': [   {   'cases': [   {   'code': '>>> outputs = []\n'
                                               '>>> s = LIFOStack_212()\n'
                                               ">>> s.add_node('a')\n"
                                               ">>> s.add_node('b')\n"
                                               '>>> outputs.append(s.get_next())\n'
                                               ">>> s.add_node('c')\n"
                                               '>>> outputs.append(s.get_next())\n'
                                               '>>> outputs.append(s.get_next())\n'
                                               ">>> outputs == ['b', 'c', 'a'] and len(s) == 0\n"
                                               'True',
                                       'failure_message': "The expected output sequence was ['b','c','a'] and the stack should be empty at the end.",
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
