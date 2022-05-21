FROM python:3.9-slim-bullseye

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY download_file.py ./

ENTRYPOINT ["python", "download_file.py"]
