# MLops-assignment
Steps to docker containerization:

1. Create a folder, place the ML model in it.
2. Write a Dockerfile to install dependencies, and run the python file.
3. Run the following commands one by one :
    docker build -t mlops
   docker run mlops
4. Docker image has been created.
5. Create a repository in your Docker Hub account.
6. Now push the docker image to docker hub using the following commands:
    #Create a tag
   docker tag IMAGE_ID REPOSITORY: TAG
    #Push the image
   docker push IMAGE_ID REPOSITORY: TAG
7. Docker image has been succesfully pushed to Docker Hub
   
Steps to deploy Docker image on AWS EC2:

1. Create an EC2 instance with Ubuntu OS.
2. Connect to the instance using EC2 Instance Connect.
3. Run the commands found on https://docs.docker.com/engine/install/ubuntu/ to install docker on EC2 instance.
4. Login as root user, search the docker hub for the previously created image using the command:
    docker search sathwikk17/mlops
5. Pull the docker image using the command:
    docker pull sathwikk17/mlops:mlops
6. Result is displayed.
