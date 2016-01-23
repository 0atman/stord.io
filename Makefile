token:
	docker-compose run web python generate_token.py
upgrade:
	docker-compose build
	docker-compose up -d
