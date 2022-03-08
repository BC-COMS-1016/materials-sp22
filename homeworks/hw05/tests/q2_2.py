test = {   'name': 'q2_2',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> # Remember that your function needs to return a value.;\n>>> assert simulate_key_strike() is not None\n', 'hidden': False, 'locked': False},
                                   {   'code': '>>> import string;\n'
                                               '>>> assert all([simulate_key_strike() in list(string.ascii_lowercase + string.ascii_uppercase + string.digits) for i in range(100)])\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> import numpy as np;\n>>> np.random.seed(22);\n>>> assert 62 >= len(np.unique([simulate_key_strike() for i in range(500)])) >= 45\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
