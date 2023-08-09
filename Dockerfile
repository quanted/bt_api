FROM openjdk:slim

ENV APP_USER=www-data

# COPY --from=python:3.8-slim / /

RUN apt-get update && \
	apt-get install -y \
		python3 \
		python3-pip

# Install requirements for bt_api
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt

RUN apt-get update -y && \
	apt-get upgrade -y

# Copy the project code
COPY . /src/
WORKDIR /src

RUN chown -R $APP_USER:$APP_USER /src /tmp

RUN chmod 755 /src/start_flask.sh

USER $APP_USER

CMD ["sh", "/src/start_flask.sh"]