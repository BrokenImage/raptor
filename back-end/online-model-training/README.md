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
  <h3 align="center">Sonomaly Online Model Training</h3>

  <p align="center">
    The deployment for the api to call when a new model needs to be trained automatically on new data because of a tigger determined on the api side, usually model accuracy decreasing.
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
* [MongoDB](https://www.mongodb.com/)

<!-- GETTING STARTED -->
## Getting Started

Lets get into setting this up for yourself.

### Installation

1. Install Docker following the instructions [here](https://docs.docker.com/get-docker/)
2. Currently in progress...


<!-- USAGE EXAMPLES -->
## Usage

* The goal/usage of this part of the service is to allow the api to train the model automatically without needing to have human involvment. Specificaly, this part is the current deployment of the automated training process with a specific framework includes thats allowing for the training to be hosted online. 


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
