build:
	docker build . -t gradio-asr-inference-service:1.0.1
dev:
	docker run -p 8080:8080 --rm -it -v ${PWD}:/dory gradio-asr-inference-service:1.0.1
