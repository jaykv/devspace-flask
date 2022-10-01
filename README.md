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
1. `devspace deploy`
2. `devspace open`


## TODO
- [x] Build a k8s service to expose app without port forwarding
- [x] Setup database service
- [ ] Build more flask services
- [ ] Create frontend app
- [ ] Templatize devspace.yaml