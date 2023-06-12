# tna-python-django

This Docker image:

- extends [tna-python](../tna-python)
- copies in a new run script and manage.py entrypoint specifically for Django applications
- adds a static version of Django to the dependency list ready for the install script

## Environment variables

In addition to the environment variables in [tna-python](../tna-python), the Django-specific variables are:

- `DJANGO_SETTINGS_MODULE` - https://docs.djangoproject.com/en/4.2/topics/settings/#designating-the-settings