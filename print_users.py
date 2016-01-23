import json

from redis import StrictRedis


r = StrictRedis(host='db', port=6379, db=0)
users = [
    v for
    v in r.hgetall('auth').values()
    if '@' in v and v != 'tristram@oaten.name'
]

print json.dumps({
    'users': users,
    'count': len(users)
})
