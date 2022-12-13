FROM python:3
WORKDIR /usr/src
COPY requirements.txt ./
RUN mkdir my_django
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


