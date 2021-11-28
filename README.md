# CS1660 - Course Project - Option 1 (CHM171)
## Video (might have to press unmute button):


https://user-images.githubusercontent.com/42789465/143763598-36d0fffc-4b41-49e5-a09e-8c45fc7fea58.mp4




## Steps to running the application
- Before setting up any of the applications, you must clone this repo to get the dependent files.
- After cloning the repo, `cd` into the directory. 

### GUI Driver Set Up:
- `cd terminal` to change into the terminal directory. This directory contains all the necessary files for creating and containerizing the GUI application.
- Once in the directory, run `docker-compose up` and the GUI Flask application should start and will be exposed on port 5000.
- To connect to the application, open a web browser and go to `http://{host_ip}:5000`. The host ip will most likely be localhost.  

Note: It is most practicaly to set this up last because you want your applications to be started up before your driver.

### Jupyter Notebook Set Up (jupyter/scipy-notebook on Docker Hub):
- In your terminal, run `docker pull jupyter/scipy-notebook` to pull the Jupyter image.
- Next, you need to get the image id. We can do this by doing the following command: `docker images`. Then, copy the image id.
- To finally run the notebook, run `docker run -p 8888:8888 jupyter/scipy-notebook:{image_id}` and paste your image id that you copied earlier into the spot where it says `{image_id}`.
- Once started, the GUI driver will be able to connect to the application by clicking on the link for Jupyter Notebook.

### Apache Spark Set Up (bitnami/spark image on Docker Hub):
- To run Apache Spark, simply `cd spark` and then run `docker-compose up` which should start both the spark master and spark worker.
- Once started, the application can be started by clicking the link for Apache Spark in the GUI.  
Note: Since I have not implemented Kubernetes, Spark will sometimes go down and will need to be manually restarted. Kubernetes would typically restart a failing pod, but we have to do this manually, which is really annoying. To restart, just delete the container and image, then rerun the `docker-compose up`.

### Apache Hadoop Set Up (Uses multiple images from https://github.com/big-data-europe/docker-hadoop on GitHub):
- To run Apache Hadoop, run `cd hadoop` and then run `docker-compose up` which should start all the services defined in the docker-compose file. The environment variables are all predefined in the hadoop.env file and configured in the docker-compose file. 
- Once started, you can connect to the Hadoop web interface by clicking on the Apache Hadoop link on the GUI.
Note: Hadoop might also go down at some point, but what's nice about Hadoop is that it usually will restart itself unlike Spark. If for some reason Hadoop doesn't restart on it's own, then delete the container and images and then rerun the docker-compose command. If Hadoop goes down for a second, you will get a browser error when trying to connect to it via the GUI, but it should tell you that it's most likely because it is starting.

### Sonar Set Up (from sonarqube):
- Run `docker pull sonarqube` in the terminal to pull the base SonarQube image.
- To run application, run the command `docker run -d --name sonarqube -p 9000:9000 -p 9092:9092 sonarqube` and then Sonar should be started.  

**Note: Because of the issue of me not being able to run this on my M1 Mac, I had to do it on a Windows PC in Ubuntu. I wasn't able to test if there were any conflicts because of this. However it looks like SonarQube and the Hadoop namenode share the same port number, so you might need to change one of them to get them to work simultaneously. I would recommend changing the port on SonarQube. If you end up changing any of the ports, then you MUST change the port in the link for the application in the `app.py` file for the GUI driver. After changing the port in the link, you must delete the container and image for the GUI and rerun the docker-compose command.**
---
Estimated Grade:
- Containerized the four applications: 50%
- Deploy on Kubernetes Cluster: 0% X
- Deploy Kubernetes Cluster to GCP: 0% X
- Bonus GUI for Driver: 20%
- Bonus Milestone: 9%   
-------------------------------------------
Total: ~79%
