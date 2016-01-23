token:
	docker-compose run web python generate_token.py
upgrade:
	ssh root@stord.io cd flask-keyval && docker-compose build && docker-compose up -d --force-recreate
