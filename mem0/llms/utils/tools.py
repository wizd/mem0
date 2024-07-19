ADD_MEMORY_TOOL = {
    "type": "function",
    "name": "add_memory",
    "function": {
        "description": "Add a memory",
        "parameters": {
            "type": "object",
            "properties": {
                "data": {"type": "string", "description": "Data to add to memory"}
            },
            "required": ["data"],
        },
    },
}

UPDATE_MEMORY_TOOL = {
    "type": "function",
    "name": "update_memory",
    "function": {
        "description": "Update memory provided ID and data",
        "parameters": {
            "type": "object",
            "properties": {
                "memory_id": {
                    "type": "string",
                    "description": "memory_id of the memory to update",
                },
                "data": {
                    "type": "string",
                    "description": "Updated data for the memory",
                },
            },
            "required": ["memory_id", "data"],
        },
    },
}

DELETE_MEMORY_TOOL = {
    "type": "function",
    "name": "delete_memory",
    "function": {
        "description": "Delete memory by memory_id",
        "parameters": {
            "type": "object",
            "properties": {
                "memory_id": {
                    "type": "string",
                    "description": "memory_id of the memory to delete",
                }
            },
            "required": ["memory_id"],
        },
    },
}
