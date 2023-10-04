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
   
