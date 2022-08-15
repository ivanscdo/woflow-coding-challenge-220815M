from nodes_response import nodes_response

# 1. What is the total number of unique nodes?
def get_number_of_unique_nodes(nodes_response):

    unique_nodes = set() # array for storing unique nodes
    number_of_unique_nodes = 0 

    for i, nodes in enumerate(nodes_response):
        node_uuid = nodes.get('id')
        unique_nodes.add(node_uuid)

    number_of_unique_nodes = len(unique_nodes) # length/size of unique_nodes set will tell us how many unique nodes exist
    
    return number_of_unique_nodes

print(get_number_of_unique_nodes(nodes_response))


# 2. Which node ID is shared the most among all other nodes?
# I am assuming the question is referring to child_node_ids being shared among other parent ids,
# and not child_node_ids being parent ids themselves

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

    for key, value in child_node_ids_count.items(): # iterate through dict
        if value > most_shared_id_count: # if the child_node_count in dict is greater than the highest count so far(most_shared_id_count), replace count and grab that child_node_id 
            most_shared_id_count = value
            most_shared_id = key

    return most_shared_id

print(get_shared_node_ids(nodes_response))