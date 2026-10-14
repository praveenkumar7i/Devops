# Exercise 7 - Jenkins CI Automation

## Objective
Understand Continuous Integration (CI) and install Jenkins using Docker.

## Requirements
- Docker Desktop
- VS Code
- Web browser

## Step 1: Verify Docker
```powershell
docker --version
docker info
```

## Step 2: Download and start Jenkins
```powershell
docker run -d --name jenkins -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts
```

## Step 3: Check the container
```powershell
docker ps -a
docker logs jenkins
```

## Step 4: Retrieve the initial administrator password
```powershell
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

## Step 5: Open Jenkins
http://localhost:8080/

Enter the initial administrator password in the Jenkins setup page and follow the installation wizard.

## Step 6: Verify Jenkins
Confirm that the Jenkins dashboard opens successfully.

## Stop and restart Jenkins
```powershell
docker stop jenkins
docker start jenkins
```

## Remove the container when no longer needed
```powershell
docker stop jenkins
docker rm jenkins
```

Note: Removing the container may remove Jenkins data unless it is stored in a persistent volume.

---

## 📸 Jenkins Installation Screenshots from the Original Exercise

### 1. Jenkins Initial Password Unlock

![Jenkins Initial Password Unlock](https://github.com/user-attachments/assets/1902e321-ac1b-4187-a046-ca996ddd546a)

### 2. Jenkins Getting Started

![Jenkins Getting Started](https://github.com/user-attachments/assets/dff9c748-31cd-42f9-adee-3a5c5b317779)

### 3. Jenkins Landing Page

![Jenkins Landing Page](https://github.com/user-attachments/assets/42839e8e-a592-4d1d-95a0-825ce3849970)

---
