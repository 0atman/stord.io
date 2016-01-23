import json

from redis import StrictRedis


r = StrictRedis(host='db', port=6379, db=0)
users = [
    v.split(':')[0] for
    v in r.hgetall('auth').values()
]

print json.dumps({
    'users': users,
    'count': len(users)
})
