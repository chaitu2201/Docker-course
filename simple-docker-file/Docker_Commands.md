## Basic Docker Commands 

1. To see all the images present in your local Machine 
      docker images
   
2. To findout the imagesi n Docker hub
      docker search image1
   
3. To Download image form docker hub to local machine
      docker pull ubuntu
   
4. To Run and give name to container
      docker run -it --name "contaier123" ubuntu /bin/bash

5. To check service is start or not
      Service docker status

6. To start a container
      docker start container123
   
7. To go inside a container
      docker attach container123
   
8. To see all Containers
      docker ps -a
9. To see only running containers
      docker ps
    
10. To stop a Container
     docker stop container123
    
11. To Delete a Container
     docker rm container123
        
      
