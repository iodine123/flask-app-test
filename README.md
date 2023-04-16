# flask-app-test

## Build and Deploying Concept

### Context

#### 1. Technology Used
On this project I made simple python script to call an api to get information about most popular article from New York Times api. I am also created a unit test file to test the api. 
The application will be build as a docker image, then push that image to the heroku container registry and then that image that exist on registry will be used to deploy the
application to the Heroku server.
#### 2. Dockerfile
To build this program as a docker image we have to create a file called "Dockerfile" that explain the way how to build the program. On this file there are some instruction
that will be excecute on the machine. I used alpine for the base image, copy the source code to the container, install the library that needed to run the program, create 
a user to run the service, and then run the service with gunicorn.
#### 3. Heroku
To deploy the application on the Heroku we have to push the images to the Heroku container registry and run some instruction with Heroku CLI. If the images already pushed to
the container registry we just need to release that image and the heroku will automatically run the container service from that image and we can access application on
https://flask-trial.herokuapp.com/. If the process run without error we will see our appliction run on that server.
#### 4. Automation with Jenkins ( using Jenkinsfile )
To automate the process I used jenkins. Before start the Pipeline we have to setup some dependencies that needed to excecute or run the instruction on jenkins pipeline. We have to install
docker and Heroku CLI on the jenkins machine, we can access the jenkins bash with
instruction "docker exec -ti -u 0 bash". Then allow the permission to the docker.sock on /var/run/docker.sock, because the jenkins did'nt run the service as a root. 
So, we have to change permission to allow the user to excecute the docker instruction. Then login to the heroku cli on the jenkins service. Then we just need to run heroku login and follow the instruction to login on our heroku accounts. If all the process run as well,
finally we can run the pipeline on jenkins. On this project the workflow is start from the push action from developer, then jenkins will download the source code from the
guthub repository, then test the api, then build the image from Dockerfile, push the image to heroku container registry, and the last instruction is release the container
images. 

### Heroku Link
https://flask-trial.herokuapp.com/
