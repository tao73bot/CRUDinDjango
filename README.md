### 1. At first create virtual enviroment.

- `pyhton3 -m venv .venv`

### 2. Activate virtual enviroment.

- `source .venv/bin/activate`

### 3. Install Django

- `pip install django`

### 4. Upgrade pip

- `pip install --upgrade pip`

### 5. create requirements.txt

- `pip freeze > requirements.txt`

### 6. Create Django project

- `django-admin startproject project_name`

### 7. Go inside created project

- `cd project_name/`

### 8. Run server of project

- See if you have manage.py. if you have it then `python manage.py runserver`

### 9. Make migrations

- `python manage.py makemigrations`

### 10. Migrate Project

- `python manage.py migrate`

### 11. Create Super user for Admin

- `python manage.py createsuperuser`

### 12. Import os in settings.py file

- `import os`

- add this part at end
- `MEDIA_URL = '/media'`
- `MEDIA_ROOT = os.path.join(BASE_DIR,'media')`
- `STATIC_URL = 'static/'`
- `STATICFILES_DIR = [os.path.join(BASE_DIR,'static')]`

### in urls.py add static media settings

    from django.conf import settings 
    from django.conf.urls.static import static
    ...
    ...
    ...
    urlpatterns = [ path("admin/", admin.site.urls),] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



