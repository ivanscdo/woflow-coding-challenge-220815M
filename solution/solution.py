import requests
   
def make_callout(endpoint_node_ids):
    endpoint = ''
    if len(endpoint_node_ids) == 1:
        endpoint = ''.join(map(str, endpoint_node_ids))
    elif len(endpoint_node_ids) > 1:
        endpoint = ','.join(map(str, endpoint_node_ids))

    base_url = 'https://nodes-on-nodes-challenge.herokuapp.com/nodes/'
    r = requests.get(base_url + endpoint)
    response = r.json()

    return response

def execute(endpoint_node_ids, unique_node_ids, nodes_response):
    response = make_callout(endpoint_node_ids)
    endpoint_node_ids = []

    for i, parent_node in enumerate(response):
        # print('\nparent_node:',parent_node)
        nodes_response.append(parent_node) # store each individual response
        unique_node_ids.add(parent_node.get('id')) # get parent node id
        endpoint_node_ids = parent_node.get('child_node_ids')

        if len(endpoint_node_ids) > 0:
            execute(endpoint_node_ids, unique_node_ids, nodes_response)

def get_shared_node_ids(nodes_response):
    child_node_ids_count = dict() # key/value pair of child_node_ids to number of times it appears; ex: {id123: 1}
    most_shared_id = ''
    most_shared_id_count = 0

    for i, parent_node in enumerate(nodes_response): 
        child_nodes = parent_node.get('child_node_ids')

        for j, child_node_id in enumerate(child_nodes):
            child_node_count = 0 # reset count each time we enter new list of child_node_ids

            if not child_node_ids_count.get(child_node_id): # child_node_id HAS NOT been previously added to dict
                child_node_count += 1 # increase count by one 
                child_node_ids_count.update({child_node_id: child_node_count}) # add child_node_id and its count

            elif child_node_ids_count.get(child_node_id):  # child_node_id HAS been previously added to dict
                existing_child_node_count = child_node_ids_count.get(child_node_id) # get existing count from dict and increase by one
                existing_child_node_count += 1
                child_node_ids_count.update({child_node_id: existing_child_node_count}) # update child_node_id and its count in dict

    # print('child_node_ids_count:',child_node_ids_count)
    for key, value in child_node_ids_count.items(): # iterate through dict
        if value > most_shared_id_count: # if the child_node_count in dict is greater than the highest count so far(most_shared_id_count), replace count and grab that child_node_id 
            most_shared_id_count = value
            most_shared_id = key

    return most_shared_id
    
nodes_response = [] # store all responses
unique_node_ids = set() # store unique nodes
endpoint_node_ids = ['089ef556-dfff-4ff2-9733-654645be56fe']

execute(endpoint_node_ids, unique_node_ids, nodes_response)
print('number of unique nodes:',len(unique_node_ids))
print('most_shared_id:',get_shared_node_ids(nodes_response))
# print('nodes_response:',nodes_response)


