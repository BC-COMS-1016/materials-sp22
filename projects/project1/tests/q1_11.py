test = {   'name': 'q1_11',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> ## It looks like you are returning incorrect labels;\n'
                                               '>>> t = stats_for_year(1990);\n'
                                               ">>> assert t.labels == ('geo', 'population_total', 'children_per_woman_total_fertility', 'child_mortality_under_5_per_1000_born')\n",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # It looks like you are returning the incorrect number of rows;\n>>> t = stats_for_year(1990);\n>>> assert t.num_rows == 50\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> assert round(np.average(stats_for_year(1960).sort('geo').column('children_per_woman_total_fertility')), 3) == 5.627\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
