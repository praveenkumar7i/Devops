# Exercise 7 - Jenkins CI Automation

## 📌 Exercise Overview

| Detail | Description |
|---|---|
| Exercise Number | 7 |
| Exercise Title | Introduction to Continuous Integration (CI) and Jenkins Installation |
| Category | DevOps / CI Automation |
| Main Tool | Jenkins |
| Container Platform | Docker |
| Access URL | http://localhost:8080/ |
| Repository Folder | `Exercises/exercise-7-Jenkins-CI-Automation` |

---

## 🎯 Objective

To understand Continuous Integration (CI), learn the fundamentals of Jenkins automation, and install and run Jenkins inside a Docker container.

## 📖 Introduction

Continuous Integration is a software development practice in which developers frequently integrate their code changes into a shared repository. The purpose is to identify integration problems early and improve software quality.

Jenkins is an open-source automation server that helps automate software building, testing, and delivery tasks. It supports CI and Continuous Delivery through jobs, pipelines, plugins, and distributed build execution.

In this exercise, Jenkins is started using the official Jenkins Long-Term Support Docker image and accessed through a web browser.

## 🎓 Learning Outcomes

After completing this exercise, you should be able to:

- Explain Continuous Integration and its purpose.
- Identify the main features and benefits of CI.
- Describe a basic CI workflow.
- Recognize commonly used CI/CD tools.
- Explain Jenkins jobs, builds, pipelines, plugins, and nodes.
- Run Jenkins using Docker.
- Inspect container status, port mappings, and startup logs.
- Access the Jenkins web interface through port 8080.

---

## 🛠️ Requirements

| Component | Purpose |
|---|---|
| Windows 10/11 | Host operating system |
| Visual Studio Code | Terminal and documentation editor |
| PowerShell | Execute Docker and verification commands |
| Docker Desktop | Run Jenkins in a container |
| Internet connection | Download the Jenkins image and load online references |
| Web browser | Open the Jenkins interface |
| `jenkins/jenkins:lts` | Jenkins Long-Term Support container image |

### Prerequisite Verification

Open the VS Code PowerShell terminal and run:

```powershell
docker --version
docker info
```

**Expected result:** Docker displays its version and information about the running Docker Engine.

---

## 🧠 Part 1: Understanding Continuous Integration

### 1.1 What is Continuous Integration?

Continuous Integration (CI) is a development practice where developers frequently integrate their code changes into a shared repository. Automated builds and tests can validate these changes and help detect errors early.

### 1.2 Key Features of CI

| Feature | Explanation |
|---|---|
| Frequent Code Integration | Developers regularly commit changes to a shared repository. |
| Automated Builds | A configured CI system builds the code when changes trigger a build. |
| Automated Testing | Automated tests check whether the software continues to behave correctly. |
| Immediate Feedback | Developers receive build and test results so they can address failures. |

### 1.3 Benefits of CI

| Benefit | Explanation |
|---|---|
| Early Bug Detection | Integration problems can be identified before they become harder to fix. |
| Improved Collaboration | Team members integrate changes into a shared codebase. |
| Faster Development Cycles | Automated tasks reduce repetitive manual work. |
| Improved Software Quality | Regular testing helps detect regressions. |

### 1.4 How CI Works

| Stage | Activity |
|---|---|
| 1. Code Change | A developer writes or updates code. |
| 2. Repository Update | The developer pushes the changes to a version control system such as Git. |
| 3. Build Trigger | A configured CI server detects the change or receives a build trigger. |
| 4. Automated Build | The system builds the application and resolves required dependencies. |
| 5. Automated Testing | Configured tests run to validate the changes. |
| 6. Feedback | Build and test results are reported to the team. |

### 1.5 Basic CI Workflow

```text
Developer writes code
        |
        v
Push changes to Git repository
        |
        v
CI server triggers a build
        |
        v
Build and automated tests
        |
        v
Success or failure feedback
```

**Note:** This diagram explains the general CI workflow. The steps above do not mean that a new automated pipeline was configured during this installation exercise.

---

## 🔧 Part 2: Overview of CI/CD Tools

The original exercise introduces the following tools.

