# devspace-flask
Starter project to develop and deploy flask microservices on k8s using devspace.

Pre-reqs: 
1. kubernetes cluster (kind/minikube/k3s etc.)
2. docker
3. kubectl
4. devspace


## Development
- `devspace dev` for dev
- `devspace ui` for monitoring
- `devspace run bdi` to build base app image


## Deployment
1. `devspace deploy` to deploy app to k8s
2. `kubectl port-forward deployment/app1 8080:8080` to expose app


## TODO
[x] Build a k8s service to expose app without port forwarding
[x] Setup database service
[ ] Create frontend app
[ ] Templatize devspace.yaml