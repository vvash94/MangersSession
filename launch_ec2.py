import boto.ec2
import time

ami_id = "<<AMI ID>>"
private_key = "<<Private Key>>"
instance_type = "<<Instance Type>>"
subnet_id = "<<Subnet to launch the instance in>>"
instance_name = "<<Name of the instance>>"
region_name = "<<Region Name>>"

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
