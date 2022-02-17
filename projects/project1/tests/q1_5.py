test = {   'name': 'q1_5',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> # Hint: make sure the returned table has the labls:;\n'
                                               ">>> #   'Year' and 'Children per woman';\n"
                                               ">>> assert fertility_over_time('usa', 2010).labels == ('Year', 'Children per woman')\n",
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> assert all(fertility_over_time('usa', 2010).column('Year') == np.arange(2010, 2016))\n", 'hidden': False, 'locked': False},
                                   {'code': ">>> assert all(fertility_over_time('usa', 2005).column('Year') == np.arange(2005, 2016))\n", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
