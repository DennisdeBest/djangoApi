# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
	config.vm.box = "debian/stretch64"

	config.vm.network "private_network", ip: "10.0.0.200"
	config.vm.hostname = "django.api"
	config.hostsupdater.aliases = ["django.api"]
	config.vm.synced_folder ".", "/vagrant", disabled: true

	config.vm.synced_folder "project/", "/home/vagrant/project", type: "nfs",
		mount_options: %w{nolock,vers=3,udp,noatime,actimeo=1}
	config.vm.provider "virtualbox" do |vb|
	vb.customize ["setextradata", :id, "VBoxInternal2/SharedFoldersEnableSymlinksCreate/v-root", "1"]
		# Display the VirtualBox GUI when booting the machine
		vb.gui = false

		# Customize the amount of memory on the VM:
		vb.memory = "4048"
		vb.name = "Django API"
		vb.customize ["modifyvm", :id, "--usb", "on"]
		vb.customize ["modifyvm", :id, "--usbehci", "off"]
	end

  	config.vm.provision "ansible" do |ansible|
    	ansible.playbook = "provision/playbook.yml"
    	ansible.inventory_path = "provision/hosts"
    	ansible.limit = "all"
  	end

end
