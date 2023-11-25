FROM python:3.10-slim
COPY . .
ADD https://github.com/vishnubob/wait-for-it/raw/master/wait-for-it.sh /usr/local/bin/wait-for-it
RUN chmod +x /usr/local/bin/wait-for-it
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD wait-for-it postgres:5432 -- python create_table_apartmants.py && \
    python parser.py 1 && \
    python get_data.py