FROM python:slim

WORKDIR /project

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

ENTRYPOINT [ "streamlit" ]

CMD [ "run", "app.py", "--server.port", "8080" ]
