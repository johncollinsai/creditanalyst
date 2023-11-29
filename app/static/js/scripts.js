document.addEventListener('DOMContentLoaded', function () {
    const promptForm = document.getElementById('prompt-form');
    const resultElement = document.getElementById('result');
    const skeletonScreen = document.getElementById('skeleton-screen');
    const spinner = document.querySelector('.spinner');
    const submitButton = document.querySelector('.circle-btn');
    const promptTextArea = document.getElementById('prompt');
    const modal = document.querySelector('.project-selection-modal'); // This is the only modal declaration
    const button = document.querySelector('.open-modal-btn');
    const projects = document.querySelectorAll('#project-selection-modal .project img, #project-selection-modal .project p');
    const models = document.querySelectorAll('#model-selection-modal .project img, #model-selection-modal .project p');
    const modelButton = document.getElementById('open-model-modal-btn');
    const projectButton = document.getElementById('open-project-modal-btn');
    const modelModal = document.getElementById('model-selection-modal');
    const projectModal = document.getElementById('project-selection-modal');
    let model; // Declare model variable
    let projectType; // Declare projectType variable
    let projectOptions = document.getElementsByClassName("project-option");
    let openModalBtn = document.getElementById("open-modal-btn");
    
    // Function to capture the model description (i.e., model) and pass it to my Python function
    models.forEach(modelElement => {
        modelElement.addEventListener('click', (e) => {
            // Remove 'active' class from the selected model indicator
            document.getElementById('selected-model').classList.remove('active');

            // Remove 'active' class from all models
            models.forEach(el => el.closest('.project').classList.remove('active'));

            const selectedModelElement = e.target.closest('.project');
            const description = selectedModelElement.dataset.description;
            model = description;

            // Add 'active' class to the selected model
            selectedModelElement.classList.add('active');

            // Update the text content of the selected-model indicator
            document.getElementById('selected-model').textContent = 'Selected model: ' + description;

            // Highlight the selected model indicator
            document.getElementById('selected-model').classList.add('active');
        });
    });

    // Function to capture the project description (i.e., project_type) and pass it to my Python function
    projects.forEach(project => {
        project.addEventListener('click', (e) => {
            // Remove 'active' class from the selected project indicator
            document.getElementById('selected-project').classList.remove('active');

            // Remove 'active' class from all projects
            projects.forEach(el => el.closest('.project').classList.remove('active'));

            const selectedProjectElement = e.target.closest('.project');
            const description = selectedProjectElement.dataset.description;
            projectType = description;

            // Add 'active' class to the selected project
            selectedProjectElement.classList.add('active');

            // Update the text content of the selected-project indicator
            document.getElementById('selected-project').textContent = 'Selected project: ' + description;

            // Highlight the selected project indicator
            document.getElementById('selected-project').classList.add('active');
        });
    });

    // Function adding animation for the modal opening and positioning 
    function openModal(e, modalElement) {
        const rect = e.target.getBoundingClientRect();
        modalElement.style.left = rect.right + 'px';
        modalElement.style.top = (window.scrollY + rect.bottom) + 'px';
        modalElement.style.display = 'grid';
    }
    
    modelButton.addEventListener('click', (e) => openModal(e, modelModal));
    projectButton.addEventListener('click', (e) => openModal(e, projectModal));
    
    // Function to keep both modals open unless a click event happens outside both modals. 
    document.addEventListener('click', (e) => {
        // Check if click is outside both modals and not on the buttons that open them
        if (e.target !== modelModal && !modelModal.contains(e.target) && e.target !== modelButton &&
            e.target !== projectModal && !projectModal.contains(e.target) && e.target !== projectButton) {
            
            // If it's an outside click, hide both modals
            modelModal.style.display = 'none';
            projectModal.style.display = 'none';
        }
    });  

    button.addEventListener('click', (e) => {
        const rect = e.target.getBoundingClientRect(); // Get the button's position
        modal.style.left = rect.right + 'px'; // Position the modal to the right of the button
        modal.style.top = (window.scrollY + rect.bottom) + 'px'; // Align the modal's top edge with the button's bottom
        modal.style.display = 'grid'; // Show the modal as a grid
    }); 

    function updateSubmitButtonColor() {
        if (promptTextArea.value.trim() !== '') {
            submitButton.style.backgroundColor = '#6f42c1';
        } else {
            submitButton.style.backgroundColor = '#b3b3b3';
        }
    }

    updateSubmitButtonColor();
    
    promptTextArea.addEventListener('input', function() {
        this.style.height = 'auto';
        this.style.height = this.scrollHeight + 'px';
    });

    promptTextArea.addEventListener('keydown', function(event) {
        if (event.key === 'Enter' && !event.shiftKey) {
            event.preventDefault(); // prevent the new line from being added
            promptForm.dispatchEvent(new Event('submit')); // submit the form
        }
    });    

    function displayResult(result) {
        resultElement.innerHTML = result;
    }

    function displayError(error, element) {
        element.innerHTML = `<div class="alert alert-danger" role="alert">${error}</div>`;
    }

    function toggleSpinner(visible) {
        spinner.style.display = visible ? 'flex' : 'none';
        skeletonScreen.classList.toggle('d-none', !visible);
    }

    function fetchWithTimeout(resource, options, timeout = 60000) {
        return Promise.race([
            fetch(resource, options),
            new Promise((_, reject) =>
                setTimeout(() => reject(new Error("Request timed out")), timeout)
            ),
        ]);
    }

    // Function to get the version of the project-manager.ai and display it on the page
    window.addEventListener('load', function() {
        fetch('/get-version')
            .then(response => response.json())
            .then(data => {
            const version = data.version;
            document.querySelector('#version-info').innerHTML = `project-manager.ai may produce inaccurate information. ${version} version`;
            })
            .catch(error => console.error('An error occurred:', error));
    });

    async function fetchData(prompt, model, projectType) { // add projectType to parameters
        const formData = new FormData(promptForm); // Create formData object
        formData.append("model", model); // Append model to formData
        formData.append("project_type", projectType); // Append projectType to formData
        
        try {
            const response = await fetchWithTimeout("/get_completion", {
                method: "POST",
                body: formData,
            }, 180000);

            if (response.ok) {
                const data = await response.json();
                console.log("Data received: " + JSON.stringify(data));
                return data;
            } else {
                console.error("Error occurred while fetching data", response.statusText);
                return { success: false, error: "An error occurred while fetching data. Please try again later." };
            }
        } catch (error) {
            console.error("Error occurred while fetching data", error);
            return {
                success: false,
                error: "An error occurred while fetching data. Please try again later.",
            };
        }
    }

    async function handleFormSubmit(event) {
        event.preventDefault();
        toggleSpinner(true);
    
        const prompt = promptForm.elements["prompt"].value;
    
        try {
            const result = await fetchData(prompt, model, projectType); // pass model and projectType
    
            if (result.success) {
                displayResult(`<h3>Model: ${model}</h3><h5>Project Type: ${projectType}</h5><h5 class="text-lightgrey">Project description: ${prompt}</h5><pre class="text-white">${result.response}</pre>`);
            } else {
                displayError(result.error, resultElement);
            }
        } catch (error) {
            displayError("An error occurred while processing the request. Please try again later.", resultElement);
        }
    
        toggleSpinner(false);
    }    

    promptForm.addEventListener('submit', handleFormSubmit);
});
