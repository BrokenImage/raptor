# STEP 1: Add the base image
FROM node:13.12.0-alpine

# STEP 2: Set working directory
WORKDIR /app

# STEP 3: Add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# STEP 4: Install dependencies
COPY package.json ./
COPY package-lock.json ./
RUN npm install --silent
RUN npm install react-scripts@3.4.1 -g --silent

# STEP 5: Add current directory to docker image
COPY . ./

# STEP 6: Start the react app
CMD ["npm", "start"]