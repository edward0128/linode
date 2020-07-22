from linode_api4 import LinodeClient
client = LinodeClient("5b1eb1cd3f9664dfd429ec32a00a8cfbb4c8XXXXXXXXXXXXXXXXXXXXXXXXXX")

#my_linodes = client.linode.instances()
#for current_linode in my_linodes:
#    print(current_linode.label[3])
#print(my_linodes[3].label)
#my_linodes[3].delete()

#for current_linode in my_linodes:
#    print(current_linode)

# #available_regions = client.regions()

# ltypes = client.linode.types()
# images = client.images()
# regions = client.regions()

# for flavor in ltypes:
#     print(flavor)

# for image in images:
#     print(image)

# for region in regions:
#     print(region)

available_regions = client.regions()
chosen_region = available_regions[0]
new_linode, password = client.linode.instance_create('g6-nanode-1','ap-west',image='linode/debian9',label="test213")
print("ssh root@{} - {}".format(new_linode.ipv4[0], password))
