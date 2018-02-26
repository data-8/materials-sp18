test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(simulated_test_statistics) == 1000
          True
          >>> np.all(simulated_test_statistics <= 30)
          True
          >>> np.all(simulated_test_statistics >= 0)
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
