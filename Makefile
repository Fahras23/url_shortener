run-db:
	docker run --name db_postgres -p 5433:5433 -e POSTGRES_PASSWORD=mysuperpassword -e POSTGRES_DB=urlshortener_db -v ${PWD}/db_data:/var/lib/postgresql/data -d postgres