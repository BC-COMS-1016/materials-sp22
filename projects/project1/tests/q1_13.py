test = {   'name': 'q1_13',
    'points': 2,
    'suites': [   {   'cases': [   {'code': '>>> # The table should have only two columns;\n>>> assert region_counts.num_columns == 2\n', 'hidden': False, 'locked': False},
                                   {'code': ">>> # Double check for typos in the names of the 2 columns;\n>>> assert region_counts.labels == ('region', 'count')\n", 'hidden': False, 'locked': False},
                                   {'code': ">>> # The counts must sum up to 50;\n>>> assert sum(region_counts.column('count')) == 50\n", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
