from langchain.llms import CTransformers
from langchain.chains import LLMChain
from langchain import PromptTemplate

prompt_template = """
You are an AI coding assistant. Generates a code snippet based on the given query and return coding snippets.
Query: {query}

Must return helpful answer.
Helpful Answer: 
"""

prompt = PromptTemplate(template=prompt_template, input_variables=['query'])


llm = CTransformers(model = "model/luna-ai-llama2-uncensored.Q4_0.gguf",
                    model_type = "llama",
                    max_new_tokens=512,
                    temperature=0.2
                    )

llm_chain = LLMChain(prompt=prompt, llm=llm)

llm_response = llm_chain.run({"query": "Write a python code to do semantic analysis on list of tweets"})

print(llm_response)