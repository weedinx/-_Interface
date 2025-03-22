
memory_store = []

def log_interaction(context):
    memory_store.append(context)

def get_recent_context():
    return memory_store[-5:]
