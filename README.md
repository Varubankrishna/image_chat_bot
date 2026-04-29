# Local AI Chatbot (ChatGPT-like)

This project is a locally running AI chatbot that supports both text and image inputs. It is built using Python (Flask) and Ollama with the LLaVA model, allowing the system to run completely offline without any API cost.

## Features

* Chat-based interaction similar to ChatGPT
* Image upload and explanation support
* Smart input handling to avoid incorrect AI responses
* Runs locally (no internet or API dependency)

## Tech Stack

* Python (Flask)
* Ollama (LLaVA model)
* HTML, CSS, JavaScript

## How It Works

The frontend sends user input (text or image) to the Flask backend.
The backend forwards the request to the Ollama model.
The AI processes the input and returns a response, which is displayed in the UI.

## How to Run

1. Install dependencies:
   pip install flask flask-cors requests

2. Run Ollama:
   ollama run llava

3. Start the backend:
   python server.py

4. Open the frontend:
   Open chat.html in your browser

## Project Structure

* server.py → Backend (Flask API)
* chat.html → Frontend (UI)

## Future Improvements

* Chat memory (conversation history)
* Improved UI (ChatGPT-style interface)
* Unity integration for AI-powered NPCs

## Author

Varuban Krishna
