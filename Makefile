serve:
	docker run --rm --label=jekyll --volume=/home/oatman/Projects/stord.io:/srv/jekyll -it -p 127.0.0.1:4000:4000 jekyll/builder:pages
