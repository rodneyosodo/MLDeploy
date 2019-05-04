# MLDeploy
How to simply deploy your Machine Learning models to production


## Getting Started

These instructions will get you a copy of the code up and running on your local host for development and testing purposes. Deployment will focus on one platform of my choice.

### Prerequisites

Things you will need to bring the project up on your local machine
```
Docker (Not necessarily but adviced)
Jupyter notebook
Python3
Text editor
```

### Installing

A step by step series of getting a development env running on your local machine

#### Windows

```
mkdir Big4
cd Big4
virtualenv --no-site-packages venv
venv\Scripts\activate
git clone https://github.com/0x6f736f646f/Big4Trendanalysis.git
cd Big4Trendanalysis
```

#### Unix

```
mkdir Big4
cd Big4
virtualenv --no-site-packages venv
.venv/bin/activate
git clone https://github.com/0x6f736f646f/Big4Trendanalysis.git
cd Big4Trendanalysis
```

#### Installing requirements

```
pip install -r requirements
```

#### Running webapp

```
python3 web.py
```
#### Running webapi

```
python3 api.py
```

### Dockerising your app

```
docker build -t mldeploy:1.0 .
```

* **-t** is to tag the image being built
* **mldepoly** is the image name your can replace it with your own image name
* **1.0** is the version

### Running docker web app container

```
docker run -d -p 4000:5000 big4trendanalysis:10.1 python3 web.py
```
* **-d** is running it as a daemon
* **-p** is for port mapping (We are mapping 5000 from docker container to 4000 to our localhost)
* **mldeploy** this is the image name we built
* **1.0** this is the version of the image we built
* **python3 web.py** this is passing a command to the container

### Running docker web api container
```
docker run -d -p 4000:5000 big4trendanalysis:10.1 python3 web.py
```
* **-d** is running it as a daemon
* **-p** is for port mapping (We are mapping 5000 from docker container to 4000 to our localhost)
* **mldeploy** this is the image name we built
* **1.0** this is the version of the image we built
* **python3 api.py** this is passing a command to the container

### Web app
#### Windows
Find your docker ip
```
docker-machine.exe ip
```
Then go to http:// *docker-machine ip*:4000

#### Otherwise
Go to [http://localhost:4000](http://localhost:4000) to find the web app or api


## Deployment

Procedure on how to deploy on heroku as a live system. I choosed installation through the command line because it was easier for me than the web based view.

    install heroku cli for windows and linux users
```
heroku login
heroku create --region eu your_appname # creates app in eu region, common regions: eu, us
heroku buildpacks:set heroku/python # set python buildpack
git push heroku master # deploy app to heroku
heroku logs --tail # If for some reason it’s not working, check the logs
```

## Built With

* [Docker](https://www.docker.com/) - Container development tool
* [Flask](https://maven.apache.org/) - The web framework used
* [Heroku](https://www.heroku.com/) - Platform

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* AI saturday Kenya
