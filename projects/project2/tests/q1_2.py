test = {   'name': 'q1_2',
    'points': 3,
    'suites': [   {   'cases': [   {'code': '>>> # Hint: make sure recent_poverty_total is a Table;\n>>> assert type(recent_poverty_total) == Table\n', 'hidden': False, 'locked': False},
                                   {   'code': '>>> # Make sure your column labels are spelled correctly and in this order;\n'
                                               ">>> assert recent_poverty_total.labels == ('geo', 'poverty_percent', 'population_total', 'poverty_total')\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # Careful, the population in Austrailia in 2010 was 22,162,863;\n'
                                               ">>> assert recent_poverty_total.where('geo', 'aus').column(2).item(0) == 22162863\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # The number of estimated people living poverty in Australia;\n'
                                               '>>> # should be 301,415. This is 22,162,863 * 0.0136;\n'
                                               ">>> assert np.round(recent_poverty_total.where('geo', 'aus').column(3).item(0))  == 301415\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
