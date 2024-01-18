# OpenAI Chatbot with FastAPI

This repository contains a simple application that utilizes the OpenAI API to build a chatbot using FastAPI in the backend and a basic web interface in the frontend.

## Setup Instructions

### Clone the Repository

    ```bash
    git clone https://github.com/YourUsername/openai-fastapi-chatbot.git
    cd openai-fastapi-chatbot
    ```

### Environment Setup
#### Create a conda environment:
    ```bash
    conda create --name myenv python=3.8
    ```
#### Activate the conda environment:
    ```bash
    conda activate myenv
    ```
#### Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
### OpenAI API Key Setup
Get your OpenAI API key and set it as an environment variable:

    ```bash
    export YOUR_API_KEY=your_actual_api_key
    ```
### Run the Application
    ```bash
    uvicorn main:app --reload
    ```
The application will be accessible at http://127.0.0.1:8000.

### Usage

Open the user interface in your web browser.
Type a message and click "Send" to interact with the chatbot.

### Contributions

Contributions are welcome! If you find any issues or have improvements, please create an issue or send a pull request.