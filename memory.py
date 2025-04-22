from langchain.memory import ConversationBufferMemory

def get_memory(memory_key="chat_history"):
    return ConversationBufferMemory(
        memory_key=memory_key,
        input_key="input",       
        output_key="text",   
        return_messages=True  
    )

def create_character_memory(character_name=None):
    memory = get_memory()
    return memory