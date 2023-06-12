# Example TNA Python application

From the project root, run:

```sh
# Build the base TNA Python image
docker build -t tna-python docker/tna-python

# Build the base TNA Python/Django image
docker build -t tna-python-django docker/tna-python-django

# Build the application image (using the tna-python-django image)
docker build -t example-tna-python-django-application ./example-tna-python-django-application

# Run the application image
docker run -d --name example-tna-python-django-application -p 8080:8080 example-tna-python-django-application
```

For development to build the complete stack:

```sh
docker build -t tna-python --progress plain --no-cache docker/tna-python && docker build -t tna-python-django --progress plain --no-cache docker/tna-python-django && docker build -t example-tna-python-django-application --progress plain --no-cache ./example-tna-python-django-application && docker run -p 8080:8080 example-tna-python-django-application
```
