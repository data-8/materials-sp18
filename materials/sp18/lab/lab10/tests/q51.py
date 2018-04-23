test = {
  'name': 'Question',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> len(secrets.split(" ")) == 4
          True
          >>> secrets.split(" ")[3][-1] == '!'
          True
          >>> len(secrets.split(" ")[2]) == 2
          True
          >>> (secrets.split(" ")[1][2] + secrets.split(" ")[1][0]).lower() == secrets.split(" ")[2]
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
