test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(model_proportions) % 2 == 0
          True
          >>> len(np.unique(model_proportions)) == 1
          True
          >>> sum(model_proportions) == 1
          True
          >>> type(simulation_proportion) == float
          True
          >>> 0 <= one_test_statistic <= 20
          True
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
