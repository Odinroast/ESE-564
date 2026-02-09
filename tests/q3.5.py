OK_FORMAT = True

test = {   'name': 'q3.5',
    'points': 7,
    'suites': [   {   'cases': [   {   'code': '>>> type(joints_35) is list and len(joints_35) == 7\nTrue',
                                       'failure_message': 'IK did not return any joint angles',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0},
                                   {   'code': ">>> joint_ids = [mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_JOINT, f'panda_joint{i + 1}') for i in range(7)]\n"
                                               '>>> all((joints_35[i] >= model.jnt_range[joint_ids[i], 0] and joints_35[i] <= model.jnt_range[joint_ids[i], 1] for i in range(7)))\n'
                                               'True',
                                       'failure_message': 'The joint values do not respect joint limits',
                                       'hidden': False,
                                       'locked': False,
                                       'points': 0}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
