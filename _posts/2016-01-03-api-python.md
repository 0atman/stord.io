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

get = lambda key: requests.get(url + key, {'auth': '1234'}).json()
put = lambda key, value: requests.put(url + key, {'auth': '1234', 'data': value}).json()

get('hello')
{"success": "world"}

put('hello', 'world')
{"success": "world"}
{% endhighlight %}
