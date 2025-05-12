# Developing a Single Page App with FastAPI and Vue.js

### Want to learn how to build this?

Check out the [post](https://testdriven.io/blog/developing-a-single-page-app-with-fastapi-and-vuejs).

## Want to use this project?

Build the images and spin up the containers:

```sh
$ docker-compose up -d --build
```

Apply the migrations:

```sh
$ docker-compose exec backend aerich upgrade
```

Ensure [http://localhost:5000](http://localhost:5000), [http://localhost:5000/docs](http://localhost:5000/docs), and [http://localhost:8080](http://localhost:8080) work as expected.

### fastapi db migrations
```bash
docker-compose exec backend rm -rf ./migrations
docker-compose exec backend aerich init -t src.database.config.TORTOISE_ORM
docker-compose exec backend aerich init-db
```


# pull secret


# Container Registry (github packages)

## Github Packages
* create personal access token (settings --> Developer settings -- > Personal Access Tokens), select classic
* select write:packages
* save the token to a file
* to see packages, go to your github profile and select tab Packages
* tag an image
```bash
docker build -t ghcr.io/<GITHUB-USERNAME>/image-name:latest -f Dockerfile .
```
* login to docker registry
```bash
cat ~/github-image-repo.txt | docker login ghcr.io -u <GITHUB-USERNAME> --password-stdin
```
* push image
```bash
docker push ghcr.io/<GITHUB-USERNAME>/image-name:latest
```

## create dockercongig secret
create a file with name .dockerconfig.json using this template

```bash

  {
    "auths": {
        "https://ghcr.io":{
            "username":"REGISTRY_USERNAME",
            "password":"REGISTRY_TOKEN",
            "email":"REGISTRY_EMAIL",
            "auth":"BASE_64_BASIC_AUTH_CREDENTIALS"
    	}
    }
}
```

```bash
kubectl create secret docker-registry github-pull-secret --from-file=.dockerconfigjson=.dockerconfig.json
```



