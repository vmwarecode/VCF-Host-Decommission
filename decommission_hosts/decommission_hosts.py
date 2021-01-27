#Decommission hosts.
#Decommissions hosts gives as parametres.
import sys
import os
sys.path.append(os.path.abspath(__file__ + '/../../'))
from Utils.utils import Utils
import pprint

class DecomissionHosts:
    def __init__(self):
        print('Decommission Hosts')
        self.utils = Utils(sys.argv)
        self.hostname = sys.argv[1]

    def decommission_hosts(self):
        decommission_url = 'https://'+self.hostname+'/v1/hosts'
        payload = self.utils.read_input(os.path.abspath(__file__ +'/../')+'/decommission_hosts_spec.json')
        print ('Decommissioning hosts...')
        response = self.utils.delete_request(payload,decommission_url)
        pprint.pprint(response)
        task_id = response['id']
        task_url = 'https://'+self.hostname+'/v1/tasks/'+task_id
        print ('Decommissioning of hosts is ' + self.utils.poll_on_id(task_url,True))

if __name__== "__main__":
    DecomissionHosts().decommission_hosts()