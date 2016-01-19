---
title: "Python"
bg: black  #defined in _config.yml, can use html color like '#0fbfcf'
color: white  #text color
fa-icon: file-code-o
---

{% highlight python linenos=table %}
import requests
requests.post('http://stord.io/api/store/hello?auth=1234', data={'data':'world'}).text
u'{"success": "world"}\n'
{% endhighlight %}

Easy! Lets throw together a few functions to store data simply:

{% highlight python linenos=table %}
import requests

def get(key):
    return requests.get(url + key, {'auth': '1234'}).json()

def put(key, value):
    return requests.put(url + key, {'auth': '1234', 'data': value}).json()

get('hello')
{"success": "world"}

put('hello', 'universe')
{"success": "world"}

get('hello')
{"success": "universe"}
{% endhighlight %}
