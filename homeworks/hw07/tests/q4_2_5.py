test = {   'name': 'q4_2_5',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> # Make sure bootstrap_max_estimates has 7500 examples;\n>>> assert len(bootstrap_max_estimates) == 7500\n', 'hidden': False, 'locked': False},
                                   {'code': '>>> np.random.seed(1234);\n>>> assert np.round(np.mean(sample_estimates(observations, max, 8000)), 5) == 122.35675\n', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
