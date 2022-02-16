FROM jjanzic/docker-python3-opencv:latest

COPY ./start.sh /start.sh
RUN chmod +x /start.sh

COPY ./gunicorn_conf.py /gunicorn_conf.py

COPY ./start-reload.sh /start-reload.sh
RUN chmod +x /start-reload.sh

EXPOSE 80

# Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Gunicorn with Uvicorn
CMD ["/start.sh"]

ARG DF_PYPICLOUD_PASSWORD
ENV VERSION 3

# Copy requirements.txt first and install, to
# speed up docker builds+pushes (layers are cached).
RUN pip install --upgrade pip
RUN apt-get update
RUN apt-get install -y build-essential 
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Add application code.
COPY ./app /app/app

WORKDIR /app/

ENV PYTHONPATH=/app