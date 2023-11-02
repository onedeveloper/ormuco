Requiremnets:
- kind
- helm
- docker

# initializing the project:

## create the cluster
```console
kind create cluster --config cluster.yaml
```

## build the backend image
```console
docker build -t ormuco-backend:1.2 .
```

## ensure the image is available to the cluster
```console
kind load docker-image ormuco-backend:1.2
docker exec -it $(kind get clusters | head -1)-control-plane crictl images
```

# deploying the application

```console
helm install ormuco-database ./charts/ormuco-database
helm install ormuco-backend ./charts/ormuco-backend
```

# testing the application
```console
kubectl get pods
kubectl get services
kubectl port-forward service/ormuco-backend 8000:80
```

# running the tests
```console
# write to the database
curl -X 'POST' \
  'http://localhost:8000/items/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "pencil",
  "price": 1.0,
  "count": 100
}'

# get a list of items
curl -X 'GET' \
  'http://localhost:8000/items/' \
  -H 'accept: application/json'
```

you can also reach the api documentation via:
http://localhost:8000/docs

