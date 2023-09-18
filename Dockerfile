FROM python:3.9.16-bullseye



# Django Development Setup
WORKDIR /app
COPY . .

# create virtual env
RUN python3 -m venv env

# install requirements
RUN /app/env/bin/pip3 install --default-timeout=100 -r requirements.txt

# gunicorn setup
RUN /app/env/bin/python -m pip install --default-timeout=100 'gunicorn==20.1.*'
RUN mkdir -pv /var/{log,run}/gunicorn/
RUN chown -cR $USER:$USER /var/{log,run}/gunicorn/
RUN mkdir /var/log/gunicorn/
RUN mkdir /var/run/gunicorn/
RUN touch /var/log/gunicorn/dev.log

EXPOSE 8000
CMD ["./start.gunicorn.sh"]

