# FROM openjdk:slim
# FROM ubuntu/jre:8-22.04_3
FROM openjdk:22-slim

ENV APP_USER=www-data

# COPY --from=python:3.8-slim / /
COPY --from=python:3.11.4-slim / /

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