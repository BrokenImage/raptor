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

1. Install Docker following the instructions [here](https://docs.docker.com/get-docker/)
2. Clone the repo
```sh
git clone https://github.com/BrokenImage/raptor-api.git
```
3. Build the Docker image (make sure Docker is running)
```sh
docker build -t sonomaly-api .
```
4. Start a Docker container
```sh
docker run -p 8000:8000 --rm --name sonomaly-api-container sonomaly-api
```


<!-- USAGE EXAMPLES -->
## Usage

The API can be called from Postman, using curl, or can be called by the like in the sonomoly frontend repo

<!-- Deployment -->
## Deployment

1. Follow the [Installation](#installation) guide above.
4. Generally, follow [this](https://medium.com/swlh/caprover-the-definitive-guide-90076405aae4) guide to setup caprover on an Ubuntu 18 server hosted by the cloud service of your choice. (we used AWS EC2 free tier)
5. Create a new app on your caprover server with the name of your choice.
6. Add enviroment variables needed for the API to run, creating the realted resouces following standard guidelines
```sh
AWS_ACCESS_KEY_ID=
AWS_SECRET_KEY=
AWS_BUCKET_NAME=
MONGO_CLIENT_URL=
```
6. Compact the prediction API into a .tar file (mac os command)
```sh
tar -czf prediction-api.tar prediction-api/
```
7. Upload the file to the caprover app you created earlier.
8. Make sure the build is successful on the caprover deployment logs
9. Go to the url you setup during the caprover setup and you should see the swagger ui for the api

ps. Due to issues with swagger ui not handling multiple file upload properly, you will not be able to test it there but the api will work when properly sent request.


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
[contributors-shield]: https://img.shields.io/github/contributors/BrokenImage/raptor-api.svg?style=flat-square
[contributors-url]: https://github.com/BrokenImage/raptor-api/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/BrokenImage/raptor-api.svg?style=flat-square
[forks-url]: https://github.com/BrokenImage/raptor-api/network/members
[stars-shield]: https://img.shields.io/github/stars/BrokenImage/raptor-api.svg?style=flat-square
[stars-url]: https://github.com/BrokenImage/raptor-api/stargazers
[issues-shield]: https://img.shields.io/github/issues/BrokenImage/raptor-api.svg?style=flat-square
[issues-url]: https://github.com/BrokenImage/raptor-api/issues
[license-shield]: https://img.shields.io/github/license/BrokenImage/raptor-api.svg?style=flat-square
[license-url]: https://github.com/BrokenImage/raptor-api/blob/master/LICENSE.txt
[product-screenshot]: images/screenshot.png
