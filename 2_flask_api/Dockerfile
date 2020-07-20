FROM python:3.8.4-buster
COPY . /app
WORKDIR /app/api
ENV POSTGRES_DB=postgresdb
ENV POSTGRES_USER=postgresadmin
ENV POSTGRES_PASSWORD=admin123
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]