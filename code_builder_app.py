from langchain.llms import CTransformers
from langchain.chains import LLMChain
from langchain import PromptTemplate
import os
import io
import gradio as gr
import time


custom_prompt_template = """
You are an AI coding assistant. Generates a code snippet based on the given query and return coding snippets.
Query: {query}

Must return helpful answer.
Helpful Answer: 
"""

def set_custom_prompt():
    prompt = PromptTemplate(template=custom_prompt_template,
    input_variables=['query'])
    return prompt


#Loading the model
def load_model():
    llm = CTransformers(
        model = "model/luna-ai-llama2-uncensored.Q4_0.gguf",
        model_type="llama",
        max_new_tokens = 512,
        temperature = 0.2,
        repetition_penalty = 1.15
    )

    return llm

print(load_model())

def chain_pipeline():
    llm = load_model()
    qa_prompt = set_custom_prompt()
    qa_chain = LLMChain(
        prompt=qa_prompt,
        llm=llm
    )
    return qa_chain

llmchain = chain_pipeline()

def bot(query):
    llm_response = llmchain.run({"query": query})
    return llm_response

with gr.Blocks(title='Code Llama Assistant Demo') as demo:
    gr.Markdown("# Code Llama Assistant Demo")
    chatbot = gr.Chatbot([], elem_id="chatbot", height=500)
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    def respond(message, chat_history):
        bot_message = bot(message)
        chat_history.append((message, bot_message))
        time.sleep(2)
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

demo.launch()