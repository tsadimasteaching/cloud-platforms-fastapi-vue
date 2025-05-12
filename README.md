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




helm repo add hashicorp https://helm.releases.hashicorp.com
helm repo update

helm install vault hashicorp/vault \
  --namespace vault \
  --create-namespace \
  --set server.ha.enabled=false \
  --set server.dataStorage.enabled=true \
  --set server.dataStorage.size=1Gi \
  --set server.dataStorage.storageClass=microk8s-hostpath


vault operator init (copy root token )

vault operator unseal <unseal-key-1>
vault operator unseal <unseal-key-2>
vault operator unseal <unseal-key-3>


## install vault cli (apt)

## port-forward and use it
kubectl port-forward svc/vault 8200:8200 -n vault
export VAULT_ADDR="http://127.0.0.1:8200"
vault status
vault login <token>
vault secrets enable kv
vault secrets enable -path=secret kv

## enable vault access to kubernetes
vault auth enable kubernetes


(from exec into vault pod)
vault login <token>

vault write auth/kubernetes/config \
token_reviewer_jwt="$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)" \
kubernetes_host="https://${KUBERNETES_PORT_443_TCP_ADDR}:443" \
kubernetes_ca_cert=@/var/run/secrets/kubernetes.io/serviceaccount/ca.crt

create a policy





vault kv put secret/jenkins username=rg password=alekos1111



vault policy write jenkins-policy policy.hcl

Bind Kubernetes service account to Vault:

vault write auth/kubernetes/role/jenkins-role \
bound_service_account_names=jenkins \
bound_service_account_namespaces=default \
policies=jenkins-policy \
ttl=24h


## Jenkins

