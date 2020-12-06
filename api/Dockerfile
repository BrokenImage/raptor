# STEP 1: Add base image. Optimized for python
FROM python:3.7-slim-buster
# FROM tensorflow/tensorflow:2.2.0

# STEP 2: Add the requirements.txt file
ADD requirements.txt /requirements.txt

# STEP 3: Install requirements from requirements.txt
RUN pip install -r requirements.txt

# STEP 4: Copy source code in current directoy to the container
ADD . /app

# STEP 5: Set the working directory to the previousely added app directory
WORKDIR /app

# STEP 8: Expose the port Flask is running on
EXPOSE 8000

# STEP 9: Run Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]