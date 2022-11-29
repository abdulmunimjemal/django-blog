# django-blog
 This is my first python django-based blog. 

first install pipenv
pip install pipenv
when it finishes, run the following commands
pipenv install django~=3.1.0
pipenv install markdown==3.2.1
pipenv install django-markdownx
pipenv shell

Then do this:

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  (then create an admin account)
python manage.py runserver  ( adn then visit localhost:5000/admin and login, then continue to make your posts)

#AAiT
