# tna-python

This Docker image:

- defines the version of Python used for all derivative images
- sets up the Python, pip and Poetry environment variables
- installs gettext which is used to template out Poetry config with envsubst
- declares an open port
- creates a non-root user to execute the application with
- upgades pip
- copies the default build and run scripts
- installs Poetry
- adds Poetry and the virtual environment to the path
- copies in a default Poetry configuration

The dependencies declared are minimal and easy to maintain:

- gunicorn - so all Python applications can consistently be served behind a WSGI

The development dependencies should also now all be the same across all applications:

- black - for formatting of Python code
- coverage - provides integration with GitHub for test coverage
- flake8 - linting Python code
- isort - set order of imports

## Environment variables

- `TNA_APPLICATION_NAME` - the application name that gets compiled into the Poetry config
- `TNA_APPLICATION_VERSION` - the application version that gets compiled into the Poetry config
- `TNA_APPLICATION_DESCRIPTION` (optional) - a description of the application that gets compiled into the Poetry config
- `TNA_APPLICATION_ENTRYPOINT` - the entrypoint for gunicorn
