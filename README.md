<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <h3 align="center">Sonomaly Prediction API</h3>

  <p align="center">
    The API backend for the Sonomaly frontend website
    <br />
    <a href="https://github.com/BrokenImage/raptor-api"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#">View Demo</a>
    ·
    <a href="https://github.com/BrokenImage/raptor-api/issues">Report Bug</a>
    ·
    <a href="https://github.com/BrokenImage/raptor-api/issues">Request Feature</a>
  </p>
</p>

# Live
Visit this link http://raptor-app.raptorapps.com/

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Installation](#installation)
* [Usage](#usage)
* [Deployment](#deployment)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)


<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

Sonomaly is a capstone project for the Raptor Maps Student team that was formed from the collaboration of Raptor Maps and make School. This repo is for the backend of that application that aims to be a full production level machine learning pipline that inclues continual learning/development and a model registry. 

Here's why:
* Machine learning in production is a new feild and is something that data scientist need to learn
* Being able to understand industy standards for deployment to production is important

This is only one part of this project and you should look at the other parts on the team organization.

### Built With
* [Tensorflow](https://www.tensorflow.org/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Flask RestPlus](https://flask-restplus.readthedocs.io/en/stable/)
* [Caprover](https://caprover.com/)
* [AWS](https://aws.amazon.com/ec2/)


<!-- GETTING STARTED -->
## Getting Started

Lets get into setting this up for yourself.

### Installation

#### To run on machine locally
##### Set up React 
Must have `Node.js` installed. From root directory, type
```
cd front-end
npm install 
npm run build
```
##### Set up Flask server 
Must have `virtualenv` python package installed. From root directory, type
```
cd back-end
virtualenv env 
source env/bin/activate
pip install -r requirements.txt
python app.py
```
Go to http://localhost:5000 to try out the API.


#### To run on Docker

1. Install Docker following the instructions [here](https://docs.docker.com/get-docker/)
2. Clone the repo
```sh
git clone https://github.com/BrokenImage/raptor-api.git
```
3. Create a production build of the frontend (this will build the frontend into the back-end static folder)
```sh
cd front-end
npm install
npm run build
```
4. Start and build the Docker container
```sh
docker-compose up [--build if you're activly making changes]
```


<!-- USAGE EXAMPLES -->
## Usage

The API can be called from Postman, using curl, or can be called by the like in the sonomoly frontend repo

<!-- Deployment -->
## Deployment

1. Follow the [Installation](#installation) guide above.
4. Generally, follow [this](https://medium.com/swlh/caprover-the-definitive-guide-90076405aae4) guide to setup caprover on an Ubuntu 18 server hosted by the cloud service of your choice. (we used [DigitalOcean](https://www.digitalocean.com/))
5. Create a new app on your caprover server with the name of your choice.
6. Add enviroment variables needed for the API to run, creating the realted resouces following standard guidelines
```sh
AWS_ACCESS_KEY_ID=
AWS_SECRET_KEY=
AWS_BUCKET_NAME=
MONGO_CLIENT_URL=
```
6. Compress the backend into a .tar file (mac os command)
```sh
tar -czf back-end.tar back-end/
```
7. Upload the file to the caprover app you created earlier.
8. Make sure the build is successful on the caprover deployment logs
9. Go to the url you deployed during caprover's setup, you should see the react front-end for the application

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/BrokenImage/raptor-api/issues) for a list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/BrokenImage/raptor.svg?style=flat-square
[contributors-url]: https://github.com/BrokenImage/raptor/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/BrokenImage/raptor.svg?style=flat-square
[forks-url]: https://github.com/BrokenImage/raptor/network/members
[stars-shield]: https://img.shields.io/github/stars/BrokenImage/raptor.svg?style=flat-square
[stars-url]: https://github.com/BrokenImage/raptor/stargazers
[issues-shield]: https://img.shields.io/github/issues/BrokenImage/raptor.svg?style=flat-square
[issues-url]: https://github.com/BrokenImage/raptor/issues
[license-shield]: https://img.shields.io/github/license/BrokenImage/raptor.svg?style=flat-square
[license-url]: https://github.com/BrokenImage/raptor/blob/master/LICENSE.txt
[product-screenshot]: images/screenshot.png
