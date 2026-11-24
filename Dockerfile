FROM alpine:3.22
RUN apk add --no-cache py3-pillow python3
COPY proof.py /app/proof.py
ENTRYPOINT ["/usr/bin/python3", "/app/proof.py"]
