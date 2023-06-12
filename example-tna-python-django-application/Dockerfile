# This should be a real image hosted on a registry but currently refers to a local image that we create
FROM tna-python-django

ENV TNA_APPLICATION_NAME="The National Archives Example Python Django Application"
ENV TNA_APPLICATION_VERSION="0.1.0"
# ENV TNA_APPLICATION_DESCRIPTION=""
ENV DJANGO_SETTINGS_MODULE=my_django_application.settings

COPY --chown=app:app . .

RUN tna-build

CMD ["tna-run"]
