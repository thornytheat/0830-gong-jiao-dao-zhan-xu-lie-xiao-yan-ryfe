from app.business import measured


def compute(data):
    route,pings,minimum = data
    ranked = []
    for i,ping in enumerate(pings):
        eligible = [ranked[j] for j,prev in enumerate(pings[:i]) if prev['second']<ping['second'] and route[prev['station']]<route[ping['station']]]
        _,negative_score,path = min(eligible,default=(0,0,()))
        followed = (*path,i)
        ranked.append((-len(followed),negative_score-ping['score'],followed))
    _,negative_score,path = min(ranked,default=(0,0,()))
    visited = [pings[i]['station'] for i in path]
    return measured(len(path),minimum,'站',{'route':visited,'pings':[pings[i]['record'] for i in path],'missing':[k for k in sorted(route,key=route.get) if k not in visited],'confidence':-negative_score})
