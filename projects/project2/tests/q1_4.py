test = {   'name': 'q1_4',
    'points': 2,
    'suites': [   {   'cases': [   {'code': ">>> # Hint: poverty_map should not have a column named country;\n>>> assert 'country' not in poverty_map.labels\n", 'hidden': False, 'locked': False},
                                   {   'code': '>>> # Make sure the column names are not misspelled and in the right order;\n'
                                               ">>> assert poverty_map.labels == ('latitude', 'longitude', 'name', 'region', 'poverty_total')\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> # Check your region column;\n>>> assert list(np.sort(np.unique(poverty_map.column('region')))) == ['africa', 'americas', 'asia', 'europe']\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
