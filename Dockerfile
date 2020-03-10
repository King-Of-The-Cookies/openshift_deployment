FROM python:3.6.10-buster

WORKDIR /app

COPY . /app

RUN pip install flask

CMD ["python", "app.py"]   
 
 
 
 
   
 
