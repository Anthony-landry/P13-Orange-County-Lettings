FROM python:3.11-slim
ENV PYTHONUNBUFFERED 1
RUN mkdir /oc_p13_lettings
WORKDIR /oc_p13_lettings
COPY . /oc_p13_lettings/
RUN pip install -r requirements.txt
CMD python manage.py runserver 0.0.0.0:8000