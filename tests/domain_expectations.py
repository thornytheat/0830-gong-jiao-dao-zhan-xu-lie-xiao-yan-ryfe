EXPECTED = {'0001': (4, 3, 'READY'),
 '0002': (2, 1, 'READY'),
 '0003': (0, None, 'STOP_ORDER_CONFLICT'),
 '0004': (2, 1, 'MISSING_STOPS')}
EVIDENCE = {'0001': {'route': [7, 8, 9],
          'pings': ['000105', '000106', '000107'],
          'missing': [],
          'confidence': 27},
 '0002': {'route': [5], 'pings': ['000204'], 'missing': [4], 'confidence': 6}}
