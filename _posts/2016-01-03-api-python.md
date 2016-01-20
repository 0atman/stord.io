---
title: "Python"
bg: '#0a2a5c'  #defined in _config.yml, can use html color like '#0fbfcf'
color: white  #text color
fa-icon: file-code-o
---

### POST

{% highlight python linenos=table %}
>>> import requests
>>> requests.post('http://stord.io/api/store/hello?auth=1234', data={'data':'world'}).text
u'{"success": "world"}\n'
{% endhighlight %}

### GET

{% highlight python linenos=table %}
>>> import requests
>>> requests.get('http://stord.io/api/store/hello?auth=1234').text
u'{"success": "world"}\n'
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
{"success": "world"}

>>> put('hello', 'universe')
{"success": "world"}

>>> get('hello')
{"success": "universe"}
{% endhighlight %}
