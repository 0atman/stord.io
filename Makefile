users:
	@ssh root@stord.io "cd flask-keyval && docker-compose run web python print_users.py"
deploy:
	ssh root@stord.io "cd flask-keyval && git pull && docker-compose build && docker-compose up -d --force-recreate"
