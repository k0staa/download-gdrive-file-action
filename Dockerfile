FROM python:3.9-slim-bullseye

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

RUN mkdir /scripts
COPY download_file.py /scripts/

ENTRYPOINT ["python", "/scripts/download_file.py"]
