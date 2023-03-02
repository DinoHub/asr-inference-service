# TODO: replace FROM
FROM dory_asr:v1.12.0
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENV TRANSFORMERS_CACHE="/dory/models/transformers_cache"

CMD ["python", "src/app.py"]
