# STEP 1: Add base image. Optimized for python
FROM python:3.7-slim-buster
# FROM tensorflow/tensorflow:2.2.0

# STEP 2: Setup enviroment variables
ARG AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
ARG AWS_SECRET_KEY=${AWS_SECRET_KEY}
ARG AWS_BUCKET_NAME=${AWS_BUCKET_NAME}
ARG MONGO_CLIENT_URL=${MONGO_CLIENT_URL}

# STEP 2: Add the requirements.txt file
ADD requirements.txt /requirements.txt

# STEP 3: Install requirements from requirements.txt
RUN pip install -r requirements.txt && pip install 'pymongo[srv]'

# STEP 4: Copy source code in current directoy to the container
ADD . /app

# STEP 5: Set the working directory to the previousely added app directory
WORKDIR /app

# STEP 8: Expose the port Flask is running on
EXPOSE 8000

# STEP 9: Run Flask with Gunicorn managing it
CMD ["gunicorn","--bind","0.0.0.0","wsgi"]