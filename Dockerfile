FROM python:latest

RUN mkdir /video_app
WORKDIR /video_app

# Copy files from current host to container
COPY ./  video_app
# unstall packages inside the container since all files have been copied over
RUN pip install -r video_app/requirements.txt

ENTRYPOINT ["python","./video_app/main.py"]

EXPOSE 3000