FROM python:3.10-alpine
RUN network=selenoid

WORKDIR /otus-pageobject

COPY requirements.txt .

RUN pip install -U pip
RUN pip install -r requirements.txt
COPY . /otus-pageobject

ENTRYPOINT ["pytest"]
