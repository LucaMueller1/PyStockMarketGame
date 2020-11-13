FROM python:3-alpine
#### uncomment to run cronjob - !!! 2nd CMD overwrites first CMD !!!
RUN mkdir -p /usr/src/app

ENV PROJ_DIR="/usr/src/app"
#ENV LOG_FILE="${PROJ_DIR}/app.log"
#ENV CRON_SPEC="0 5 * * *"

WORKDIR ${PROJ_DIR}


COPY ../../../Desktop/python-flask-server/requirements.txt /usr/src/app/



#COPY . ${PROJ_DIR}
RUN pip3 install --no-cache-dir -r requirements.txt
#RUN echo "${CRON_SPEC} python ${PROJ_DIR}/BackEnd/swagger_server/services/schedule_service.py >> ${LOG_FILE} 2>&1 > ${PROJ_DIR}/crontab"
#RUN touch ${LOG_FILE}
#RUN crontab ${PROJ_DIR}/crontab
#RUN crontab -l

COPY ../../../Desktop/python-flask-server /usr/src/app

EXPOSE 8080

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]
#CMD crond && tail -f ${LOG_FILE} # runs crond in the background