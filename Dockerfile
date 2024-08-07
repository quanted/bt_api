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

# RUN rm -rf \
# 	/usr/local/lib/python3.11/site-packages/pip-23.1.2.dist-info \
# 	/root/.cache/pip \
# 	/usr/local/lib/python3.11/site-packages/pip \
# 	/usr/local/pip3.11 \
# 	/usr/local/pip3 \
# 	/usr/local/pip

RUN mkdir -p /var/www

RUN chown -R $APP_USER:$APP_USER /src /tmp /var/www

RUN chmod 755 /src/start_flask.sh

USER $APP_USER

CMD ["sh", "/src/start_flask.sh"]