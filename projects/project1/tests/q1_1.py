test = {   'name': 'q1_1',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> # It looks like you forgot to drop the column names "geo";\n>>> assert \'geo\' not in b_pop.labels\n', 'hidden': False, 'locked': False},
                                   {   'code': ">>> # Remember: b_pop should only have two labels: 'population_total' and 'time';\n>>> assert sorted(b_pop.labels) == ['population_total', 'time']\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Times should range from 1970 through 2015. Remember that second in are.between(first, second) is exclusive;\n'
                                               '>>> assert all(b_pop.sort("time").column("time") == np.arange(1970, 2016))\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
