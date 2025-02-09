## Docker-course

## What is a Virtual Machine(VM)? 

A virtual machine is no different than any other physical computer like a laptop, smart phone, or server. It has a CPU, memory, disks to store your files, and can connect to the internet if needed. While the parts that make up your computer (called hardware) are physical and tangible, VMs are often thought of as virtual computers or software-defined computers within physical servers, existing only as code.

![image](https://github.com/user-attachments/assets/bcb2f9db-e491-4116-8a71-e036edb723ab)

## What is Hypervisor?

A hypervisor is a virtualization software that enables multiple virtual machines (VMs)—each with its own operating system (OS)—to run on one physical server. The hypervisor pools and allocates physical computing resources as needed by the VM, enabling efficiency, flexibility and scalability.It separates VMs from each other logically, assigning each its own slice of the underlying computing power, memory and storage. This prevents the VMs from interfering with each other. For example, if one OS suffers a crash or a security compromise, the others survive.


VM --------------- Advancement to physical servers 

Eg: Big Land 

## What is a server?

A server is a computer program or device that provides a service to another computer program and its user, also known as the client. The term server can refer to a physical machine, a virtual machine (VM) or software that's performing server services.In the client-server model, a server program fulfills requests from client programs, which might be running on the same computer or other computers.


A virtual server is a virtual representation of a physical server. Like a physical server, a virtual server includes its own OS and applications


<img width="722" alt="image" src="https://github.com/user-attachments/assets/bc97610d-88b2-4763-95ad-ea23e8df4d74" />

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## What is a container ?

A container is a bundle of Application, Application libraries required to run your application and the minimum system dependencies. A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings.

![image](https://github.com/user-attachments/assets/01ac8809-8e8e-4e47-8229-016104750403)

## Containers vs Virtual Machine
```
1. Resource Utilization: Containers share the host operating system kernel, making them lighter and faster than VMs. VMs have a full-fledged OS and hypervisor, making them more resource-intensive.
2. Portability: Containers are designed to be portable and can run on any system with a compatible host operating system. VMs are less portable as they need a compatible hypervisor to run.
3. Security: VMs provide a higher level of security as each VM has its own operating system and can be isolated from the host and other VMs. Containers provide less isolation, as they share the host operating system.
4. Management: Managing containers is typically easier than managing VMs, as containers are designed to be lightweight and fast-moving.
```

Containers are lightweight because they use a technology called containerization, which allows them to share the host operating system's kernel and libraries, while still providing isolation for the application and its dependencies. This results in a smaller footprint compared to traditional virtual machines, as the containers do not need to include a full operating system.

official ubuntu base image which you can use for your container. It's just ~ 22 MB, isn't it very small ? on a contrary if you look at official ubuntu VM image it will be close to ~ 2.3 GB. So the container base image is almost 100 times less than VM image.

Note: Contaiers are ephimeral in nature ie they are short lived..

## Files and Folders in containers base images

```

    /bin: contains binary executable files, such as the ls, cp, and ps commands.

    /sbin: contains system binary executable files, such as the init and shutdown commands.

    /etc: contains configuration files for various system services.

    /lib: contains library files that are used by the binary executables.

    /usr: contains user-related files and utilities, such as applications, libraries, and documentation.

    /var: contains variable data, such as log files, spool files, and temporary files.

    /root: is the home directory of the root user.

```

## Files and Folders that containers use from host operating system

```
    The host's file system: Docker containers can access the host file system using bind mounts, which allow the container to read and write files in the host file system.

    Networking stack: The host's networking stack is used to provide network connectivity to the container. Docker containers can be connected to the host's network directly or through a virtual network.

    System calls: The host's kernel handles system calls from the container, which is how the container accesses the host's resources, such as CPU, memory, and I/O.

    Namespaces: Docker containers use Linux namespaces to create isolated environments for the container's processes. Namespaces provide isolation for resources such as the file system, process ID, and network.

    Control groups (cgroups): Docker containers use cgroups to limit and control the amount of resources, such as CPU, memory, and I/O, that a container can access.
```

It's important to note that while a container uses resources from the host operating system, it is still isolated from the host and other containers, so changes to the container do not affect the host or other containers.

so, in a nutshell, container base images are typically smaller compared to VM images because they are designed to be minimalist and only contain the necessary components for running a specific application or service. VMs, on the other hand, emulate an entire operating system, including all its libraries, utilities, and system files, resulting in a much larger size.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
## Docker Begins

## What is Docker ?

Docker is a containerization platform that provides easy way to containerize your applications, which means, using Docker you can build container images, run the images to create containers and also push these containers to container regestries such as DockerHub, Quay.io and so on.

In simple words, you can understand as containerization is a concept or technology and Docker Implements Containerization.

Dockeris a set of platform as a service that uses OS level virtualization where as VMware uses Hardware level Virtualization. 

Docker is  open source centralized platform designed to create , deploy and run applications written in GO language.

Note: Docker was relased in Mar 2013 developed by solomon Hykes and Sebastain Patel.

## Docker Architecture ?

![image](https://github.com/user-attachments/assets/5445f545-a2bb-43c0-9491-a0903af5d82c)

## Docker LifeCycle

There are three important things,

1. docker build -> builds docker images from Dockerfile
2. docker run -> runs container from docker images
3. docker push -> push the container image to public/private regestries to share the docker images.

<img src="https://github.com/user-attachments/assets/213a4462-fa3f-4003-9622-e7d1c83da52e" width=50% height=50%>

## Understanding the terminology

## Docker daemon

The Docker daemon (dockerd) listens for Docker API requests and manages Docker objects such as images, containers, networks, and volumes. A daemon can also communicate with other daemons to manage Docker services.

## Docker client

The Docker client (docker) is the primary way that many Docker users interact with Docker. When you use commands such as docker run, the client sends these commands to dockerd, which carries them out. The docker command uses the Docker API. The Docker client can communicate with more than one daemon.

## Docker Desktop

Docker Desktop is an easy-to-install application for your Mac, Windows or Linux environment that enables you to build and share containerized applications and microservices. Docker Desktop includes the Docker daemon (dockerd), the Docker client (docker), Docker Compose, Docker Content Trust, Kubernetes, and Credential Helper. For more information, see Docker Desktop.


## Docker registries

A Docker registry stores Docker images. Docker Hub is a public registry that anyone can use, and Docker is configured to look for images on Docker Hub by default. You can even run your own private registry.

When you use the docker pull or docker run commands, the required images are pulled from your configured registry. When you use the docker push command, your image is pushed to your configured registry. Docker objects

When you use Docker, you are creating and using images, containers, networks, volumes, plugins, and other objects. This section is a brief overview of some of those objects.

   Eg: Docker registry , pay.io

## Dockerfile

Dockerfile is a set of instructions file to build your Docker Image that you share to Docker Daemon.


## Docker Images

An image is a read-only template with instructions for creating a Docker container. Often, an image is based on another image, with some additional customization. For example, you may build an image which is based on the ubuntu image, but installs the Apache web server and your application, as well as the configuration details needed to make your application run.

You might create your own images or you might only use those created by others and published in a registry. To build your own image, you create a Dockerfile with a simple syntax for defining the steps needed to create the image and run it. Each instruction in a Dockerfile creates a layer in the image. When you change the Dockerfile and rebuild the image, only those layers which have changed are rebuilt. This is part of what makes images so lightweight, small, and fast, when compared to other virtualization technologies.


## Advantages of Docker 

```

1. No Pre Allocation of RAM.

2. CI Efficency: Docker enables you to build container image and use the same image accross every step of the deployment process.

3. Less Cost and It is light in weight.

4. It can run on Physical H/W / virtual H/W or on cloud.

5. you can re-use the same image.

6. It will take less time to create a container.

```

## Limitations / Diasdvantages of Docker

```
1. Docker is not a good solution for application that rquired rich GUI.

2. Difficult to maange large amount of containers.

3. Docker does not provide Cross-Platform compatability ie if an application is designed to run a docker container on windows, then it can't run linux , vice versa.

4. Docker is suitable when development OS and testing OS are same if OS is different, we should use VM.

5. No Solution for Data Recovery and Backup.

```
## Difference between Github and Dockerhub 

Github is version control Platform used to store source code.

Dockerhub is also a version control platform to store Docker images.

## INSTALL DOCKER

```
sudo apt update
sudo apt install docker.io -y

```

## Start Docker and Grant Access

After they install docker using the sudo access, they miss the step to Start the Docker daemon and grant acess to the user they want to use to interact with docker and run docker commands.

Always ensure the docker daemon is up and running.

A easy way to verify your Docker installation is by running the below command

```
azureuser@docker-vm:~/docker$ docker run hello-world
docker: permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Head "http://%2Fvar%2Frun%2Fdocker.sock/_ping": dial unix /var/run/docker.sock: connect: permission denied.
See 'docker run --help'.
```

This can mean two things,

1.Docker deamon is not running.
2.Your user does not have access to run docker commands.

## Start Docker daemon

```
sudo systemctl status docker
sudo systemctl start docker
```
## Grant Access to your user to run docker commands

To grant access to your user to run the docker command, you should add the user to the Docker Linux group. Docker group is create by default when docker is installed.

```
sudo usermod -aG docker azureuser

```

NOTE: : You need to logout and login back for the changes to be reflected.


## Docker is Installed, up and running 

```
azureuser@docker-vm:~$ docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
e6590344b1a5: Pull complete
Digest: sha256:d715f14f9eca81473d9112df50457893aa4d099adeb4729f679006bf5ea12407
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

```

## Login DockerHub

```
azureuser@docker-vm:~/Docker-Zero-to-Hero/examples/first-docker-file$ docker login
Log in with your Docker ID or email address to push and pull images from Docker Hub. If you don't have a Docker ID, head over to https://hub.docker.com/ to create one.
You can log in with your password or a Personal Access Token (PAT). Using a limited-scope PAT grants better security and is required for organizations using SSO. Learn more at https://docs.docker.com/go/access-tokens/

Username: nsaichaitu
Password:
WARNING! Your password will be stored unencrypted in /home/azureuser/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credentials-store

```

## Docker File 

<img width="424" alt="image" src="https://github.com/user-attachments/assets/b7ed01e0-860b-42aa-aec8-281a2cd49253" />


## Build your Docker Image

```
azureuser@docker-vm:~/Docker-Zero-to-Hero/examples/first-docker-file$ docker build -t nsaichaitu/my-first-docker-image:latest .
DEPRECATED: The legacy builder is deprecated and will be removed in a future release.
            Install the buildx component to build images with BuildKit:
            https://docs.docker.com/go/buildx/

Sending build context to Docker daemon  3.072kB
Step 1/6 : FROM ubuntu:latest
 ---> a04dc4851cbc
Step 2/6 : WORKDIR /app
 ---> Using cache
 ---> e411e4d720c6
Step 3/6 : COPY . /app
 ---> Using cache
 ---> 93cc6a0a688c

```

## Verify Docker Image is created

```
azureuser@docker-vm:~/Docker-Zero-to-Hero/examples/first-docker-file$ docker images
REPOSITORY                         TAG       IMAGE ID       CREATED          SIZE
nsaichaitu/my-first-docker-image   latest    9a5de09473d9   35 minutes ago   552MB
nschaitu/my-first-docker-image     latest    9a5de09473d9   35 minutes ago   552MB
ubuntu                             latest    a04dc4851cbc   9 days ago       78.1MB
hello-world                        latest    74cc54e27dc4   2 weeks ago      10.1kB

```

## Run your First Docker Container

```
azureuser@docker-vm:~/Docker-Zero-to-Hero/examples/first-docker-file$ docker run -it nsaichaitu/my-first-docker-image:latest
Hello World

```

## Push the Image to DockerHub and share it with others

```
azureuser@docker-vm:~/Docker-Zero-to-Hero/examples/first-docker-file$ docker push nsaichaitu/my-first-docker-image:latest
The push refers to repository [docker.io/nsaichaitu/my-first-docker-image]
adad54215a21: Layer already exists
2e27074727d9: Layer already exists
a1cc37594853: Layer already exists
4b7c01ed0534: Layer already exists
latest: digest: sha256:87ca27fdd3744486aaf4779517659b0b3527b4db13cc72e97ed38a17324540cb size: 1155

```

Note: Docker will run using rootuser and it is a single monolothic process..
