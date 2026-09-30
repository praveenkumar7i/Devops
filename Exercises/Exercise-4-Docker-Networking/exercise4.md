# Docker Multi-Container Networking

## Overview

This exercise demonstrates how to containerize a Flask REST API and connect it with MySQL and Redis using a custom Docker bridge network.

### Technologies Used

* Docker
* Flask
* MySQL
* Redis
* Docker Bridge Network

---

## 1. Build the Flask Docker Image

Build the Docker image using the existing `Dockerfile`:

```bash
docker build -t flask-api .
```

The image is successfully created as:

```text
flask-api:latest
```

---

## 2. Run the Flask API Container

Run the Flask application and map port `5001` on the host to port `5001` inside the container:

```bash
docker run -d --name flask-test -p 5001:5001 flask-api
```

Verify the API:

```bash
curl.exe http://localhost:5001/about
```

Response:

```json
{
  "description": "This is a simple REST API built with Flask.",
  "name": "Simple REST API",
  "version": "1.0"
}
```

---

## 3. Create MySQL and Redis Containers

Both services are connected to the same custom Docker network.

### MySQL

```bash
docker run -d --name mysql \
  --network my-bridge-net \
  -e MYSQL_ROOT_PASSWORD=rootpass \
  -e MYSQL_DATABASE=devopsdb \
  mysql:latest
```

### Redis

```bash
docker run -d --name redis \
  --network my-bridge-net \
  redis:latest
```

---

## 4. Inspect the Docker Network

```bash
docker network inspect my-bridge-net
```

The network uses the Docker `bridge` driver.

Example network configuration:

```text
Network: my-bridge-net
Driver: bridge
Subnet: 172.19.0.0/16
Gateway: 172.19.0.1
```

The containers receive IP addresses from this network.

| Container | IP Address   |
| --------- | ------------ |
| MySQL     | `172.19.0.2` |
| Redis     | `172.19.0.3` |

---

## 5. Connect Flask to the Custom Network

Remove the initial Flask container:

```bash
docker rm -f flask-test
```

Run Flask on `my-bridge-net`:

```bash
docker run -d \
  --name flask \
  --network my-bridge-net \
  -p 5001:5001 \
  flask-api
```

Verify the running containers:

```bash
docker ps
```

The final setup contains:

```text
flask
mysql
redis
```

---

## 6. Verify Flask API

```bash
curl.exe http://localhost:5001/about
```

Response:

```json
{
  "description": "This is a simple REST API built with Flask.",
  "name": "Simple REST API",
  "version": "1.0"
}
```

Port mapping can also be verified with:

```bash
docker port flask
```

Output:

```text
5001/tcp -> 0.0.0.0:5001
5001/tcp -> [::]:5001
```

---

## 7. Verify Container-to-Container Communication

Open a shell inside the Flask container:

```bash
docker exec -it flask bash
```

Install the ping utility:

```bash
apt-get update
apt-get install -y iputils-ping
```

### Test MySQL Connectivity

```bash
ping -c 3 mysql
```

Result:

```text
3 packets transmitted, 3 received, 0% packet loss
```

### Test Redis Connectivity

```bash
ping -c 3 redis
```

Result:

```text
3 packets transmitted, 3 received, 0% packet loss
```

This confirms that the Flask container can communicate with both MySQL and Redis through the custom Docker network.

---

## 8. Verify Docker DNS Resolution

Docker's internal DNS allows containers to communicate using container names instead of IP addresses.

```bash
getent hosts mysql
getent hosts redis
```

Output:

```text
172.19.0.2      mysql
172.19.0.3      redis
```

Exit the Flask container:

```bash
exit
```

---

## 9. Verify Redis

Test Redis using its CLI:

```bash
docker exec -it redis redis-cli ping
```

Output:

```text
PONG
```

---

## 10. Verify MySQL

Check the databases created inside MySQL:

```bash
docker exec -it mysql mysql -uroot -prootpass -e "SHOW DATABASES;"
```

Output:

```text
+--------------------+
| Database           |
+--------------------+
| devopsdb           |
| information_schema |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
```

The `devopsdb` database was successfully created.

---

## 11. Final Architecture

```text
                         Host Machine
                              |
                              |
                       Port 5001:5001
                              |
                              v
                     +----------------+
                     |   Flask API    |
                     |    flask       |
                     |   172.19.0.4   |
                     +----------------+
                              |
                    Docker Bridge Network
                       my-bridge-net
                              |
              +---------------+---------------+
              |                               |
              v                               v
       +--------------+                +--------------+
       |    MySQL     |                |    Redis     |
       |    mysql     |                |    redis     |
       |  172.19.0.2  |                |  172.19.0.3  |
       +--------------+                +--------------+
```

---

## 12. Key Concepts Demonstrated

### Docker Image

The Flask application was packaged into a Docker image:

```text
flask-api:latest
```

### Port Mapping

```text
Host Port 5001 → Container Port 5001
```

This allows the Flask API to be accessed from the host machine.

### Custom Bridge Network

```text
my-bridge-net
```

The custom network allows the Flask, MySQL, and Redis containers to communicate with each other.

### Container Name Resolution

Instead of using IP addresses, containers can communicate using their names:

```text
mysql
redis
flask
```

For example:

```bash
ping mysql
ping redis
```

### Multi-Container Architecture

The final setup consists of:

```text
Flask → Application/API
MySQL → Database
Redis → Cache
Docker Bridge Network → Container Communication
```

---

## Result

The Flask REST API was successfully containerized and connected to MySQL and Redis through a custom Docker bridge network.

The following were successfully verified:

* Flask API accessibility through port `5001`
* MySQL container operation
* Redis container operation
* Custom bridge network
* Container-to-container connectivity
* Docker DNS-based service discovery
* MySQL database creation
* Redis connectivity
