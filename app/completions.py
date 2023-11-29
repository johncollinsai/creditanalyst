import requests
import traceback
import os
import re
import openai
import fire
import torch
import torch.multiprocessing as mp
from torch.nn.parallel import DistributedDataParallel as DDP
from .validateproject import validate_project
from .prompts import PROMPTS
from google.cloud import aiplatform
from vertexai.preview.language_models import TextGenerationModel

# from llama import Llama # uncomment this line to use llama-2-7b

def get_api_key():
    api_key = os.environ["OPENAI_API_KEY"]
    openai.api_key = api_key    
    return api_key

api_key = get_api_key()

def setup(rank, world_size):
    os.environ['MASTER_ADDR'] = 'localhost'
    os.environ['MASTER_PORT'] = '12355'

    # initialize the process group
    torch.distributed.init_process_group("gloo", rank=rank, world_size=world_size)

def cleanup():
    torch.distributed.destroy_process_group()

# roughly estimate tokens in response provided by PaLM-2
def count_tokens_simple(text):
    return len(text.split())

def generate_response(
        prompt, 
        model, 
        project_type,
        api_key, 
        max_batch_size=4, 
        max_tokens=2000, # max tokens for gpt-4 = 8192, for palm-2 supported range = [1, 1025)
        temperature=0.5, # 0 implies models will always pick most likely next word. Set zero but use high top_p and top_k values
        top_p=0.95, # top-P determines how selects tokens for output, where lower value = less random responses 
        top_k=40, # top-K determines how  model selects tokens for output, where lower value = less random responses 
        ckpt_dir=None,  # set to None as default value, for situations when llama-2-7b is not used
        tokenizer_path=None,  # set to None as default value, for situations when llama-2-7b is not used
        max_seq_len=100, # max length of the input sequence, set to 25 because llama-2-7b seems to work in simple Q&A fashion
        max_gen_len=1000 # max length of the generated sequence, set to max_tokens
    ):
    try:
        print("prompt: ", prompt)   
        print("model: ", model)   
        print("project_type: ", project_type)   

        is_valid = validate_project(prompt, model, api_key)
        
        if not is_valid:
            raise ValueError(f"Invalid AI project description: {prompt}")
        
        # Initialize the Vertex AI SDK
        aiplatform.init(
            project='johncollins',
            location='us-central1',
            staging_bucket='gs://projectmanager'
        )
        
        user_prompt = PROMPTS[model][project_type].format(prompt=prompt)
        print("user_prompt: ", user_prompt) 
        
        openai.api_key = api_key

        if model == "GPT-4":                
            def create_chat_completion():
                return openai.ChatCompletion.create(
                    model="gpt-4-0613", # gpt-4-0613 is the latest version of gpt-4 as of 2021-06-13
                    messages=[
                        {"role": "system", "content": f"You are an AI trained to provide detailed and accurate information about AI build and deployment projects."},
                        {"role": "assistant", "content": user_prompt}
                    ],
                    max_tokens=max_tokens,
                    stop=None,
                    temperature=temperature,
                    top_p=top_p,
                )

            response = create_chat_completion()
            print(model, " response:", response)

            final_response = response['choices'][0]['message']['content']
            return final_response.strip()
        
        elif model == "GPT-4-Turbo":
            def create_chat_completion():
                return openai.ChatCompletion.create(
                    model="gpt-4-1106-preview", # At 20231109 GPT-4 Turbo = gpt-4-1106-preview, stable production-ready model coming later
                    messages=[
                        {"role": "system", "content": f"You are an AI trained to provide detailed and accurate information about AI build and deployment projects."},
                        {"role": "assistant", "content": user_prompt}
                    ],
                    max_tokens=max_tokens,
                    stop=None,
                    temperature=temperature,
                    top_p=top_p,
                )

            response = create_chat_completion()
            print(model, " response:", response)

            final_response = response['choices'][0]['message']['content']
            return final_response.strip()
        
        elif model == "PaLM-2":
            parameters = {
                "temperature": temperature,
                "max_output_tokens": max_tokens,
                "top_p": top_p,
                "top_k": top_k,
            }
            
            palm_model = TextGenerationModel.from_pretrained("text-bison") # text-bison@001 is stable version as of 2023-06-07
            
            response = palm_model.predict(user_prompt, **parameters)
            print(f"{model} response: {response.text}")
            return response.text.strip()
        
        elif model == "Claude-2":
            return "Claude-2 is not yet supported"
        
        else:
            return f"This model {model} is not yet supported"

    # except block to catche any other errors and print to terminal
    except Exception as e:
        print(f"An error of type {type(e).__name__} occurred during the generation: {str(e)}")
        traceback.print_exc()
        return str(e)
