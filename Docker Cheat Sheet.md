#### List docker images

```yaml
docker images
```

#### Create and run a new container from an image

```yaml
docker run image-name
```

#### Download an image from a registry

```yaml
docker pull image-name
```

#### Show info about all containers that have ever been run (default shows just running)

```yaml
docker ps -a
```

#### Search Docker Hub for images

```yaml
docker search
```

#### Remove one or more containers

```yaml
docker rm container-name
```

#### Build an image from a Dockerfile (run from Dockerfile directory) :-t => tag

```yaml
docker build -t bizcore-django:1.0 .
```

#### Run container :-p => publish exposed container port to host port :-it => enable interactive tty

```yaml
docker run -it -p 8000:8000 bizcore-django:1.0
```

#### Delete multiple images using their image ids

```yaml
docker rmi image-id image-id2 image-id3 -f
```

#### Create and start container from docker image using Docker Compose || build the services

```yaml
docker compose up || docker compose up --build
```

### Uploading docker image to Docker Hub

#### Login to Docker Hub account

```yaml
docker login
```

#### Tag your local image with your Docker Hub username i.e. username/docker-image

```yaml
docker tag bizcore-django:latest vinnjeru/bizcore-django:latest
```

#### Push your image to Docker Hub

```yaml
docker push vinnjeru/bizcore-django:latest
```

#### Create and run the container using your env file

```yaml
docker run -it -p 8000:8000 --env-file .env vinnjeru/bizcore-django
```
