---
title: "Simple Vagrant Ansible Local Example"
date: "2018-07-05"
categories: 
  - "miscellaneous"
---

I recently worked on a project showing how to install and configure a complete Pentaho Server instance with a back-end data repository housed in Postgresql. I wanted to select a provisioner for this work that would be easy to use to deploy the server either as a single instance VM, as an Amazon AMI, or as a set of docker containers.

As I was setting up the first such target I wanted to support – a VirtualBox VM – I noticed that the examples and documentation for using Vagrant’s ansible-local provisioner were a bit sparse. Because of this, once I had my proof of concept working I decided to make a copy of the repository so I could share it with my adoring public. Well, with the public, anyway!

I’ve shared the code on [Github](https://github.com/CodeSolid/vagrant-ansible-local-example). It’s pretty straightforward, but let’s walk through it briefly. The code consists of four files, which together launch a simple Centos VM with Nginx installed:

- Vagrantfile - We’re using Vagrant to manage our VM.
- playbook.yml - Our Ansible Playbook that will install Nginx for us on our Vagrant VM.
- inventory - Ansible “inventory” lists are groups of target machines that Ansible will configure. Unlike tools like Chef and Puppet, which rely on having a client installed, Ansible can configure remote machines listed in its inventory over SSH. Since we’re only configuring a single VM, our inventory file is quite simple and simply contains the same IP address we configure in our VagantFile.
- index.html - A test file for Nginx to serve.

The Vagrantfile is only a few lines:

```ruby
Vagrant.configure("2") do |config|
  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.box = "centos/7"
  config.vm.network 'private_network', ip: '192.168.56.10'
  config.vm.provision :ansible_local do |ansible|
    ansible.playbook = "playbook.yml"
    ansible.inventory_path = 'inventory'
    ansible.limit = 'all'
end
```

This example assumes Vagrant and Virtualbox are installed. We configure the VM to use a private network using a static IP in the reserved private address space (see the Vagrant docs on [private networks](https://www.vagrantup.com/docs/networking/private_network.html) for more information). We also forward a port so that once you bring the VM up you can test the connection on your host machine’s browser (at http://localhost:8080).

Looking at the ansible\_local configuration, we see it points to the playbook.yml file in our directory. To keep things simple, this playbook was based on Ansible’s example, [Getting Started Writing Your First Playbook](https://www.ansible.com/blog/getting-started-writing-your-first-playbook). It installs Nginx, copies index.html to the right place, and starts the server listening. We won’t show the file here, but you can take a look on Github.

The inventory file, an important piece that was missing from some of the documentation, is a one-liner that matches the IP in our private network:

```ruby
192.168.56.10 ansible_connection=local
```

Note we still give the IP even though we’ve specified “ansible\_connection=local.” I ran into some issues at one point using localhost.

Finally, our Vagrantfile sets “`ansible.limit = ‘all’`”, which tells ansible to connect to “all the machines in our inventory” (that’s right all one of them)!

### Vagrant Up

To try it out, run “vagrant up” from the directory containing the Vagrantfile. It’ll take a few minutes to download the Centos VM and configure the VM, then you can try to connect to Nginx from your web browser: [http://localhost:8080](http://localhost:8080/).

## You May Also Enjoy

- [Building a Docker Golang Container](https://codesolid.com/building-a-docker-golang-container/)
- [How to Use Docker Python Images and Docker Compose with Python](https://codesolid.com/how-to-use-docker-with-python/)
