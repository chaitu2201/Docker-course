# Docker-course

What is a Virtual Machine(VM)? 

A virtual machine is no different than any other physical computer like a laptop, smart phone, or server. It has a CPU, memory, disks to store your files, and can connect to the internet if needed. While the parts that make up your computer (called hardware) are physical and tangible, VMs are often thought of as virtual computers or software-defined computers within physical servers, existing only as code.

![image](https://github.com/user-attachments/assets/bcb2f9db-e491-4116-8a71-e036edb723ab)

What is Hypervisor?

A hypervisor is a virtualization software that enables multiple virtual machines (VMs)—each with its own operating system (OS)—to run on one physical server. The hypervisor pools and allocates physical computing resources as needed by the VM, enabling efficiency, flexibility and scalability.It separates VMs from each other logically, assigning each its own slice of the underlying computing power, memory and storage. This prevents the VMs from interfering with each other. For example, if one OS suffers a crash or a security compromise, the others survive.


VM --------------- Advancement to physical servers 

Eg: Big Land 

What is a server?

A server is a computer program or device that provides a service to another computer program and its user, also known as the client. The term server can refer to a physical machine, a virtual machine (VM) or software that's performing server services.In the client-server model, a server program fulfills requests from client programs, which might be running on the same computer or other computers.


A virtual server is a virtual representation of a physical server. Like a physical server, a virtual server includes its own OS and applications


<img width="722" alt="image" src="https://github.com/user-attachments/assets/bc97610d-88b2-4763-95ad-ea23e8df4d74" />

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
What is a container ?

A container is a bundle of Application, Application libraries required to run your application and the minimum system dependencies. A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings.

![image](https://github.com/user-attachments/assets/01ac8809-8e8e-4e47-8229-016104750403)

Containers vs Virtual Machine
```
1. Resource Utilization: Containers share the host operating system kernel, making them lighter and faster than VMs. VMs have a full-fledged OS and hypervisor, making them more resource-intensive.
2. Portability: Containers are designed to be portable and can run on any system with a compatible host operating system. VMs are less portable as they need a compatible hypervisor to run.
3. Security: VMs provide a higher level of security as each VM has its own operating system and can be isolated from the host and other VMs. Containers provide less isolation, as they share the host operating system.
4. Management: Managing containers is typically easier than managing VMs, as containers are designed to be lightweight and fast-moving.
```

Containers are lightweight because they use a technology called containerization, which allows them to share the host operating system's kernel and libraries, while still providing isolation for the application and its dependencies. This results in a smaller footprint compared to traditional virtual machines, as the containers do not need to include a full operating system.

official ubuntu base image which you can use for your container. It's just ~ 22 MB, isn't it very small ? on a contrary if you look at official ubuntu VM image it will be close to ~ 2.3 GB. So the container base image is almost 100 times less than VM image.



















