import boto.ec2
import time

region_name = raw_input("Enter the region to launch your instance in: ")
ami_id = raw_input("Enter the AMI id: ")
private_key = raw_input("Enter the Private Key: ")
instance_type = raw_input("Enter the Instance Type: ")
subnet_id = raw_input("Enter the Subnet ID: ")
instance_name = raw_input("Enter the name you want to give to your instance: ")

print "Establishing connection with AWS"

connection = boto.ec2.connect_to_region(region_name)

print "Connection established"

print "Launching ec2 instance"

reservation = connection.run_instances(image_id=ami_id, key_name=private_key,instance_type=instance_type,subnet_id=subnet_id)

instance = reservation.instances[0]

connection.create_tags([instance.id],{'Name':instance_name})

while instance.state != "running":
  print "Instance is not running yet. Waiting 30 seconds before retrying."
  time.sleep(30)
  instance.update()

print "Your instance is ready."
print "Ip Address: %s" %instance.ip_address
