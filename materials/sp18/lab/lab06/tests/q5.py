test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> int(round(test_statistic(.5,.5) + test_statistic(.4,.1),1))
          30
          >>> int(test_statistic(.4,.1) - test_statistic(.1,.4))
          0
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
