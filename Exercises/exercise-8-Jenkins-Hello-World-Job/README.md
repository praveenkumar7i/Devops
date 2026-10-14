# Exercise 8: Creating a Hello World Jenkins Job

## 1. Objective

The objective of this exercise is to create and execute a simple Jenkins Freestyle job that runs a shell script stored in a GitHub repository.

This exercise demonstrates how Jenkins retrieves source code from GitHub, executes a build step, and displays the execution results in the Console Output.

## 2. Overview

Jenkins is an automation server used to automate software development tasks, including building, testing, and deploying applications.

In this exercise, a shell script named `hello-world.sh` prints the message `Hello, Jenkins!`. The script is stored in GitHub, and Jenkins is configured to retrieve and execute it.

### Workflow

1. Create the shell script locally.
2. Create a GitHub repository and upload the script.
3. Configure a Jenkins Freestyle project.
4. Connect Jenkins to the GitHub repository.
5. Configure the build step to execute the shell script.
6. Run the Jenkins job and verify the output.

## 3. Tools and Technologies

| Tool / Technology | Purpose |
|---|---|
| Visual Studio Code | Create and edit the shell script and README documentation. |
| Git | Track changes, commit files, and push changes to GitHub. |
| GitHub | Store and manage the source code in a remote repository. |
| Jenkins | Automate the execution of the shell script through a Freestyle job. |
| Bash / Shell | Execute the script that prints the greeting message. |
| Web Browser | Access and configure the Jenkins dashboard. |

## 4. Prerequisites

Before starting the exercise, ensure that the following requirements are satisfied:

- Git is installed and configured on the system.
- A GitHub account is available.
- A GitHub repository has been created for the exercise.
- Jenkins is installed and running.
- The Jenkins dashboard is accessible through a web browser.
- Jenkins has the necessary Git support to retrieve the repository.
- The machine or container executing the job supports the configured shell build step.

## 5. Project Structure

The Exercise 8 directory contains the following files:

```text
exercise-8-Jenkins-Hello-World-Job/
├── hello-world.sh
└── README.md
```

| File | Description |
|---|---|
| `hello-world.sh` | Shell script executed by Jenkins. |
| `README.md` | Documentation describing the objective, configuration, execution, and expected results. |

## 6. Implementation

### Step 1: Create the Shell Script

Create a file named `hello-world.sh` with the following content:

```bash
#!/bin/bash
echo "Hello, Jenkins!"
```

**Explanation:**

- `#!/bin/bash` specifies Bash as the interpreter for the script.
- `echo` prints the specified text to standard output.
- `Hello, Jenkins!` is the message displayed when the script executes successfully.

### Step 2: Create a GitHub Repository

Create a repository on GitHub to store the shell script.

The exercise instructions suggest the following repository details:

| Setting | Value |
|---|---|
| Repository name | `devops-sample-code` |
| Description | A demo repository for Jenkins scripting |
| Visibility | Public |
| Main file | `hello-world.sh` |

If the script is stored in an existing repository instead, use that repository's URL and the correct path to the script when configuring Jenkins.

### Step 3: Push the Script to GitHub

Use Git to stage, commit, and push the script to the remote repository.

Example commands when working inside a newly initialized local repository:

```bash
git init
git add hello-world.sh
git commit -m "Add hello-world.sh"
git branch -M main
git remote add origin https://github.com/<your-username>/devops-sample-code.git
git push -u origin main
```

Replace `<your-username>` with your GitHub username.

If you are using an existing Git repository, do not run `git init` or add another remote unnecessarily. Stage and push the required files using the existing repository configuration.

### Step 4: Access Jenkins

1. Open a web browser.
2. Navigate to `http://localhost:8080`, or use your configured Jenkins URL.
3. Log in with your Jenkins credentials.
4. Verify that the Jenkins dashboard is accessible.

### Step 5: Create a Freestyle Job

1. Click **New Item** on the Jenkins dashboard.
2. Enter the job name `HelloWorld`.
3. Select **Freestyle project**.
4. Click **OK** to open the job configuration page.

### Step 6: Configure Source Code Management

1. Find the **Source Code Management** section.
2. Select **Git**.
3. Enter the GitHub repository URL.
4. Configure credentials if required for a private repository.
5. Specify the correct branch, such as `*/main`, if necessary.

For example:

```text
https://github.com/<your-username>/devops-sample-code.git
```

Jenkins will use this configuration to retrieve the repository's source code for the job.

### Step 7: Configure the Build Step

1. Navigate to the **Build Steps** section.
2. Click **Add build step**.
3. Select **Execute shell**.
4. Enter the appropriate command for the repository layout.

If `hello-world.sh` is located at the root of the repository:

```bash
sh hello-world.sh
```

If using the existing DevOps repository with the script inside the Exercise 8 directory:

```bash
sh Exercises/exercise-8-Jenkins-Hello-World-Job/hello-world.sh
```

Save the configuration.

**Note:** The build command must match the actual location of the script in the repository Jenkins checks out. The Execute shell option requires an environment capable of running shell commands, such as a Linux-based Jenkins agent.

### Step 8: Run the Jenkins Job

1. Open the `HelloWorld` job.
2. Click **Build Now**.
3. Wait for the build to finish.
4. Open the corresponding build number in **Build History**.
5. Click **Console Output** to inspect the logs.

## 7. Expected Output

The Console Output should contain a message similar to the following:

```text
Started by user Admin
Building in workspace /var/jenkins_home/workspace/HelloWorld
[HelloWorld] $ /bin/sh -xe /tmp/jenkins-script.sh
+ echo 'Hello, Jenkins!'
Hello, Jenkins!
Finished: SUCCESS
```

The workspace path and temporary script name may differ depending on the Jenkins installation and configuration.

### Result Verification

| Verification Item | Expected Result |
|---|---|
| Jenkins job | `HelloWorld` |
| Build execution | Completed |
| Script output | `Hello, Jenkins!` |
| Final build status | `SUCCESS` |

## 8. Troubleshooting

| Problem | Possible Cause | Suggested Action |
|---|---|---|
| Jenkins dashboard does not open | Jenkins is not running or the URL/port is incorrect. | Start Jenkins and verify the configured URL and port. |
| Git repository checkout fails | Incorrect repository URL, branch, or credentials. | Verify the repository URL, branch, and required credentials. |
| Script file not found | The build command uses an incorrect relative path. | Check the repository structure and update the command. |
| Permission denied | The script lacks execution permission or the environment restricts execution. | Check permissions or invoke the script with `sh hello-world.sh` where appropriate. |
| Execute shell is unavailable | The selected Jenkins agent or installation does not support the configured build step. | Use a compatible Linux agent or configure the appropriate execution environment. |
| Build fails | A configuration or execution error occurred. | Open Console Output and inspect the error message. |

## 9. Learning Outcomes

After completing this exercise, the following concepts should be understood:

- Creating a shell script for a basic automation task.
- Using Git to track and upload source code.
- Storing source code in a GitHub repository.
- Creating and configuring a Jenkins Freestyle project.
- Connecting Jenkins to a Git repository.
- Executing shell commands through a Jenkins build step.
- Inspecting Console Output to verify build execution.
- Identifying and troubleshooting common Jenkins job errors.

## 10. Conclusion

This exercise demonstrates the basic operation of a Jenkins Freestyle job. A shell script is stored in GitHub, retrieved by Jenkins, and executed through a configured build step.

The exercise is successful when the Console Output displays `Hello, Jenkins!` and the build finishes with the status `SUCCESS`.

