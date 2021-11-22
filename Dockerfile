FROM python:3.8

# USER app
ENV PYTHONUNBUFFERED 1
# RUN mkdir /db
#RUN chown app:app -R /db




WORKDIR /lom

COPY Pipfile Pipfile.lock /lom/
RUN pip install pipenv && pipenv install --system

COPY . /lom