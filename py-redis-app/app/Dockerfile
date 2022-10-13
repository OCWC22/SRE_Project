FROM python:slim-buster

# set work directory
WORKDIR /app

# set environment variables
#Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
#Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache -r requirements.txt
EXPOSE 9001
# copy project
COPY ./src /app/
RUN chmod +x /app/entrypoint.sh
# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]