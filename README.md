# ai-code-assistant

**AI Code Assistant**

This repository contains a simple code assistant built using LangChain, CTransformers, and Gradio. The code assistant can be used to generate code snippets, translate code from one language to another, and answer code-related questions in a comprehensive and informative way. 

**To use the code assistant:**

1. Clone this repository to your local machine.

2. Create "/model" directory
    - Example code uses "luna-ai-llama2-uncensored.Q4_0.gguf".
    - If uses multiple model files (.bin files), specify a model file: model_file='ggml-model.bin'
      https://python.langchain.com/docs/integrations/providers/ctransformers
      
3. Install the required dependencies: 
    ```bash
    pip install -r requirements.txt
    ```
4.  Start the Gradio app:
    ```bash
    python code_builder_app.py
    ```
Note: Change the transformer configs according to the local model under "/model" directory
