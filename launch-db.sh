# docker run --rm --name database -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=ormuco -v ormuco-db:/var/lib/mysql --network ormuco mysql
docker run --name database --rm -d \
	-e MYSQL_ROOT_PASSWORD=ormuco \
	-e MYSQL_DATABASE=ormucodb \
	-e MYSQL_USER=ormuco \
	-e MYSQL_PASSWORD=ormuco \
	-v ormucodb:/var/lib/mysql \
	--network ormuco \
	-p 3306:3306 \
	mysql:5.7
