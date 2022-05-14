# Pi Sensor to Prom
This project contains an example of how to configure and expose sensors to a Prometheus instance for scraping using python, Docker, and Prometheus.

## Installation
This requires python and docker. If they are not already installed then they should be. I recommend installing <a href="https://docs.docker.com/desktop/">Docker Desktop</a> for your platform to more easily manage images. It can also be installed using brew or winget.


```sh
brew install docker --cask
```

```pwsh
winget install Docker.DockerDesktop
```

Using docker, it is not required to install prometheus, since its reference will be pulled automatically from the Dockerfile.

## Theory
Prometheus is an excellent way to store time series data from sensors, particularly with its gauge metric. It requires very little code knowledge, as demonstrated in the small size of the python file, no exporting of any file, and only a light configuration.

On the client machine, a raspberry pi or similar device, the python script will run pulling data from sensors and hands it off to prometheus as a gauge metric. In the python code the prometheus http server is started.

This HTTP server can be used to view the data from the client. Another machine on the local network can read this page and scrape it periodically, storing it into the prometheus server. Notably, this machine can also host the UI for interacting with the prometheus server, so data can be viewed easily -- no code required.

## Usage
Move `sensor.py` and `requirements.txt` to the client machine, install the only requirement (prometheus client) and begin the service by simply running `sensor.py`. The client should be exposing viewable data from prometheus at localhost:8000.

Your router will have configured a local IP address for the client. On another machine, running docker desktop, place that IP address in `prometheus.yml` file in place of where it says `host.docker.internal`. This tells the prometheus server where it should be scraping data from.

Next, run the following command in this project's directory.
```sh
docker build -t prom_server .
```
This will create an image for the prometheus server with the cofinguration set correctly.

From the Docker Desktop Images tab run the prom_server image, with the port 9090 set, to create a container.

This container should be running and actively scraping data, view it at localhost:9090.