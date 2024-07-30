# pyk8s-hello

This is reference flask python application repository to build flask application using k8s and helm

### Some useful commands

```bash
# if using kubectl
kubectl apply -f manifests  # to apply manifests
kubectl delete -f manifests  # to destroy deployed app

# if using helm charts
helm install pyk8s-hello-release-1 pyk8s-hello/  # to deploy application
helm uninstall pyk8s-hello-release-1  # to destroy deployed app
```
