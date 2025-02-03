# Docker-course

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
# <ins>Docker</ins>

## What is Docker ?

Docker is a containerization platform that provides easy way to containerize your applications, which means, using Docker you can build container images, run the images to create containers and also push these containers to container regestries such as DockerHub, Quay.io and so on.

In simple words, you can understand as containerization is a concept or technology and Docker Implements Containerization.

## Docker Architecture ?

![image](https://github.com/user-attachments/assets/5445f545-a2bb-43c0-9491-a0903af5d82c)

## Docker LifeCycle

There are three important things,

1. docker build -> builds docker images from Dockerfile
2. docker run -> runs container from docker images
3. docker push -> push the container image to public/private regestries to share the docker images.

<img src="https://github.com/user-attachments/assets/213a4462-fa3f-4003-9622-e7d1c83da52e" width=50% height=50%>

## Understanding the terminology



    














