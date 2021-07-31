* Task 1:  Build a Dockerfile to create an image for this app.  
  * You'll need to:
    * Start from the python:3.8.3 base image 
    * Copy your current directory (.) into the /app directory on the container and set your working directory to the /app directory 
    * Install requirements.txt with pip 
    * Start the app by running `python flaskapp.py`
* Task 2:  Build a kubernetes manifest that will create a deployment for the simple application above and a service to refer users to the app. 
  * HINTs:  
    * The application will serve on container port 5000 by default.  
    * You will need to set ImagePullPolicy: Never for the container in your manifest and run `eval $(minikube docker-env)` to allow minikube to use your local image instead of one from dockerhub  
    * Important:  Be sure to run eval `eval $(minikube docker-env -u).` when we are done with this exercise to reset your docker daemon
* Task 3:  Build a Helm chart to deploy k8s infrastructure you just wrote manifests for.  Make at least one parameter configurable with values.yaml

When we come back to the main session, each group will share how they solved the problem and we'll walk through what it would take to deploy this solution with Jenkins.
