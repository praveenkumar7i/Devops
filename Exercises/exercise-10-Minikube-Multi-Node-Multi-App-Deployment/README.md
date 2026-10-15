# Exercise 10: Minikube Multi-Node Multi-App Deployment

## 1. Objective

Deploy two Python Flask applications on a three-node Minikube Kubernetes
cluster. Use Deployments, replicas, pod anti-affinity and Services to
demonstrate application deployment and workload distribution.

## 2. Applications

| Application | Purpose | Replicas | Endpoint |
|---|---|---:|---|
| Product Catalog | Returns a list of products and prices | 2 | GET /products |
| Shopping Cart | Retrieves and adds cart items | 3 | GET /cart, POST /cart |

Total expected application pods: 5.

## 3. Technologies Used

- Python and Flask
- Docker
- Kubernetes
- Minikube
- kubectl
- YAML
- PowerShell and VS Code

## 4. Folder Structure

```text
exercise-10-Minikube-Multi-Node-Multi-App-Deployment/
├── product_catalog.py
├── shopping_cart.py
├── Dockerfile.product
├── Dockerfile.shopping
├── product_catalog_deployment.yaml
├── shopping_cart_deployment.yaml
├── product_catalog_service.yaml
├── shopping_cart_service.yaml
└── README.md
```

## 5. Architecture

```text
Developer
   |
   v
VS Code and PowerShell
   |
   v
Docker Images
   |
   v
Minikube Cluster (3 nodes)
   |
   +-- Product Catalog Deployment (2 replicas)
   |
   +-- Shopping Cart Deployment (3 replicas)
   |
   +-- Product Catalog Service
   |
   +-- Shopping Cart Service
```

Pod anti-affinity requires replicas of the same application to be placed
on different nodes. With three eligible nodes, the two Catalog pods and
three Cart pods can be spread across the cluster.

## 6. Execution Steps

### Step 1: Start a three-node Minikube cluster

```powershell
minikube start --nodes=3 -p devops-multinode --driver=docker
```

### Step 2: Enable the registry add-on

```powershell
minikube -p devops-multinode addons enable registry
```

### Step 3: Build Docker images

Run these commands from this directory:

```powershell
docker build -t product-catalog:latest -f Dockerfile.product .
docker build -t shopping-cart:latest -f Dockerfile.shopping .
docker images
```

### Step 4: Load images into Minikube

```powershell
minikube -p devops-multinode image load product-catalog:latest
minikube -p devops-multinode image load shopping-cart:latest
```

### Step 5: Apply Deployments and Services

```powershell
kubectl config use-context devops-multinode
kubectl apply -f product_catalog_deployment.yaml
kubectl apply -f shopping_cart_deployment.yaml
kubectl apply -f product_catalog_service.yaml
kubectl apply -f shopping_cart_service.yaml
```

### Step 6: Verify resources

```powershell
kubectl get nodes
kubectl get deployments
kubectl get replicasets
kubectl get pods -o wide
kubectl get services
```

Expected application replicas: 2 Catalog pods and 3 Cart pods, all Running
and Ready. Pod anti-affinity should distribute each application's replicas
across separate nodes.

### Step 7: Access the services

Run each command in its own terminal and keep the terminals open:

```powershell
minikube -p devops-multinode service product-catalog-service
```

```powershell
minikube -p devops-multinode service shopping-cart-service
```

Use the local URLs printed by Minikube. Add `/products` to the Product
Catalog URL and `/cart` to the Shopping Cart URL.

### Step 8: Test the APIs

Use the URLs printed in the terminals, replacing the example ports:

```powershell
curl.exe http://127.0.0.1:PORT/products
curl.exe http://127.0.0.1:PORT/cart
```

Add an item to the cart:

```powershell
curl.exe -X POST http://127.0.0.1:PORT/cart -H "Content-Type: application/json" -d "{\"id\":1,\"name\":\"Laptop\",\"quantity\":1}"
```

Replace PORT with the actual local port for the Shopping Cart service.

## 7. Expected Results

- Product Catalog returns three products.
- Shopping Cart initially returns an empty JSON array.
- Adding a cart item returns HTTP 201 and the updated cart.
- Two Product Catalog replicas are Ready.
- Three Shopping Cart replicas are Ready.
- Replicas of the same application are distributed across different nodes.

## 8. Important Notes

- Both Deployments and Services use the default namespace.
- The required pod anti-affinity rule prevents replicas of the same
  application from sharing a node.
- The cart is stored in application memory; it is not persistent and
  can differ between replicas.
- Keep the service tunnel terminals open while testing.
- Do not delete existing Minikube profiles unless you intend to remove them.

## 9. Cleanup

When you have finished testing, remove the exercise resources:

```powershell
kubectl delete -f product_catalog_service.yaml
kubectl delete -f shopping_cart_service.yaml
kubectl delete -f product_catalog_deployment.yaml
kubectl delete -f shopping_cart_deployment.yaml
```

To remove the entire exercise-specific Minikube cluster later, use:

```powershell
minikube -p devops-multinode delete
```

Only run the final command when you no longer need this cluster.
