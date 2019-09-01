FROM python:3.7-alpine
RUN mkdir /app
ARG project_dir=/app
ADD api03.py $project_dir
WORKDIR $project_dir
RUN pip install flask
ENV FLASK_APP=api03.py
ENTRYPOINT ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
