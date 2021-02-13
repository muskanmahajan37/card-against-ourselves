FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/cards
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
