all:
	python3 manage.py makemigrations
	python3 manage.py migrate

media:
	python3 manage.py collectstatic

runserv:
	python3 manage.py runserver
