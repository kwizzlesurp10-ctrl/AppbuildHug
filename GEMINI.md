# Antigravity Project Builder

## Project Overview

**Antigravity Project Builder** is a Gradio-based web application designed to visualize software project architectures using a "zero-gravity" animated interface. It features:
- **Interactive Visualization:** An animated canvas with orbiting "orbs" representing project components (Frontend, Backend, Database, AI, etc.).
- **Dual Modes:**
    - **Demo Mode:** Generates a static, pre-defined blueprint for demonstration.
    - **Gemini Mode:** Uses Google's Gemini API to dynamically generate custom full-stack project blueprints based on user input.
- **Deployment Target:** Optimized for deployment on Hugging Face Spaces.

## Architecture

- **Backend/Frontend:** Python with `gradio`.
- **AI Integration:** `google-generativeai` library.
- **Visualization:** HTML/CSS/JavaScript (Anime.js) embedded within the Gradio interface.
- **Entry Point:** `app.py`.

## Key Files

- `app.py`: The main application entry point. Contains the Gradio UI definition, animation HTML generation, and blueprint generation logic.
- `requirements.txt`: Python dependencies (`gradio`, `google-generativeai`).
- `preview.html`: (Likely) A standalone HTML preview of the animation component.
- `HUGGINGFACE_SSH_SETUP.md`: Documentation for configuring SSH access to the Hugging Face Space.
- `HF_SPACE_SSH_COMMANDS.md`: A cheat sheet for managing the application via SSH on Hugging Face.

## Setup & Usage

### Prerequisites

- Python 3.10+
- A Google Gemini API Key (for dynamic mode)

### Installation

1.  **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running Locally

1.  **Set Environment Variables (Optional):**
    ```bash
    export GEMINI_API_KEY="your_api_key_here"
    export DEMO_MODE="false"  # Set to "true" to force demo mode
    ```

2.  **Start the Application:**
    ```bash
    python app.py
    ```

3.  **Access:**
    Open your browser to `http://localhost:7860`.

### Hugging Face Spaces Deployment

- The project is designed to be pushed to a Hugging Face Space.
- **Secrets:** Configure `GEMINI_API_KEY` in the Space's "Settings" -> "Repository secrets".
- **SSH Access:** Refer to `HUGGINGFACE_SSH_SETUP.md` for connecting to the running Space for debugging or maintenance.

## Development Conventions

- **Code Style:** Standard Python conventions.
- **UI:** Gradio Blocks API is used for layout.
- **Embedded Assets:** The animation is handled via a string-embedded HTML component (`generate_animation_html` function in `app.py`).
- **Error Handling:** The app gracefully falls back to "Demo Mode" if the Gemini API is unavailable or unconfigured.

## Troubleshooting

- **Port Conflicts:** The app defaults to port 7860. If in use, `gradio` usually tries the next available port, but explicit configuration might be needed in `app.launch()`.
- **API Issues:** If blueprints aren't generating, check the `GEMINI_API_KEY` and ensure the `google-generativeai` package is installed.
