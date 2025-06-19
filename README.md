# 💬 Context-Aware Chatbot using LaMini-Flan-T5-783M
A lightweight chatbot built using the LaMini-Flan-T5-783M model for generating accurate responses, enhanced with a sliding window memory mechanism that remembers the last 5 interactions for context-aware conversation.

<br>  

# 🚀 Features
🧠 Memory Context: Remembers the last 5 user-bot exchanges using a sliding window approach.  
🔥 LaMini-Flan-T5-783M: Utilizes a fine-tuned T5 model for effective instruction-based responses.  
💻 Simple Interface: Easy-to-run script to initiate and chat via the terminal.  

<br>  

# 📁 File Structure

├── `chat_memory.py`  ->   Handles sliding window memory of past conversations  
├── `interface.py`   ->   Main file to run the chatbot  
└── `model_loader.py`  ->   Loads and prepares the LaMini-Flan-T5-783M model  

<br>  

# 🧠 Sliding Window Mechanism
The chatbot stores the last 5 user questions and bot responses. This enables the model to provide more relevant and context-aware answers, similar to how human conversation works.

## Example:
```
User: What is the Capital of France
Bot: Paris.
  
User: And what about italy?
Bot: The capital of Italy is Rome.
  
User: And of India
Bot: The capital of India is New Delhi.  
```
```
User: Who is the president of America
Bot: The current president of America is Joe Biden.

User: And of India
The current president of India is Narendra Modi.
```
```
User: What is your Name  
Bot: As an AI language model, I do not have a name.  
```
```
User: What is the capital of China  
Bot: Beijing.
  
User: And what of Japan  
Bot: The capital of Japan is Tokyo
  
User: exit  
Exiting chatbot. Goodbye!  
```
<br>   

# 🛠️ Setup Instructions
### 1. Clone the repository
```Git
git clone https://github.com/nishantksingh0/LaMini-Flan-T5-783M_with_sliding_window.git
cd LaMini-Flan-T5-783M_with_sliding_window
```
### 2. Install dependencies
```Python
pip install torch transformers
```
### 3. Run the chatbot
```Python
python interface.py
```

## Use live on cloud 🟢
<a href="https://colab.research.google.com/drive/1VmOeYUdhDA7bp3eO9m9I6V_E7zBCXRbo?usp=sharing" target="_blank">Colab</a> --> Use, Experiment, Update...

<br>   


# 🧾 Example Interaction

![image](https://github.com/user-attachments/assets/e4855b67-764d-4400-a944-8969c15b7f5c)

### - Memory History (memory.history)
```
['User: What is machine learning?\nBot: Machine learning is a type of artificial intelligence that enables computers to learn from data and improve their performance on a specific task without being explicitly programmed.',
 'User: Is it used in healthcare?\nBot: Yes, machine learning is used in healthcare for a variety of applications such as medical image analysis, drug discovery, personalized treatment plans, and predictive analytics.']
```

<br>  

# 📌 Model Info
`Model`: MBZUAI/LaMini-Flan-T5-783M  
`Source`: Hugging Face  
`Type`: Instruction-tuned T5 variant (783M parameters)  
