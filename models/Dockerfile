# STEP 1: Add base image. Optimized for python
FROM tensorflow/tensorflow:2.2.0

# STEP 2: Add the requirements.txt file
ADD requirements.txt /requirements.txt

# STEP 3: Install requirements from requirements.txt
RUN pip install -r requirements.txt

# STEP 4: Copy source code in current directoy to the container
ADD . /app

# STEP 5: Set the working directory to the previousely added app directory
WORKDIR /app

# STEP 8: Start commandline service

