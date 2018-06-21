FROM alpine
LABEL maintainer="panu.markkanen@gmail.com"

RUN apk update
RUN apk add --no-cache bash python3 \
	&& pip3 install --upgrade pip \
	&& pip3 install flask
    
COPY . /app
WORKDIR /app
# RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]