# This should be a real image hosted on a registry but currently refers to a local image that we create
FROM tna-python

ENV TNA_APPLICATION_NAME="The National Archives Example Python Application"
ENV TNA_APPLICATION_VERSION="0.1.0"
# ENV TNA_APPLICATION_DESCRIPTION=""
ENV TNA_APPLICATION_ENTRYPOINT="server"

COPY --chown=app:app . .

RUN tna-build

CMD ["tna-run"]
