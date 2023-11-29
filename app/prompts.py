# define prompts
PROMPTS = {
    "GPT-4": {
        "Assistant": """
        First, assess the details in '{prompt}' to determine if they are suitable for developing and deploying an AI Assistant. Explain your assessment clearly, focusing on the following:
        - Project Scope: How well does '{prompt}' align with the objectives and functionalities of an AI Assistant?
        - Feasibility: Are the goals outlined in '{prompt}' achievable with an AI Assistant?
        - Limitations: Are there any constraints or challenges in '{prompt}' that might affect the successful delivery of an AI Assistant?

        If '{prompt}' is not suitable for an AI Assistant, clearly state this and provide alternative suggestions or recommendations for the type of AI project that would be more appropriate.
        
        If '{prompt}' is applicable, proceed to draft a comprehensive project plan for developing and deploying an AI Assistant. Structure your answer to ensure a close fit between the project as described in '{prompt}' and an AI Assistant solution. In your plan, take into account challenges, unique aspects, and innovative strategies that are most appropriate for '{prompt}':

        1. Initialization, including:
        - Tech Assessment: Enumerate resources, servers, APIs, costs, and essential libraries.
        2. Prerequisites, including:
        - API Key: Obtain a key for your chosen model.
        - Tech Stack: Set up Python, Flask, and necessary libraries.
        3. Backend, including:
        - API: Set up Flask, integrate the API with asynchronous calls, and manage the API key securely.
        - Errors: Handle potential API issues.
        - Security: Add caching, rate limiting, and endpoint protections.
        4. Frontend, including:
        - Design: Make a user-centric interface with mobile and browser considerations.
        5. Testing:
        6. Deployment, including:
        - Platform: Choose an appropriate cloud provider.
        - Pre-deployment: Store secrets, optimize for live environment.
        7. Post-Deployment, including:
        - Maintenance: Schedule updates or API changes.
        8. Documentation, including:
        - Tech Docs: Cover architecture and integrations.
        """,
        "POC": """
        First, assess the details in '{prompt}' to determine if they are suitable for developing and deploying an AI Proof-Of-Concept (PoC). Explain your assessment clearly, focusing on the following:
        - Project Scope: How well does '{prompt}' align with the objectives and functionalities of an AI PoC?
        - Feasibility: Are the goals outlined in '{prompt}' achievable with a PoC?
        - Limitations: Are there any constraints or challenges in '{prompt}' that might affect the successful delivery of a PoC?
        
        If '{prompt}' is not suitable for a PoC, clearly state this and provide alternative suggestions or recommendations for the type of AI project that would be more appropriate.
        
        If '{prompt}' is applicable, based on the details in '{prompt}', explain how to develop and deploy an AI Proof-Of-Concept (PoC). Your audience is AI engineers at OpenAI, Google, and Meta. Please provide accurate technical detail regarding '{prompt}' and cover the following:
        1. Initialization:
        - Goal: Define the PoC's primary objective.
        - Stakeholders: Recognize key participants and their needs.
        - Constraints: Understand time, budget, and resource limits.
        2. Data Handling:
        - Sources: Determine the data origin.
        - Preparation: Clean and process the data.
        - Segmentation: Split data for training and testing.
        3. Model Strategy:
        - Potential Models: Identify suitable AI models.
        - Baseline: Set performance benchmarks with a basic model.
        - Training: Educate selected models on the dataset.
        4. Evaluation:
        - Key Metrics: Select metrics for performance assessment.
        - Testing: Gauge models using the test dataset.
        - Refinement: Adjust models based on feedback.
        5. Visualization:
        - Data Patterns: Display data characteristics.
        - Outcomes: Depict model results.
        - Comparisons: Contrast results if multiple models are used.
        6. Documentation:
        - Objective: Reaffirm the PoC's goal.
        - Methods: Describe the process and tools used.
        - Insights: Share findings and potential limitations.
        7. Stakeholder Interaction:
        - Presentation: Offer a PoC demonstration.
        - Feedback Collection: Receive stakeholder input.
        - Future Discussion: Address next steps or full-scale progression.
        8. Wrap-up:
        - Summary: Conclude the PoC's outcomes.
        - Recommendations: Suggest the viability of further development.
        - Decision: Decide on continuation, modification, or discontinuation.
        """,
        "Model": """
        First, assess the details in '{prompt}' to determine if they are suitable for AI model selection, construction, implementation, evaluation, and documentation. Explain your assessment clearly, focusing on the following:
        - Project Scope: How well does '{prompt}' align with the objectives and functionalities of AI model development?
        - Feasibility: Are the goals outlined in '{prompt}' achievable with the types of models mentioned?
        - Limitations: Are there any constraints or challenges in '{prompt}' that might affect the model development?

        If '{prompt}' is not suitable for AI model development, clearly state this and provide alternative suggestions or recommendations for the type of AI project that would be more appropriate.
        
        If '{prompt}' is applicable, based on the details in '{prompt}', guide on AI model selection, construction, implementation, evaluation, and documentation. Adjust recommendations based on the model class from '{prompt}'. Ensure to cover:
        1. Model Selection:
        - Analyze requirements.
        - Suggest AI model classes (e.g., Supervised, Unsupervised).
        - Recommend specific models (CNN, RNN, Transformers, etc.).
        2. Data Preparation:
        - Guide on collecting and preprocessing data.
        - Discuss dataset splitting (training, validation, test sets).
        3. Model Construction:
        - Define model architecture.
        - Mention crucial hyperparameters.
        - Suggest libraries (TensorFlow, PyTorch, etc.).
        4. Implementation:
        - Offer coding best practices.
        - Discuss training and optimization techniques.
        5. Testing & Evaluation:
        - Propose metrics for evaluation (accuracy, F1-score, etc.).
        - Emphasize validation and interpretation techniques.
        6. Model Variations:
        - Touch upon Supervised, Unsupervised, and Reinforcement Learning.
        - Discuss transfer learning and pre-trained models.
        7. Deployment:
        - Discuss serving the model.
        - Touch on scalability and continuous learning.
        8. Documentation:
        - Guide on model description, results, and conclusion.
        9. Communication:
        - Stress updates to stakeholders and clear documentation.
        """,
        "PAAS": """
        First, assess the details in '{prompt}' to determine if they are suitable for constructing, implementing, and optimizing an AI Platform As A Service (PAAS). Explain your assessment clearly, focusing on the following:
        - Project Scope: How well does '{prompt}' align with the objectives and functionalities of a PAAS?
        - Feasibility: Are the goals outlined in '{prompt}' achievable with a PAAS?
        - Limitations: Are there any constraints or challenges in '{prompt}' that might affect the successful delivery of a PAAS?

        If '{prompt}' is not suitable for a PAAS, clearly state this and provide alternative suggestions or recommendations for the type of AI project that would be more appropriate.
        
        If '{prompt}' is applicable, given the specifics in '{prompt}', offer guidance on constructing, implementing, and optimizing an AI Platform As A Service (PAAS). Adjust recommendations based on the provided details in '{prompt}'. Ensure to include:
        1. Service Design:
        - Define core functionalities and capabilities of the PAAS.
        - Establish user roles (e.g., admins, developers, end-users).
        2. Infrastructure Setup:
        - Suggest optimal cloud providers (e.g., AWS, Azure, GCP).
        - Discuss containerization (Docker) and orchestration (Kubernetes).
        3. Data Handling:
        - Guide on data storage, retrieval, and scalability solutions.
        - Address data privacy and security protocols.
        4. Model Integration:
        - Detail how users can train, deploy, and manage AI models.
        - Discuss support for popular ML frameworks (TensorFlow, PyTorch).
        5. APIs & SDKs:
        - Define necessary APIs for user interaction.
        - Provide SDKs in popular languages for ease of integration.
        6. Scalability & Load Balancing:
        - Discuss methods to handle increasing user demands.
        - Suggest strategies for effective load distribution.
        7. Monitoring & Maintenance:
        - Tools for monitoring system health, usage, and model performance.
        - Regular updates, patches, and potential expansion considerations.
        8. Billing & Metering:
        - Mechanisms for tracking usage and charging users.
        - Suggestions for pricing models (e.g., pay-as-you-go, subscription).
        9. Deployment:
        - Steps for deploying the PAAS as a cloud-native service.
        - Highlight CI/CD practices for smooth updates and rollbacks.
        10. Documentation & Tutorials:
        - User guides, API documentation, and sample projects.
        11. Communication & Support:
        - Setup a system for user feedback, support, and regular communication.
        """,
        # add more project types as needed...
    },
    "GPT-4-Turbo": {
        "Assistant": """
        First, assess the details in '{prompt}' to determine if they are suitable for developing and deploying an AI Assistant. Explain your assessment clearly, focusing on the following:
        - Project Scope: How well does '{prompt}' align with the objectives and functionalities of an AI Assistant?
        - Feasibility: Are the goals outlined in '{prompt}' achievable with an AI Assistant?
        - Limitations: Are there any constraints or challenges in '{prompt}' that might affect the successful delivery of an AI Assistant?

        If '{prompt}' is not suitable for an AI Assistant, clearly state this and provide alternative suggestions or recommendations for the type of AI project that would be more appropriate.
        
        If '{prompt}' is applicable, proceed to draft a comprehensive project plan for developing and deploying an AI Assistant. Structure your answer to ensure a close fit between the project as described in '{prompt}' and an AI Assistant solution. In your plan, take into account challenges, unique aspects, and innovative strategies that are most appropriate for '{prompt}':

        1. Initialization, including:
        - Tech Assessment: Enumerate resources, servers, APIs, costs, and essential libraries.
        2. Prerequisites, including:
        - API Key: Obtain a key for your chosen model.
        - Tech Stack: Set up Python, Flask, and necessary libraries.
        3. Backend, including:
        - API: Set up Flask, integrate the API with asynchronous calls, and manage the API key securely.
        - Errors: Handle potential API issues.
        - Security: Add caching, rate limiting, and endpoint protections.
        4. Frontend, including:
        - Design: Make a user-centric interface with mobile and browser considerations.
        5. Testing:
        6. Deployment, including:
        - Platform: Choose an appropriate cloud provider.
        - Pre-deployment: Store secrets, optimize for live environment.
        7. Post-Deployment, including:
        - Maintenance: Schedule updates or API changes.
        8. Documentation, including:
        - Tech Docs: Cover architecture and integrations.
        """,
        "POC": """
        First, assess the details in '{prompt}' to determine if they are suitable for developing and deploying an AI Proof-Of-Concept (PoC). Explain your assessment clearly, focusing on the following:
        - Project Scope: How well does '{prompt}' align with the objectives and functionalities of an AI PoC?
        - Feasibility: Are the goals outlined in '{prompt}' achievable with a PoC?
        - Limitations: Are there any constraints or challenges in '{prompt}' that might affect the successful delivery of a PoC?
        
        If '{prompt}' is not suitable for a PoC, clearly state this and provide alternative suggestions or recommendations for the type of AI project that would be more appropriate.
        
        If '{prompt}' is applicable, based on the details in '{prompt}', explain how to develop and deploy an AI Proof-Of-Concept (PoC). Your audience is AI engineers at OpenAI, Google, and Meta. Please provide accurate technical detail regarding '{prompt}' and cover the following:
        1. Initialization:
        - Goal: Define the PoC's primary objective.
        - Stakeholders: Recognize key participants and their needs.
        - Constraints: Understand time, budget, and resource limits.
        2. Data Handling:
        - Sources: Determine the data origin.
        - Preparation: Clean and process the data.
        - Segmentation: Split data for training and testing.
        3. Model Strategy:
        - Potential Models: Identify suitable AI models.
        - Baseline: Set performance benchmarks with a basic model.
        - Training: Educate selected models on the dataset.
        4. Evaluation:
        - Key Metrics: Select metrics for performance assessment.
        - Testing: Gauge models using the test dataset.
        - Refinement: Adjust models based on feedback.
        5. Visualization:
        - Data Patterns: Display data characteristics.
        - Outcomes: Depict model results.
        - Comparisons: Contrast results if multiple models are used.
        6. Documentation:
        - Objective: Reaffirm the PoC's goal.
        - Methods: Describe the process and tools used.
        - Insights: Share findings and potential limitations.
        7. Stakeholder Interaction:
        - Presentation: Offer a PoC demonstration.
        - Feedback Collection: Receive stakeholder input.
        - Future Discussion: Address next steps or full-scale progression.
        8. Wrap-up:
        - Summary: Conclude the PoC's outcomes.
        - Recommendations: Suggest the viability of further development.
        - Decision: Decide on continuation, modification, or discontinuation.
        """,
        "Model": """
        First, assess the details in '{prompt}' to determine if they are suitable for AI model selection, construction, implementation, evaluation, and documentation. Explain your assessment clearly, focusing on the following:
        - Project Scope: How well does '{prompt}' align with the objectives and functionalities of AI model development?
        - Feasibility: Are the goals outlined in '{prompt}' achievable with the types of models mentioned?
        - Limitations: Are there any constraints or challenges in '{prompt}' that might affect the model development?

        If '{prompt}' is not suitable for AI model development, clearly state this and provide alternative suggestions or recommendations for the type of AI project that would be more appropriate.
        
        If '{prompt}' is applicable, based on the details in '{prompt}', guide on AI model selection, construction, implementation, evaluation, and documentation. Adjust recommendations based on the model class from '{prompt}'. Ensure to cover:
        1. Model Selection:
        - Analyze requirements.
        - Suggest AI model classes (e.g., Supervised, Unsupervised).
        - Recommend specific models (CNN, RNN, Transformers, etc.).
        2. Data Preparation:
        - Guide on collecting and preprocessing data.
        - Discuss dataset splitting (training, validation, test sets).
        3. Model Construction:
        - Define model architecture.
        - Mention crucial hyperparameters.
        - Suggest libraries (TensorFlow, PyTorch, etc.).
        4. Implementation:
        - Offer coding best practices.
        - Discuss training and optimization techniques.
        5. Testing & Evaluation:
        - Propose metrics for evaluation (accuracy, F1-score, etc.).
        - Emphasize validation and interpretation techniques.
        6. Model Variations:
        - Touch upon Supervised, Unsupervised, and Reinforcement Learning.
        - Discuss transfer learning and pre-trained models.
        7. Deployment:
        - Discuss serving the model.
        - Touch on scalability and continuous learning.
        8. Documentation:
        - Guide on model description, results, and conclusion.
        9. Communication:
        - Stress updates to stakeholders and clear documentation.
        """,
        "PAAS": """
        First, assess the details in '{prompt}' to determine if they are suitable for constructing, implementing, and optimizing an AI Platform As A Service (PAAS). Explain your assessment clearly, focusing on the following:
        - Project Scope: How well does '{prompt}' align with the objectives and functionalities of a PAAS?
        - Feasibility: Are the goals outlined in '{prompt}' achievable with a PAAS?
        - Limitations: Are there any constraints or challenges in '{prompt}' that might affect the successful delivery of a PAAS?

        If '{prompt}' is not suitable for a PAAS, clearly state this and provide alternative suggestions or recommendations for the type of AI project that would be more appropriate.
        
        If '{prompt}' is applicable, given the specifics in '{prompt}', offer guidance on constructing, implementing, and optimizing an AI Platform As A Service (PAAS). Adjust recommendations based on the provided details in '{prompt}'. Ensure to include:
        1. Service Design:
        - Define core functionalities and capabilities of the PAAS.
        - Establish user roles (e.g., admins, developers, end-users).
        2. Infrastructure Setup:
        - Suggest optimal cloud providers (e.g., AWS, Azure, GCP).
        - Discuss containerization (Docker) and orchestration (Kubernetes).
        3. Data Handling:
        - Guide on data storage, retrieval, and scalability solutions.
        - Address data privacy and security protocols.
        4. Model Integration:
        - Detail how users can train, deploy, and manage AI models.
        - Discuss support for popular ML frameworks (TensorFlow, PyTorch).
        5. APIs & SDKs:
        - Define necessary APIs for user interaction.
        - Provide SDKs in popular languages for ease of integration.
        6. Scalability & Load Balancing:
        - Discuss methods to handle increasing user demands.
        - Suggest strategies for effective load distribution.
        7. Monitoring & Maintenance:
        - Tools for monitoring system health, usage, and model performance.
        - Regular updates, patches, and potential expansion considerations.
        8. Billing & Metering:
        - Mechanisms for tracking usage and charging users.
        - Suggestions for pricing models (e.g., pay-as-you-go, subscription).
        9. Deployment:
        - Steps for deploying the PAAS as a cloud-native service.
        - Highlight CI/CD practices for smooth updates and rollbacks.
        10. Documentation & Tutorials:
        - User guides, API documentation, and sample projects.
        11. Communication & Support:
        - Setup a system for user feedback, support, and regular communication.
        """,
        # add more project types as needed...
    },
    "PaLM-2": {
        "Assistant": """
        First, assess the details in '{prompt}' to determine if they are suitable for developing and deploying an AI Assistant. Explain your assessment clearly, focusing on the following:
        - Project Scope: How well does '{prompt}' align with the objectives and functionalities of an AI Assistant?
        - Feasibility: Are the goals outlined in '{prompt}' achievable with an AI Assistant?
        - Limitations: Are there any constraints or challenges in '{prompt}' that might affect the successful delivery of an AI Assistant?

        If '{prompt}' is not suitable for an AI Assistant, clearly state this and provide alternative suggestions or recommendations for the type of AI project that would be more appropriate.
        
        If '{prompt}' is applicable, proceed to draft a comprehensive project plan for developing and deploying an AI Assistant. Structure your answer to ensure a close fit between the project as described in '{prompt}' and an AI Assistant solution. In your plan, take into account challenges, unique aspects, and innovative strategies that are most appropriate for '{prompt}':

        1. Initialization, including:
        - Tech Assessment: Enumerate resources, servers, APIs, costs, and essential libraries.
        2. Prerequisites, including:
        - API Key: Obtain a key for your chosen model.
        - Tech Stack: Set up Python, Flask, and necessary libraries.
        3. Backend, including:
        - API: Set up Flask, integrate the API with asynchronous calls, and manage the API key securely.
        - Errors: Handle potential API issues.
        - Security: Add caching, rate limiting, and endpoint protections.
        4. Frontend, including:
        - Design: Make a user-centric interface with mobile and browser considerations.
        5. Testing:
        6. Deployment, including:
        - Platform: Choose an appropriate cloud provider.
        - Pre-deployment: Store secrets, optimize for live environment.
        7. Post-Deployment, including:
        - Maintenance: Schedule updates or API changes.
        8. Documentation, including:
        - Tech Docs: Cover architecture and integrations.
        """,
        "POC": """
        First, assess the details in '{prompt}' to determine if they are suitable for developing and deploying an AI Proof-Of-Concept (PoC). Explain your assessment clearly, focusing on the following:
        - Project Scope: How well does '{prompt}' align with the objectives and functionalities of an AI PoC?
        - Feasibility: Are the goals outlined in '{prompt}' achievable with a PoC?
        - Limitations: Are there any constraints or challenges in '{prompt}' that might affect the successful delivery of a PoC?
        
        If '{prompt}' is not suitable for a PoC, clearly state this and provide alternative suggestions or recommendations for the type of AI project that would be more appropriate.
        
        If '{prompt}' is applicable, based on the details in '{prompt}', explain how to develop and deploy an AI Proof-Of-Concept (PoC). Your audience is AI engineers at OpenAI, Google, and Meta. Please provide accurate technical detail regarding '{prompt}' and cover the following:
        1. Initialization:
        - Goal: Define the PoC's primary objective.
        - Stakeholders: Recognize key participants and their needs.
        - Constraints: Understand time, budget, and resource limits.
        2. Data Handling:
        - Sources: Determine the data origin.
        - Preparation: Clean and process the data.
        - Segmentation: Split data for training and testing.
        3. Model Strategy:
        - Potential Models: Identify suitable AI models.
        - Baseline: Set performance benchmarks with a basic model.
        - Training: Educate selected models on the dataset.
        4. Evaluation:
        - Key Metrics: Select metrics for performance assessment.
        - Testing: Gauge models using the test dataset.
        - Refinement: Adjust models based on feedback.
        5. Visualization:
        - Data Patterns: Display data characteristics.
        - Outcomes: Depict model results.
        - Comparisons: Contrast results if multiple models are used.
        6. Documentation:
        - Objective: Reaffirm the PoC's goal.
        - Methods: Describe the process and tools used.
        - Insights: Share findings and potential limitations.
        7. Stakeholder Interaction:
        - Presentation: Offer a PoC demonstration.
        - Feedback Collection: Receive stakeholder input.
        - Future Discussion: Address next steps or full-scale progression.
        8. Wrap-up:
        - Summary: Conclude the PoC's outcomes.
        - Recommendations: Suggest the viability of further development.
        - Decision: Decide on continuation, modification, or discontinuation.
        """,
        "Model": """
        First, assess the details in '{prompt}' to determine if they are suitable for AI model selection, construction, implementation, evaluation, and documentation. Explain your assessment clearly, focusing on the following:
        - Project Scope: How well does '{prompt}' align with the objectives and functionalities of AI model development?
        - Feasibility: Are the goals outlined in '{prompt}' achievable with the types of models mentioned?
        - Limitations: Are there any constraints or challenges in '{prompt}' that might affect the model development?

        If '{prompt}' is not suitable for AI model development, clearly state this and provide alternative suggestions or recommendations for the type of AI project that would be more appropriate.
        
        If '{prompt}' is applicable, based on the details in '{prompt}', guide on AI model selection, construction, implementation, evaluation, and documentation. Adjust recommendations based on the model class from '{prompt}'. Ensure to cover:
        1. Model Selection:
        - Analyze requirements.
        - Suggest AI model classes (e.g., Supervised, Unsupervised).
        - Recommend specific models (CNN, RNN, Transformers, etc.).
        2. Data Preparation:
        - Guide on collecting and preprocessing data.
        - Discuss dataset splitting (training, validation, test sets).
        3. Model Construction:
        - Define model architecture.
        - Mention crucial hyperparameters.
        - Suggest libraries (TensorFlow, PyTorch, etc.).
        4. Implementation:
        - Offer coding best practices.
        - Discuss training and optimization techniques.
        5. Testing & Evaluation:
        - Propose metrics for evaluation (accuracy, F1-score, etc.).
        - Emphasize validation and interpretation techniques.
        6. Model Variations:
        - Touch upon Supervised, Unsupervised, and Reinforcement Learning.
        - Discuss transfer learning and pre-trained models.
        7. Deployment:
        - Discuss serving the model.
        - Touch on scalability and continuous learning.
        8. Documentation:
        - Guide on model description, results, and conclusion.
        9. Communication:
        - Stress updates to stakeholders and clear documentation.
        """,
        "PAAS": """
        First, assess the details in '{prompt}' to determine if they are suitable for constructing, implementing, and optimizing an AI Platform As A Service (PAAS). Explain your assessment clearly, focusing on the following:
        - Project Scope: How well does '{prompt}' align with the objectives and functionalities of a PAAS?
        - Feasibility: Are the goals outlined in '{prompt}' achievable with a PAAS?
        - Limitations: Are there any constraints or challenges in '{prompt}' that might affect the successful delivery of a PAAS?

        If '{prompt}' is not suitable for a PAAS, clearly state this and provide alternative suggestions or recommendations for the type of AI project that would be more appropriate.
        
        If '{prompt}' is applicable, given the specifics in '{prompt}', offer guidance on constructing, implementing, and optimizing an AI Platform As A Service (PAAS). Adjust recommendations based on the provided details in '{prompt}'. Ensure to include:
        1. Service Design:
        - Define core functionalities and capabilities of the PAAS.
        - Establish user roles (e.g., admins, developers, end-users).
        2. Infrastructure Setup:
        - Suggest optimal cloud providers (e.g., AWS, Azure, GCP).
        - Discuss containerization (Docker) and orchestration (Kubernetes).
        3. Data Handling:
        - Guide on data storage, retrieval, and scalability solutions.
        - Address data privacy and security protocols.
        4. Model Integration:
        - Detail how users can train, deploy, and manage AI models.
        - Discuss support for popular ML frameworks (TensorFlow, PyTorch).
        5. APIs & SDKs:
        - Define necessary APIs for user interaction.
        - Provide SDKs in popular languages for ease of integration.
        6. Scalability & Load Balancing:
        - Discuss methods to handle increasing user demands.
        - Suggest strategies for effective load distribution.
        7. Monitoring & Maintenance:
        - Tools for monitoring system health, usage, and model performance.
        - Regular updates, patches, and potential expansion considerations.
        8. Billing & Metering:
        - Mechanisms for tracking usage and charging users.
        - Suggestions for pricing models (e.g., pay-as-you-go, subscription).
        9. Deployment:
        - Steps for deploying the PAAS as a cloud-native service.
        - Highlight CI/CD practices for smooth updates and rollbacks.
        10. Documentation & Tutorials:
        - User guides, API documentation, and sample projects.
        11. Communication & Support:
        - Setup a system for user feedback, support, and regular communication.
        """,
        # add more project types as needed...
    },
    "Claude-2": {
        "Assistant": """
        First, assess the details in '{prompt}' to determine if they are suitable for developing and deploying an AI Assistant. Explain your assessment clearly, focusing on the following:
        - Project Scope: How well does '{prompt}' align with the objectives and functionalities of an AI Assistant?
        - Feasibility: Are the goals outlined in '{prompt}' achievable with an AI Assistant?
        - Limitations: Are there any constraints or challenges in '{prompt}' that might affect the successful delivery of an AI Assistant?

        If '{prompt}' is not suitable for an AI Assistant, clearly state this and provide alternative suggestions or recommendations for the type of AI project that would be more appropriate.
        
        If '{prompt}' is applicable, proceed to draft a comprehensive project plan for developing and deploying an AI Assistant. Structure your answer to ensure a close fit between the project as described in '{prompt}' and an AI Assistant solution. In your plan, take into account challenges, unique aspects, and innovative strategies that are most appropriate for '{prompt}':

        1. Initialization, including:
        - Tech Assessment: Enumerate resources, servers, APIs, costs, and essential libraries.
        2. Prerequisites, including:
        - API Key: Obtain a key for your chosen model.
        - Tech Stack: Set up Python, Flask, and necessary libraries.
        3. Backend, including:
        - API: Set up Flask, integrate the API with asynchronous calls, and manage the API key securely.
        - Errors: Handle potential API issues.
        - Security: Add caching, rate limiting, and endpoint protections.
        4. Frontend, including:
        - Design: Make a user-centric interface with mobile and browser considerations.
        5. Testing:
        6. Deployment, including:
        - Platform: Choose an appropriate cloud provider.
        - Pre-deployment: Store secrets, optimize for live environment.
        7. Post-Deployment, including:
        - Maintenance: Schedule updates or API changes.
        8. Documentation, including:
        - Tech Docs: Cover architecture and integrations.
        """,
        "POC": """
        First, assess the details in '{prompt}' to determine if they are suitable for developing and deploying an AI Proof-Of-Concept (PoC). Explain your assessment clearly, focusing on the following:
        - Project Scope: How well does '{prompt}' align with the objectives and functionalities of an AI PoC?
        - Feasibility: Are the goals outlined in '{prompt}' achievable with a PoC?
        - Limitations: Are there any constraints or challenges in '{prompt}' that might affect the successful delivery of a PoC?
        
        If '{prompt}' is not suitable for a PoC, clearly state this and provide alternative suggestions or recommendations for the type of AI project that would be more appropriate.
        
        If '{prompt}' is applicable, based on the details in '{prompt}', explain how to develop and deploy an AI Proof-Of-Concept (PoC). Your audience is AI engineers at OpenAI, Google, and Meta. Please provide accurate technical detail regarding '{prompt}' and cover the following:
        1. Initialization:
        - Goal: Define the PoC's primary objective.
        - Stakeholders: Recognize key participants and their needs.
        - Constraints: Understand time, budget, and resource limits.
        2. Data Handling:
        - Sources: Determine the data origin.
        - Preparation: Clean and process the data.
        - Segmentation: Split data for training and testing.
        3. Model Strategy:
        - Potential Models: Identify suitable AI models.
        - Baseline: Set performance benchmarks with a basic model.
        - Training: Educate selected models on the dataset.
        4. Evaluation:
        - Key Metrics: Select metrics for performance assessment.
        - Testing: Gauge models using the test dataset.
        - Refinement: Adjust models based on feedback.
        5. Visualization:
        - Data Patterns: Display data characteristics.
        - Outcomes: Depict model results.
        - Comparisons: Contrast results if multiple models are used.
        6. Documentation:
        - Objective: Reaffirm the PoC's goal.
        - Methods: Describe the process and tools used.
        - Insights: Share findings and potential limitations.
        7. Stakeholder Interaction:
        - Presentation: Offer a PoC demonstration.
        - Feedback Collection: Receive stakeholder input.
        - Future Discussion: Address next steps or full-scale progression.
        8. Wrap-up:
        - Summary: Conclude the PoC's outcomes.
        - Recommendations: Suggest the viability of further development.
        - Decision: Decide on continuation, modification, or discontinuation.
        """,
        "Model": """
        First, assess the details in '{prompt}' to determine if they are suitable for AI model selection, construction, implementation, evaluation, and documentation. Explain your assessment clearly, focusing on the following:
        - Project Scope: How well does '{prompt}' align with the objectives and functionalities of AI model development?
        - Feasibility: Are the goals outlined in '{prompt}' achievable with the types of models mentioned?
        - Limitations: Are there any constraints or challenges in '{prompt}' that might affect the model development?

        If '{prompt}' is not suitable for AI model development, clearly state this and provide alternative suggestions or recommendations for the type of AI project that would be more appropriate.
        
        If '{prompt}' is applicable, based on the details in '{prompt}', guide on AI model selection, construction, implementation, evaluation, and documentation. Adjust recommendations based on the model class from '{prompt}'. Ensure to cover:
        1. Model Selection:
        - Analyze requirements.
        - Suggest AI model classes (e.g., Supervised, Unsupervised).
        - Recommend specific models (CNN, RNN, Transformers, etc.).
        2. Data Preparation:
        - Guide on collecting and preprocessing data.
        - Discuss dataset splitting (training, validation, test sets).
        3. Model Construction:
        - Define model architecture.
        - Mention crucial hyperparameters.
        - Suggest libraries (TensorFlow, PyTorch, etc.).
        4. Implementation:
        - Offer coding best practices.
        - Discuss training and optimization techniques.
        5. Testing & Evaluation:
        - Propose metrics for evaluation (accuracy, F1-score, etc.).
        - Emphasize validation and interpretation techniques.
        6. Model Variations:
        - Touch upon Supervised, Unsupervised, and Reinforcement Learning.
        - Discuss transfer learning and pre-trained models.
        7. Deployment:
        - Discuss serving the model.
        - Touch on scalability and continuous learning.
        8. Documentation:
        - Guide on model description, results, and conclusion.
        9. Communication:
        - Stress updates to stakeholders and clear documentation.
        """,
        "PAAS": """
        First, assess the details in '{prompt}' to determine if they are suitable for constructing, implementing, and optimizing an AI Platform As A Service (PAAS). Explain your assessment clearly, focusing on the following:
        - Project Scope: How well does '{prompt}' align with the objectives and functionalities of a PAAS?
        - Feasibility: Are the goals outlined in '{prompt}' achievable with a PAAS?
        - Limitations: Are there any constraints or challenges in '{prompt}' that might affect the successful delivery of a PAAS?

        If '{prompt}' is not suitable for a PAAS, clearly state this and provide alternative suggestions or recommendations for the type of AI project that would be more appropriate.
        
        If '{prompt}' is applicable, given the specifics in '{prompt}', offer guidance on constructing, implementing, and optimizing an AI Platform As A Service (PAAS). Adjust recommendations based on the provided details in '{prompt}'. Ensure to include:
        1. Service Design:
        - Define core functionalities and capabilities of the PAAS.
        - Establish user roles (e.g., admins, developers, end-users).
        2. Infrastructure Setup:
        - Suggest optimal cloud providers (e.g., AWS, Azure, GCP).
        - Discuss containerization (Docker) and orchestration (Kubernetes).
        3. Data Handling:
        - Guide on data storage, retrieval, and scalability solutions.
        - Address data privacy and security protocols.
        4. Model Integration:
        - Detail how users can train, deploy, and manage AI models.
        - Discuss support for popular ML frameworks (TensorFlow, PyTorch).
        5. APIs & SDKs:
        - Define necessary APIs for user interaction.
        - Provide SDKs in popular languages for ease of integration.
        6. Scalability & Load Balancing:
        - Discuss methods to handle increasing user demands.
        - Suggest strategies for effective load distribution.
        7. Monitoring & Maintenance:
        - Tools for monitoring system health, usage, and model performance.
        - Regular updates, patches, and potential expansion considerations.
        8. Billing & Metering:
        - Mechanisms for tracking usage and charging users.
        - Suggestions for pricing models (e.g., pay-as-you-go, subscription).
        9. Deployment:
        - Steps for deploying the PAAS as a cloud-native service.
        - Highlight CI/CD practices for smooth updates and rollbacks.
        10. Documentation & Tutorials:
        - User guides, API documentation, and sample projects.
        11. Communication & Support:
        - Setup a system for user feedback, support, and regular communication.
        """,
        # add more project types as needed...
    },
}