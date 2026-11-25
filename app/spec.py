COLUMNS = ('station', 'ordinal', 'second', 'score', 'minimum')
KINDS = ('stop', 'ping', 'dispatch')
PROJECT = {'name': '公交到站序列校验', 'actor': '公交运营数据员', 'stages': [('intake', '样例采信'), ('prepare', '定位候选'), ('calculate', '站序匹配'), ('policy', '漏站复核'), ('balance', '运行对账')], 'chart': '匹配线路', 'mark': '公'}
