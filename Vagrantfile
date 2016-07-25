Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.synced_folder ".", "/var/webapps/pokemongo"
  config.vm.network :private_network, ip: "172.16.0.2"

  config.vm.provider "virtualbox" do |v|
  	v.memory = 512
  	v.cpus = 1
  end

  # config.vbguest.iso_path = "#{ENV['HOME']}/Downloads/VBoxGuestAdditions_4.3.36.iso"

end