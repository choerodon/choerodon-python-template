FROM python:3.7

RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]