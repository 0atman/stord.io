import json

from redis import StrictRedis


r = StrictRedis(host='db', port=6379, db=0)
users = [
    v.split(':')[0] for
    v in r.hgetall('auth').values()
    if ('@' in v) and ('tristram@oaten.name' not in v)
]

print json.dumps({
    'users': users,
    'count': len(users)
})
