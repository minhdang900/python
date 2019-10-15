FROM python:2.7-alpine
# MAINTAINER Ravishankar Sivasubramaniam "ravi_siva@live.com"

# RUN addgroup -S flaskuser && adduser -S -g flaskuser flaskuser

#ADD . /flaskapp
ENV HOME /web
ENV PATH $PATH:/web


WORKDIR /web
COPY requirements.txt /web/
COPY manage.py /web/
COPY runserver.sh /web/

RUN pip install gunicorn
RUN pip install -r requirements.txt

COPY flaskapp /web/flaskapp
COPY runserver.sh /usr/local/bin/

RUN chmod 755 /web/runserver.sh
RUN chmod 755 /usr/local/bin/runserver.sh

RUN echo "Listing"
RUN ls -ltr /web
RUN ls -ltr /web/flaskapp


RUN pwd
#RUN python manage.py db init
#RUN python manage.py db migrate
#RUN python manage.py db upgrade
EXPOSE 4000

CMD ["runserver.sh"]
#ENTRYPOINT ["python"]
#CMD ["manage.py","runserver"]
