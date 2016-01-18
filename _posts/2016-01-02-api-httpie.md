---
title: "Command line"
bg: black  #defined in _config.yml, can use html color like '#0fbfcf'
color: white   #text color
fa-icon: terminal
---

{% highlight ruby linenos=table %}
http 'stord.io/api/store/hello?auth=1234'
{% endhighlight %}

Returns:

{% highlight yaml linenos=table %}
HTTP/1.0 200 OK
Content-Length: 27
Content-Type: application/json
Date: Mon, 18 Jan 2016 12:31:55 GMT
Server: Werkzeug/0.11.3 Python/2.7.11

{
    "success": "world"
}
{% endhighlight %}