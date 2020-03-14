FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /DRF
WORKDIR /DRF
COPY . /DRF
RUN pip install -r requirements.txt
ADD . /DRF/