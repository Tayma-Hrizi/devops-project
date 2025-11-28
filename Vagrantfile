# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  
  # Utiliser une box Ubuntu stable pour le provisionnement
  config.vm.box = "ubuntu/focal64" 
  
  # --- 1. VM du Serveur DevOps/Jenkins (CI/CD, Nagios) ---
  config.vm.define "devops-server" do |devops|
    devops.vm.hostname = "devops-server"
    
    # Configuration du réseau privé avec IP statique
    devops.vm.network "private_network", ip: "192.168.33.10"
    
    # Redirection de port pour accéder à Jenkins depuis la machine hôte
    devops.vm.network "forwarded_port", guest: 8080, host: 8080, id: "jenkins_web_ui"
    
    # Ressources accrues pour le serveur Jenkins
    devops.vm.provider "virtualbox" do |vb|
      vb.memory = "2048" # 2GB de RAM
      vb.cpus = "2"      # 2 CPUs
    end
    
    # Provisionnement Ansible pour installer Jenkins, Docker (pour le build), et Nagios
    devops.vm.provision "ansible" do |ansible|
      ansible.playbook = "ansible/devops_server_playbook.yml"
    end
  end


  # --- 2. VM de l'Hôte d'Application (Déploiement Docker Compose) ---
  config.vm.define "app-host" do |app|
    app.vm.hostname = "app-host"
    
    # Configuration du réseau privé avec IP statique
    app.vm.network "private_network", ip: "192.168.33.20"
    
    # Redirection de port pour accéder à l'application depuis la machine hôte
    # Le frontend écoute sur le port 80 du conteneur, mappé ici au port 80 de l'hôte
    app.vm.network "forwarded_port", guest: 80, host: 80, id: "app_frontend"
    # Laissez le port 5000 (backend) accessible en interne si Nagios le vérifie
    
    # Provisionnement Ansible pour installer Docker Engine et Docker Compose
    app.vm.provision "ansible" do |ansible|
      ansible.playbook = "ansible/app_host_playbook.yml"
    end
  end
  
end