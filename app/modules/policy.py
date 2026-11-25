from app.business import decision


def policy(result):
    return decision(result,'MISSING_STOPS' if result['value']<result['expected'] else None,lower_bound=True)
