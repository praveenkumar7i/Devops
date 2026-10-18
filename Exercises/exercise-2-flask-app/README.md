# Exercise 2: Deploy a Flask App on Minikube

## Objective

To containerize a Python Flask application using Docker and deploy it on a local Kubernetes cluster using Minikube. The application is exposed through a NodePort Service and verified using `curl`.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python Flask | Develop the web application |
| Docker | Build the application image |
| Minikube | Run a local Kubernetes cluster |
| Kubernetes | Deploy and manage the application |
| YAML | Define Deployment and Service resources |
| kubectl | Manage Kubernetes resources |

## Project Structure

| File | Description |
|---|---|
| `app.py` | Flask application |
| `Dockerfile` | Instructions for building the Docker image |
| `flask-deployment.yaml` | Kubernetes Deployment and Service configuration |
| `evidence-deployments.txt` | Deployment status |
| `evidence-pods.txt` | Pod status |
| `evidence-services.txt` | Service details |
| `evidence-describe-deployment.txt` | Detailed Deployment information |
| `evidence-curl-output.txt` | Application response |

## Implementation

### 1. Start Minikube

Start the local Kubernetes cluster and check its status.

```powershell
minikube start
minikube status
```

### 2. Build the Docker Image

Build the Flask application image directly inside Minikube so that Kubernetes can access it locally.

```powershell
minikube image build -t flask-app:latest .
minikube image ls | Select-String flask-app
```

**Image name:** `flask-app:latest`

### 3. Deploy the Application

Apply the Kubernetes configuration to create the Deployment and Service.

```powershell
kubectl apply -f flask-deployment.yaml
```

### 4. Verify Deployment and Pod Status

```powershell
kubectl get deployments
kubectl get pods -l app=flask-app
kubectl describe deployment flask-app
```

The Deployment should show `1/1` available, and the Pod should be in the `Running` state.

### 5. Check Application Logs

```powershell
kubectl logs -l app=flask-app
```

The logs confirm that the Flask application is running and listening on port `15000`.

### 6. Access the Application

Get the Service URL:

```powershell
minikube service flask-app-service --url
```

Use the URL returned by your terminal to test the application:

```powershell
curl http://127.0.0.1:<PORT>
```

Replace `<PORT>` with the actual port in the returned URL.

## Port Configuration

| Setting | Value | Description |
|---|---:|---|
| Flask application port | `15000` | Port on which Flask listens |
| Container port | `15000` | Port declared for the application container |
| Service port | `15000` | Port exposed by the Kubernetes Service |
| NodePort | Dynamically assigned | Port used to access the Service externally |

The NodePort is assigned by Kubernetes and may differ between environments. Use the URL returned by `minikube service flask-app-service --url` rather than assuming a fixed port.

### Important Configuration

| Component | Configuration |
|---|---|
| Service type | `NodePort` |
| Container image | `flask-app:latest` |

The Kubernetes Service forwards incoming requests to the Flask application running inside the Pod.

## Key Concepts

- **Docker Image:** Packages the application, Python runtime, and required dependencies.
- **Container:** A running instance of the Docker image.
- **Pod:** The Kubernetes unit that hosts the application container.
- **Deployment:** Maintains the desired number of Pods and replaces failed Pods when necessary.
- **NodePort Service:** Exposes the application through a port accessible using the Minikube Service URL.
- **Image Availability:** Building the image inside Minikube makes it available to the cluster without requiring a Docker Hub push.

## Expected Output

A successful request returns:

```text
Hello hi from Flask on Kubernetes!
```

## Result

The Flask application was containerized using Docker, deployed on Minikube through Kubernetes resources, exposed using a NodePort Service, and verified using `curl`.
