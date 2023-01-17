# TODO: replace FROM
FROM dory_asr:v1.14.0-torch1.11
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "src/app.py"]
