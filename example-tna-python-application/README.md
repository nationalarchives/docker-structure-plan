# Example TNA Python application

From the project root, run:

```sh
# Build the base TNA Python image
docker build -t tna-python docker/tna-python

# Build the application image (using the tna-python image)
docker build -t example-tna-python-application ./example-tna-python-application

# Run the application image
docker run -d --name example-tna-python-application -p 8080:8080 example-tna-python-application
```

For development to build the complete stack:

```sh
docker build -t tna-python --progress plain --no-cache docker/tna-python && docker build -t example-tna-python-application --progress plain --no-cache ./example-tna-python-application && docker run -d --name example-tna-python-application -p 8080:8080 example-tna-python-application
```
