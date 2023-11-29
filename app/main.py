import yaml
import random
import asyncio
import requests

from flask import Blueprint, render_template, request, jsonify
from .completions import generate_response, get_api_key

# Path to the yaml file that contains the deployment information in order to show version on the UI
yaml_path = "projectmanager-deploymentsandservices.yaml"

bp = Blueprint("main", __name__)

@bp.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

@bp.route('/get_completion', methods=["POST"])
def get_completion():
    try:
        prompt = request.form['prompt']
        model = request.form['model']
        project_type = request.form['project_type']
        api_key = get_api_key()

        # Replace the strings 'path_to_checkpoint' and 'path_to_tokenizer' with the actual paths
        # ckpt_dir = '/home/john/llama/llama-2-7b'
        # tokenizer_path = '/home/john/llama/tokenizer.model'
        ckpt_dir = ''
        tokenizer_path = ''

        # Generate response using keyword arguments to ensure that the values are assigned to the correct parameters, and the default values for the omitted parameters (like max_tokens) will be used in completions.py
        response = generate_response(
            prompt=prompt, 
            model=model, 
            project_type=project_type, 
            api_key=api_key, 
            ckpt_dir=ckpt_dir, 
            tokenizer_path=tokenizer_path
        )

        return jsonify({"success": True, "response": response})

    except ValueError as e:
        # jsonify() converts Python dictionary to JSON for the specific model
        return jsonify({"success": False, "error": str(e)})

@bp.route('/get-version', methods=['GET'])
def get_version():
    with open(yaml_path, 'r') as file:
        documents = list(yaml.load_all(file, Loader=yaml.FullLoader))

        # Iterate through the documents and find the Deployment
        for doc in documents:
            if doc['kind'] == 'Deployment':
                deployment = doc
                break
        else:
            raise ValueError('Deployment not found in YAML file')

        image = deployment['spec']['template']['spec']['containers'][0]['image']
        version = image.split(':')[-1]

    return jsonify(version=version)


