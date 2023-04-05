# Django-blog
 This is my first python django-based blog. 

## First install pipenv 
     pip install pipenv

## Then, run the following commands 
(it will install all the required dependencies within the environment)
```
     pipenv install django~=3.1.0
     pipenv install markdown==3.2.1
     pipenv install django-markdownx
```

## and Finally,:
continue
```
   pipenv shell
   python manage.py makemigrations
   python manage.py migrate
   python manage.py createsuperuser  (then create an admin account)
   python manage.py runserver  ( then just visit localhost:5000/admin and login, then continue to make your posts)
  ```
  
  
#AAiT #beginner
