FROM python:3
ENV PYTHONUNBUFFERED 1
ENV http_proxy http://wwwproxy.unimelb.edu.au:8000/
ENV https_proxy http://wwwproxy.unimelb.edu.au:8000/
ENV HTTP_PROXY http://wwwproxy.unimelb.edu.au:8000/
ENV HTTPS_PROXY http://wwwproxy.unimelb.edu.au:8000/
RUN mkdir /tweet_harvester
WORKDIR /tweet_harvester
COPY requirements.txt /tweet_harvester/
RUN pip install -r requirements.txt
COPY . /tweet_harvester/
RUN chmod +x ./au.sh
RUN chmod +x ./mel.sh