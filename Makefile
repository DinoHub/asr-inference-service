build:
	docker build . -t singlish-asr-inference-service:1.0.0
dev:
	docker run -p 8080:8080 --rm -it singlish-asr-inference-service:1.0.0
