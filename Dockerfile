FROM python:3
WORKDIR /app
ADD requirements.txt ./
RUN pip install -r requirements.txt
ADD . .
ENTRYPOINT python manage.py migrate && python manage.py runserver 0.0.0.0:8000
EXPOSE 8000
