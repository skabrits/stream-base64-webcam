FROM python:3.7.2

WORKDIR /app

RUN mkdir -p /hascam
RUN echo "False" > /hascam/has.txt

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "if [ \"$(cat /hascam/has.txt)\" = \"True\" ]; then gunicorn --chdir app app:app -b 0.0.0.0:8000; else tail -f /dev/null; fi"]