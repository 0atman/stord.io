---
title: "httpie"
bg: '#317331'  #defined in _config.yml, can use html color like '#0fbfcf'
color: white   #text color
fa-icon: terminal
date: 2016-02-01 01:01:01 -0000
---


### POST

{% highlight shell linenos=table %}
http post 'stord.io/key?auth=1234' hello=world
{% endhighlight %}

{% highlight yaml linenos=table %}
HTTP/1.0 200 OK
Content-Length: 21
Content-Type: application/json
Date: Wed, 20 Jan 2016 12:36:19 GMT
Server: Werkzeug/0.11.3 Python/2.7.11

{
    "hello": "world"
}
{% endhighlight %}


### PUT

{% highlight ruby linenos=table %}
http put 'stord.io/key/hello?auth=1234' value=world
{% endhighlight %}

{% highlight yaml linenos=table %}
HTTP/1.0 200 OK
Content-Length: 21
Content-Type: application/json
Date: Wed, 20 Jan 2016 12:36:19 GMT
Server: Werkzeug/0.11.3 Python/2.7.11

{
    "hello": "world"
}
{% endhighlight %}

### GET

{% highlight ruby linenos=table %}
http 'stord.io/key/hello?auth=1234'
{% endhighlight %}

{% highlight yaml linenos=table %}
HTTP/1.0 200 OK
Content-Length: 27
Content-Type: application/json
Date: Mon, 18 Jan 2016 12:31:55 GMT
Server: Werkzeug/0.11.3 Python/2.7.11

{
    "hello": "world"
}
{% endhighlight %}
