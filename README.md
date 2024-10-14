# Flask API for LLM Inference using Ollama

This project is a simple Flask API that uses the Ollama library to perform language model inference. The API accepts a text prompt and returns a generated response using the "Moondream" model from Ollama.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Testing the API](#testing-the-api)
- [Example](#example)

## Requirements
- Python 3.10+
- Flask library
- Ollama library
- Moondream 2 model installed in Ollama

## Installation

1. Clone this repository or download the code files.
2. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required libraries:
   ```bash
   pip install flask ollama
   ```

4. Download and setup [Ollama installer](https://github.com/ollama/ollama)
   
6. Pull the Moondream model from Ollama:
   ```bash
   ollama pull moondream
   ```

## Usage

1. Run the Flask app:
   ```bash
   python assignment.py
   ```

   This will start the server at `http://127.0.0.1:5000`.

2. To test the API, send a POST request to the `/inference` endpoint with a JSON payload containing the prompt.

## Testing the API

You can use `curl` to send a POST request:

```bash
curl -X POST -H "Content-Type: application/json" -d "{\"prompt\": \"Hello, how are you?\"}" http://127.0.0.1:5000/inference
```

Or use any HTTP client like **Postman** or **Insomnia** to test the endpoint.

## Example

### Input
```json
{
    "prompt": "Hello, how are you?"
}
```

### Output
The API responds with a JSON object containing the model name and response:
```json
{
    "model": "moondream",
    "response": "I'm doing great, thank you! How can I assist you today?"
}
```

## Error Handling

- If the `prompt` is not provided in the request, the API will return:
    ```json
    {
        "error": "no input"
    }
    ```

- If an internal error occurs (e.g., a model error), the API will return:
    ```json
    {
        "error": "error message"
    }
    ```

## Notes

- Make sure to have the "Moondream" model downloaded and set up correctly with the Ollama library.
- The Flask app runs in debug mode by default. Disable debug mode in a production environment.
