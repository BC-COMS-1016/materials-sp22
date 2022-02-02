test = {   'name': 'q2_3_1',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> # It looks liky you are not making an array. ;\n'
                                               '>>> # You shouldnt need to use .item in your solution;\n'
                                               '>>> import numpy as np;\n'
                                               '>>> assert type(population_magnitudes) == np.ndarray\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> # You made an array but there is an issue with the numbers in the array;\n'
                                               '>>> import numpy as np;\n'
                                               '>>> assert sum(abs(population_magnitudes - np.log10(population_amounts))) < 1e-6\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
