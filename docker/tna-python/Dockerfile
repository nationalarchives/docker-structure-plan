FROM python:3.11-slim

ENV \
  # python:
  PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PYTHONDONTWRITEBYTECODE=1 \
  PYTHON_VIRTUAL_ENV=/home/app/.venv \
  # pip:
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  # poetry:
  POETRY_HOME=/home/app/.local \
  POETRY_VERSION=1.4.2 \
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=true \
  POETRY_VIRTUALENVS_IN_PROJECT=true

RUN apt-get update && \
    apt-get install -y --no-install-recommends gettext=0.21-12 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

EXPOSE 8080

RUN groupadd -r tnacontainergroup && \
    useradd --no-log-init -r -g tnacontainergroup app
USER app
WORKDIR /home/app

# RUN python3 -m venv $PYTHON_VIRTUAL_ENV
# RUN pip install --upgrade pip

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
RUN curl -sSL "https://install.python-poetry.org" | python -

ENV PATH="/home/app/.local/bin:${PYTHON_VIRTUAL_ENV}/bin:${PATH}"

COPY --chown=app:app bin/tna-build bin/tna-run .local/bin/
RUN chmod +x .local/bin/tna-build .local/bin/tna-run

COPY --chown=app:app pyproject.toml.template poetry.lock ./

LABEL maintainer="Andrew Hosgood <andrew.hosgood@nationalarchives.gov.uk>" \
      version="0.1.0"
