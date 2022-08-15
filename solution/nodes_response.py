# -*- coding: utf-8 -*-

# original response from: https://nodes-on-nodes-challenge.herokuapp.com/nodes/089ef556-dfff-4ff2-9733-654645be56fe
# nodes_response = [
#     {
#         "id": "089ef556-dfff-4ff2-9733-654645be56fe",
#         "child_node_ids": [
#             "c20c063c-99b3-452f-a44f-72e2dac4eec0",
#             "3e82e3c2-4cd1-4cab-91da-899430299c84"
#         ]
#     }
# ]


# my own sample response to test
nodes_response = [
    {
        "id": "089ef556-dfff-4ff2-9733-654645be56fe",
        "child_node_ids": [
            "c20c063c-99b3-452f-a44f-72e2dac4eec0",
            "3e82e3c2-4cd1-4cab-91da-899430299c84"
        ]
    },
    {
        "id": "089ef556-dfff-4ff2-9733-654645be56fe-00",
        "child_node_ids": [
            "c20c063c-99b3-452f-a44f-72e2dac4eec0-00", # shared A
            "3e82e3c2-4cd1-4cab-91da-899430299c84-01" # shared B
        ]
    },
    {
        "id": "089ef556-dfff-4ff2-9733-654645be56fe",
        "child_node_ids": [
            "c20c063c-99b3-452f-a44f-72e2dac4eec0-00", # shared A
            "3e82e3c2-4cd1-4cab-91da-899430299c84-02" # shared C
        ]
    },
    {
        "id": "089ef556-dfff-4ff2-9733-654645be56fe-00",
        "child_node_ids": [
            "c20c063c-99b3-452f-a44f-72e2dac4eec0-00", # shared A
            "3e82e3c2-4cd1-4cab-91da-899430299c84-02" # shared C
        ]
    },
    {
        "id": "089ef556-dfff-4ff2-9733-654645be56fe-01",
        "child_node_ids": [
            "c20c063c-99b3-452f-a44f-72e2dac4eec0-00", # shared A
            "3e82e3c2-4cd1-4cab-91da-899430299c84-01" # shared B
        ]
    }
]