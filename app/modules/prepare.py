from app.business import DomainIssue, by_kind, prepared, single


def prepare(rows):
    dispatch = single(rows,'dispatch')
    stops = by_kind(rows,'stop')
    route = {r['station']:r['ordinal'] for r in stops}
    if not route or len(route)!=len(stops) or len(set(route.values()))!=len(route) or 0 in route.values():
        raise DomainIssue('STOP_ORDER_CONFLICT')
    pings = by_kind(rows,'ping')
    if len(pings)>320 or not 0 < dispatch['minimum']<=len(route):
        raise DomainIssue('INVALID_DISPATCH')
    if any(r['station'] not in route or not 0 < r['score']<=100 or r['second']>dispatch['second'] for r in pings):
        raise DomainIssue('INVALID_PING')
    ordered = sorted(pings,key=lambda p:(p['second'],p['record']))
    return prepared(len(pings),{'registered_stops':len(route),'minimum':dispatch['minimum']},(route,ordered,dispatch['minimum']))
