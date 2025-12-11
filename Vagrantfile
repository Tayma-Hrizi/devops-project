Vagrant.configure("2") do |config|
  # Define the base box to use (e.g., Ubuntu 22.04)
  config.vm.box = "ubuntu/jammy64"  # Adjust the box version as needed

  # Configure the VM's network settings (optional, e.g., private IP)
  config.vm.network "private_network", type: "dhcp"

  # Set up VM provider settings (optional, e.g., amount of RAM and CPUs)
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"  # Set memory to 2GB (adjust as necessary for Minikube)
    vb.cpus = 2         # Set number of CPUs
  end

  # Provisioning script to install Docker, Jenkins, and Minikube
  config.vm.provision "shell", inline: <<-SHELL
    # Update package list
    sudo apt-get update

    # Install Docker
    sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
    sudo apt-get update
    sudo apt-get install -y docker-ce docker-ce-cli containerd.io

    # Add current user to docker group to run docker without sudo
    sudo usermod -aG docker vagrant

    # Install Jenkins
    sudo apt upgrade -y
    sudo apt install fontconfig openjdk-17-jre -y
    sudo apt-get install -y init-system-helpers=1.54~ubuntu1
    sudo wget -O /usr/share/keyrings/jenkins-keyring.asc https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
    echo "deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc]" https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
    sudo apt-get update
    sudo apt-get install -y jenkins

    # Start Jenkins service
    sudo systemctl start jenkins
    sudo systemctl enable jenkins

    # Open firewall port for Jenkins (default port 8080)
    sudo ufw allow 8080
    sudo ufw allow 3000
    sudo ufw enable
    sudo usermod -aG docker jenkins
    sudo systemctl restart jenkins


  SHELL

  # Optional: Forward port 8080 for Jenkins access on the host machine
  config.vm.network "forwarded_port", guest: 8080, host: 8080
  config.vm.network "forwarded_port", guest: 3000, host: 3000
end  