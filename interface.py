from chat_memory import ChatMemory
from model_loader import loadModel

generator=loadModel()
memory=ChatMemory(window_size=3)
print("--------------------------------------------------\n\n")
while True:
    user_input=input("User: ")
    
    if user_input.strip().lower()=="/exit":
        print("Bot: Exiting chatbot. Goodbye!\n\n--------------------------------------------------")
        break

    context=memory.get_context()
    full_input=f"{context}\nUser: {user_input}\nBot:" if context else f"User: {user_input}\nBot:"
    response=generator(full_input, max_new_tokens=60)[0]["generated_text"]

    bot_output=response.split("Bot:")[-1].strip().split("User:")[0].strip()
    print(f"Bot: {bot_output}")
    memory.add_turn(user_input, bot_output)