FROM openjdk:slim

COPY --from=python:3.8-slim / /

# Install requirements for cts_celery
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
	# pip install uwsgi

# Copy the project code
COPY . /src/
WORKDIR /src

#COPY uwsgi.ini /etc/uwsgi/

RUN chmod 755 /src/start_flask.sh

CMD ["sh", "/src/start_flask.sh"]