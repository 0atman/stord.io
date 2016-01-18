---
title: "Python"
bg: white  #defined in _config.yml, can use html color like '#0fbfcf'
color: black   #text color
fa-icon: file-code-o
---

{% highlight python linenos=table %}
import requests
requests.post('http://stord.io/api/store/hello?auth=1234', data={'data':'world'}).text
{% endhighlight %}

Returns:
{% highlight python linenos=table %}
u'{"success": "world"}\n'
{% endhighlight %}