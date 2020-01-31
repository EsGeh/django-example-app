# django-example-app

Small django example app following the famous tutorial <https://docs.djangoproject.com/en/2.1/intro/>.
Demonstrates the possibilities of custom apps and how to integrate them into the django-cms.

## Dependencies

- docker
- docker-compose
- python 3

## Scripts to Control the Webserver

- Initialize the repository

		$ ./scripts/install.py [--build]

- Start the Webserver

		$ ./scripts/run.py [--build] [CMD]

- Stop the Webserver

		$ ./scripts/stop.py

- Clean up the repository

		$ ./scripts/uninstall.py

## Other Scripts

- see './scripts/'. All scripts accept `--help`.