| No. | Tool | Main Characteristics | Common Use |
|---:|---|---|---|
| 1 | GitLab CI/CD | Integrated with GitLab; supports YAML pipeline definitions and Auto DevOps. | Teams using GitLab repositories. |
| 2 | CircleCI | Cloud-based CI service with container support, caching, and parallel execution. | Container-based workflows. |
| 3 | Travis CI | CI service supporting configuration files and integration with source repositories. | Automated builds and tests. |
| 4 | Bamboo | Atlassian CI/CD tool with build and deployment capabilities. | Teams using the Atlassian ecosystem. |
| 5 | TeamCity | JetBrains CI/CD server with build history, reports, and integrations. | Complex build and testing workflows. |
| 6 | Azure DevOps Pipelines | Supports YAML and visual pipeline configuration across platforms. | Teams using Azure DevOps. |
| 7 | GitHub Actions | Automates repository workflows using YAML files and reusable actions. | GitHub-based automation. |
| 8 | Spinnaker | Focuses on application delivery and deployment across cloud environments. | Cloud deployment workflows. |
| 9 | Buildkite | Combines hosted pipeline management with agents running on your infrastructure. | Custom or self-hosted build environments. |
| 10 | Drone | Container-oriented CI/CD platform with configurable pipeline steps. | Container-based automation. |

Jenkins is the main tool used in this exercise.

---

## ⚙️ Part 3: Introduction to Jenkins

### 3.1 What is Jenkins?

Jenkins is an open-source automation server used to automate software development tasks such as building, testing, and deploying applications.

### 3.2 Why Use Jenkins?

| Feature | Explanation |
|---|---|
| Automation | Reduces repetitive manual development tasks. |
| Continuous Integration | Supports validation of frequently integrated code changes. |
| Extensibility | Plugins add support for additional tools and services. |
| Distributed Execution | Agents can execute jobs on different machines. |

### 3.3 Key Jenkins Concepts

| Concept | Explanation | Example |
|---|---|---|
| Job / Project | A configured task that Jenkins executes. | Build an application. |
| Build | A single execution of a job or pipeline. | Build #1 or Build #2. |
| Pipeline | A sequence of automated stages and steps. | Build, test, and package. |
| Plugin | An extension that adds functionality to Jenkins. | Git integration. |
| Node | A machine or execution environment used to run jobs. | Controller or agent machine. |

---

## 🐳 Part 4: Running Jenkins Using Docker

### 4.1 Why Docker?

Docker runs Jenkins inside an isolated container. This allows Jenkins to run without installing the Jenkins server directly on the Windows host.

### 4.2 Start Jenkins

The original exercise uses this command:

```powershell
docker run -d --name jenkins -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts
```

### 4.3 Command Breakdown

| Command / Option | Purpose |
|---|---|
| `docker run` | Creates and starts a container. |
| `-d` | Runs the container in the background. |
| `--name jenkins` | Assigns the container the name `jenkins`. |
| `-p 8080:8080` | Maps host port 8080 to container port 8080 for the web interface. |
| `-p 50000:50000` | Maps port 50000 for inbound Jenkins agent connections. |
| `jenkins/jenkins:lts` | Selects the Jenkins Long-Term Support image. |

**Important:** If the `jenkins` container already exists, do not run the creation command again with the same name. Start the existing container instead.

```powershell
docker start jenkins
```

If Docker reports that the container is already running, continue with the verification steps.

### 4.4 Verify the Container

```powershell
docker ps -a --filter "name=jenkins"
```

Inspect the output and confirm:

- The container name is `jenkins`.
- The container is running and its status shows `Up`.
- The port mappings include `8080` and `50000`.

### 4.5 Inspect Jenkins Logs

```powershell
docker logs --tail 50 jenkins
```

**Expected result:** The logs show Jenkins startup activity and, once initialization completes, a message indicating that Jenkins is fully up and running.

### 4.6 Verify Port Connectivity

```powershell
Test-NetConnection localhost -Port 8080
```

**Expected result:** `TcpTestSucceeded` displays `True` when the port is reachable.

---

## 🔐 Part 5: Initial Jenkins Setup

### 5.1 Retrieve the Initial Administrator Password

During the first-time setup, run:

```powershell
docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
```

Copy the displayed password into the Jenkins unlock page.

**Important:** The password file is intended for initial setup. Since the Jenkins instance used in this exercise has already been initialized, this file may no longer be available. Do not reset the existing instance or publish administrator credentials.

### 5.2 Complete the Setup Wizard

