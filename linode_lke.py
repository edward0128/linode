import json
import requests
import time

class linode_lke_api():

 def __init__(self, token):
  self.token = token
  self.url = "https://api.linode.com/v4/"
  self.header = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer '
    }
  self.header["Authorization"]+=token
  self.cluster=[]
  self.payload_cluster = {
    "label": "1234",
    "region": "us-central",
    "k8s_version": "1.16",
    "tags": ["ecomm", "blogs"],
    "node_pools": [
          {
            "type": "g6-nanode-1",
            "count": 1
          }]
    }
 def json_pretty_output(self,context):
  parsed = json.loads(context)
  return json.dumps(parsed, indent=4, sort_keys=True)

 def check_status(self,response):
  if response.ok:
      print(response.content)
      return True
  return False

 def list_kubernetes_clusters(self):
  r = requests.get(self.url+"lke/clusters/",headers = self.header)
  if self.check_status(r):
      return True
  return False

 
 def create_kubernetes_cluster(self,payload_cluster):
  r = requests.post(self.url+"lke/clusters", data=json.dumps(payload_cluster), headers=self.header)
  print(self.json_pretty_output(r.content))

 def view_kubernetes_cluster(self,clusterid):
  r = requests.get(self.url+"lke/clusters/"+str(clusterid),headers = self.header)
  if self.check_status(r):
      return True
  return False
 
 def update_kubernetes_cluster(self,clusterid,payload_cluster):
  r = requests.put(self.url+"lke/clusters/"+str(clusterid), data=json.dumps(payload_cluster), headers=self.header)
  print(self.json_pretty_output(r.content))
 
 def delete_kubernetes_cluster(self,clusterid):
  r = requests.delete(self.url+"lke/clusters/"+str(clusterid),headers = self.header)
  print(self.json_pretty_output(r.content))
 
 def list_node_pools(self,clusterid):
  r = requests.get(self.url+"lke/clusters/"+str(clusterid)+"/pools",headers = self.header)
  if self.check_status(r):
      return True
  return False

 def create_node_pool(self,clusterid,payload_pool):
  r = requests.post(self.url+"lke/clusters/"+str(clusterid)+"/pools", data=json.dumps(payload_pool), headers=self.header)
  print(self.json_pretty_output(r.content))
 
 def view_node_pool(self,clusterid,poolid):
  r = requests.get(self.url+"lke/clusters/"+str(clusterid)+"/pools/"+str(poolid),headers = self.header)
  if self.check_status(r):
      return True
  return False

 def update_node_pool(self,clusterid,poolid,payload_pool):
  r = requests.put(self.url+"lke/clusters/"+str(clusterid)+"/pools/"+str(poolid), data=json.dumps(payload_pool),headers = self.header)
  print(self.json_pretty_output(r.content))
 
 def delete_node_pool(self,clusterid,poolid):
  r = requests.delete(self.url+"lke/clusters/"+str(clusterid)+"/pools/"+str(poolid),headers = self.header)
  print(self.json_pretty_output(r.content))
 
 def list_kubernetes_api_endpoints(self,clusterid):
  r = requests.get(self.url+"lke/clusters/"+str(clusterid)+"/api-endpoints",headers = self.header)
  if self.check_status(r):
      return True
  return False
 
 def view_kubeconfig(self,clusterid):
  r = requests.get(self.url+"lke/clusters/"+str(clusterid)+"/kubeconfig",headers = self.header)
  if self.check_status(r):
      return True
  return False
 
 def list_kubernetes_versions(self):
  r = requests.get(self.url+"lke/versions/",headers = self.header)
  if self.check_status(r):
      return True
  return False
 
 def view_kubernetes_version(self,version):
  r = requests.get(self.url+"lke/versions/"+str(version),headers = self.header)
  if self.check_status(r):
      return True
  return False

def test_linode_api():
    token="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    linode_cluster = linode_lke_api(token)
    assert linode_cluster.list_kubernetes_clusters() == True

if __name__ == "__main__":
    token="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    linode_cluster = linode_lke_api(token)
    
    linode_cluster.list_kubernetes_clusters()
    #linode_cluster.view_kubernetes_cluster(7580)
    #linode_cluster.list_node_pools(7984)
    #linode_cluster.view_node_pool(7580,9575)
    #linode_cluster.list_kubernetes_api_endpoints(7580)
    #linode_cluster.view_kubeconfig(7580)
    #linode_cluster.view_kubernetes_version("1.15")
    
    # create_cluster = {
    # "label": "1234",
    # "region": "us-central",
    # "k8s_version": "1.16",
    # "tags": ["ecomm", "blogs"],
    # "node_pools": [
    #       {
    #         "type": "g6-nanode-1",
    #         "count": 1
    #       }]
    # }
    # linode_cluster.create_kubernetes_cluster(create_cluster)

    #time.sleep(30)
    #linode_cluster.delete_kubernetes_cluster(7984)
    #update_cluster = {
    #"label": "4567"
    #}
    #linode_cluster.update_kubernetes_cluster(7983,update_cluster)

    # create_pool = {
    # "type": "g6-nanode-1",
    # "count": 1
    # }
    # linode_cluster.create_node_pool(7984,create_pool)

    
    #linode_cluster.delete_node_pool(7984,10042)

    #update_pool = {
    #    "count": 1
    #}
    #linode_cluster.update_node_pool(7984,10043,update_pool)
    
