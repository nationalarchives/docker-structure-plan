# This should be a real image hosted on a registry but currently refers to a local image that we create
FROM tna-python

COPY --chown=app:app bin/tna-run .local/bin/
RUN chmod +x .local/bin/tna-run

COPY --chown=app:app lib/manage.py .
# RUN chmod +x manage.py

RUN echo "poetry add Django@4.2" >> .local/bin/tna-build
