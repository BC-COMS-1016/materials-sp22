test = {   'name': 'q4_2',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> # Remember to create a sample size of 200 examples;\n>>> assert representative_sample.num_rows == 200\n', 'hidden': False, 'locked': False},
                                   {   'code': '>>> # all 200 samples should be in the original earthquakes table;\n'
                                               '>>> assert all(np.in1d(representative_sample.column("mag"), earthquakes.column("mag")))\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # The mean should be between the minimum mag and maximum mag in the 200 samples;\n'
                                               ">>> assert np.min(representative_sample.column('mag')) < representative_mean < np.max(representative_sample.column('mag'))\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
