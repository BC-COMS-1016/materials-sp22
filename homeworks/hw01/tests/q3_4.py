test = {   'name': 'q3_4',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> # It looks like you forgot to round the final results after converting to Celsuis to the nearest integer.;\n'
                                               '>>> # Use the np.round() function;\n'
                                               '>>> assert round(celsius_max_temperatures.item(0), 4) != -3.8889\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # It looks like you multiplied and subtracted in the wrong order.;\n>>> assert sum(celsius_max_temperatures) != 356705.0\n',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> assert sum(celsius_max_temperatures) == 1280677.0\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert len(celsius_max_temperatures) == 65000\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> assert celsius_max_temperatures.item(2003) == 20.0\n', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
