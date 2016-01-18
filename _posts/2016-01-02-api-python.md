---
title: "Python"
bg: black  #defined in _config.yml, can use html color like '#0fbfcf'
color: white   #text color
fa-icon: fa-file-code-o
---

{% highlight python linenos=table %}
import requests

print requests.post('http://stord.io/api/store/hello?auth=1234', data={'data':'world'}).text
u'{"success": "world"}\n'
{% endhighlight %}
