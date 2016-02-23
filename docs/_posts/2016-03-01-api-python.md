---
title: "Python"
bg: '#05152e'  #defined in _config.yml, can use html color like '#0fbfcf'
color: white  #text color
fa-icon: file-code-o
date: 2016-03-01 01:01:01 -0000
---

### POST

{% highlight python linenos=table %}
>>> import requests
>>> requests.post('http://stord.io/key?auth=1234', data={'hello':'world'}).text
u'{"hello": "world"}\n'
{% endhighlight %}

### GET

{% highlight python linenos=table %}
>>> import requests
>>> requests.get('http://stord.io/key/hello?auth=1234').json()
{"hello": "world"}
{% endhighlight %}

Easy! Lets throw together a few functions to store data simply:

{% highlight python linenos=table %}
import requests


base_url = 'http://stord.io/key/'

def get(key):
    return requests.get(base_url + key, {'auth': '1234'}).json()

def put(key, value):
    return requests.put(base_url + key, {'auth': '1234', 'data': value}).json()

>>> get('hello')
{"hello": "world"}

>>> put('hello', 'universe')
{"hello": "world"}

>>> get('hello')
{"hello": "universe"}
{% endhighlight %}
