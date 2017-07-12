# Simple Photo Gallery Django App
### flexbox thumbnails with a lightbox display

## How To Use
1. Install python lib requirements (see requirements.txt)
2. Is redis installed? redis is used as key/value store for sorl-thumbnails.  You can change this in photo_gallery/settings.py
3. Setup database by running migrations (python manage.py migrate)
4. Create superuser (python manage.py createsuperuser)
5. Run the server (python manage.py runserver) or deploy using wsgi server (such as gunicorn)
6. Log in to Admin page. (http://your_url_here/admin)
7. From the Admin page you can add photos to your gallery, (or create other users who can then login and add photos)
8. You can view the resulting photo gallery at http://your_url_here

