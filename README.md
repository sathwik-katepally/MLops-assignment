# MLops-assignment

This project consists of 6 steps:
1. Setting up and using Github for version control.
2. Training an ML model for movie recommendation.
3. Dockerizing the ML model and pushing it to Docker Hub.
4. Deploying the dockerized ML model on an EC2 instance.
5. Setting up CircleCI for automated unit testing.

Steps to docker containerization:

1. Create a folder, place the ML model in it.
2. Write a Dockerfile to install dependencies, and run the python file.
3. Run the following commands one by one :  
    docker build -t mlops  
    docker run mlops  
5. Docker image has been created.
6. Create a repository in your Docker Hub account.
7. Now push the docker image to docker hub using the following commands:  
    #Create a tag  
   docker tag IMAGE_ID REPOSITORY: TAG  
    #Push the image  
   docker push IMAGE_ID REPOSITORY: TAG  
8. Docker image has been succesfully pushed to Docker Hub.

   Link to Docker image on Docker Hub : https://hub.docker.com/layers/sathwikk17/mlops/mlops/images/sha256-7725f39c6f3b7d91cb7c290813ffd142e23cd70f43ddf5216470fb153f711dda?context=repo
   
Steps to deploy Docker image on AWS EC2:

1. Create an EC2 instance with Ubuntu OS.
2. Connect to the instance using EC2 Instance Connect.
3. Run the commands found on https://docs.docker.com/engine/install/ubuntu/ to install docker on EC2 instance.
4. Login as root user, search the docker hub for the previously created image using the command:  
    docker search sathwikk17/mlops:mlops  
5. Pull the docker image using the command:  
    docker pull sathwikk17/mlops:mlops
6. Result is displayed.
<img width="726" alt="Screenshot 2023-10-05 at 12 14 16 AM" src="https://github.com/sathwik-katepally/MLops-assignment/assets/59343619/65b1ac77-fdd8-4805-8bee-2847ce3c1301">



Steps to automate tests using CircleCI:
1. Integrate CircleCI with Github and local machine (ssh keys).
2. Connect github repository with CircleCI.
3. Write test cases in a file named as tests.py
4. Edit config.yml file accordingly, to automate the workflow
5. Unit testing has now been automated successfully.


<img width="1505" alt="Screenshot 2023-10-05 at 1 33 16 AM" src="https://github.com/sathwik-katepally/MLops-assignment/assets/59343619/82611fe7-b035-4969-967a-d2ad21c997d9">
<img width="1512" alt="Screenshot 2023-10-05 at 1 37 40 AM" src="https://github.com/sathwik-katepally/MLops-assignment/assets/59343619/19357f42-66f7-4055-a8be-c33a8a7eeb4c">

