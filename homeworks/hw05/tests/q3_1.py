test = {   'name': 'q3_1',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> assert full_data.num_rows == 562\n', 'hidden': False, 'locked': False},
                                   {   'code': '>>> # Make sure you are combining the two tables in the correct order.;\n'
                                               '>>> # Use the instructions that "except Name column" as a hint for the correct order ;\n'
                                               ">>> assert full_data.labels[0] == 'Player'\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> row = full_data.select(sorted(full_data.labels)).sort(4).row(0);\n>>> assert row.Player == 'Tyler Cook' and row.Salary == 50000\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