For a new Jenkins installation:

| Step | Action |
|---:|---|
| 1 | Open the Jenkins unlock page. |
| 2 | Enter the initial administrator password. |
| 3 | Select **Install suggested plugins**. |
| 4 | Wait for the plugins to install. |
| 5 | Create an administrator account. |
| 6 | Complete the setup wizard. |

If Jenkins has already been configured, sign in using the existing account and open the dashboard instead.

---

## 🌐 Part 6: Access the Jenkins Dashboard

### 6.1 Open Jenkins

Run this command in PowerShell:

```powershell
Start-Process "http://localhost:8080/"
```

Alternatively, enter the URL directly into your browser:

**http://localhost:8080/**

### 6.2 Expected Result

The Jenkins web interface should load. For an initialized installation, the dashboard should display the available Jenkins jobs and navigation options.

### 6.3 Port Reference

| Port | Purpose |
|---:|---|
| `8080` | Jenkins web interface |
| `50000` | Inbound Jenkins agent connections when configured |

---

## 📸 Part 7: Jenkins Installation Screenshots

The following three images are the reference screenshots included in the original exercise document.

### 7.1 Jenkins Initial Password Unlock

![Jenkins Initial Password Unlock](https://github.com/user-attachments/assets/1902e321-ac1b-4187-a046-ca996ddd546a)

### 7.2 Jenkins Getting Started

![Jenkins Getting Started](https://github.com/user-attachments/assets/dff9c748-31cd-42f9-adee-3a5c5b317779)

### 7.3 Jenkins Landing Page

![Jenkins Landing Page](https://github.com/user-attachments/assets/42839e8e-a592-4d1d-95a0-825ce3849970)

**Screenshot note:** These are reference images from the source document, not screenshots captured from the current computer. They are embedded using online URLs. Store your own execution screenshots in the `Images/` folder if you want to document your local results.

---

## ✅ Part 8: Verification Summary

| No. | Verification | Command / Action | Expected Result |
|---:|---|---|---|
| 1 | Docker installation | `docker --version` | Docker version is displayed. |
| 2 | Docker Engine | `docker info` | Engine information is displayed. |
| 3 | Jenkins container | `docker ps -a --filter "name=jenkins"` | Jenkins container is listed. |
| 4 | Container status | Inspect the `STATUS` column. | Container shows `Up` when running. |
| 5 | Startup logs | `docker logs --tail 50 jenkins` | Jenkins startup information is displayed. |
| 6 | Port connectivity | `Test-NetConnection localhost -Port 8080` | `TcpTestSucceeded` is `True`. |
| 7 | Browser access | Open `http://localhost:8080/` | Jenkins interface loads. |

---

## 🧹 Part 9: Container Management

### Stop Jenkins

```powershell
docker stop jenkins
```

### Start Jenkins Again

```powershell
docker start jenkins
```

### Check Container Status

```powershell
docker ps -a --filter "name=jenkins"
```

### View Recent Logs

```powershell
docker logs --tail 50 jenkins
```

**Note:** Stopping a container does not delete it. Avoid removing the existing container unless you understand how its Jenkins data is stored.

---

## 📁 Part 10: Exercise Folder Structure

The documented installation exercise does not require separate application source code.

```text
exercise-7-Jenkins-CI-Automation/
├── README.md
└── Images/
    └── (optional local execution screenshots)
```

| Item | Purpose |
|---|---|
| `README.md` | Exercise documentation, commands, concepts, and verification steps. |
| `Images/` | Optional folder for screenshots captured during execution. |

A separate `Jenkinsfile`, application source file, or custom `Dockerfile` is not required by the installation steps in the original exercise document.

---

## 🏁 Result

Jenkins was run using Docker and accessed through the browser at `http://localhost:8080/`. Container status, startup logs, and port connectivity were used to verify that the service was running.

## 📝 Conclusion

This exercise introduced Continuous Integration, its key features and benefits, common CI/CD tools, and the fundamental concepts of Jenkins. It also demonstrated how to run Jenkins using Docker, inspect its container, and access the web interface.

The exercise establishes the Jenkins environment needed to explore further automation tasks. Creating a separate Jenkins pipeline or configuring automated application builds would be a subsequent implementation task, not a result claimed by this installation exercise.

---

**DevOps Laboratory | Practical Learning & Implementation**
