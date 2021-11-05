
make run:
	@gunicorn main:app \
			--bind 0.0.0.0:7777 \
			-w 2 --worker-class uvicorn.workers.UvicornWorker
