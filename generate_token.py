from uuid import uuid4
import datetime

from redis import StrictRedis


r = StrictRedis(host='db', port=6379, db=0)
new_token = uuid4()
r.hset('auth', new_token, datetime.datetime.now())
print new_token
