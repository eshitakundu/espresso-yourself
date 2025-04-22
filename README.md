[![Streamlit App](https://img.shields.io/badge/Live_App-Click_Here-brightgreen?style=for-the-badge)](https://espress.streamlit.app/)

# Espresso Yourself Café

A Streamlit-powered conversational app where you can rant to AI characters in a coffee shop setting.

![Café Atmosphere](static/bg.png)

## Features

- **Multiple AI Characters**: Chat with three distinct personalities:
  - 🧑🏻‍🍳 **Barista**: A warm, supportive listener who offers comforting advice
  - 🧍🏻‍♀️ **Waitress**: An anxious but well-meaning character who tries her best
  - 🧑🏻‍🦰 **Customer**: A sarcastic regular who delivers brutally honest feedback

- **Conversation Memory**: Each character remembers your previous messages and maintains context
- **Typewriter Effect**: Responses appear with a realistic typing animation
- **Character-Specific Styling**: Different avatars and personalities for each character

## Architecture

The app uses:
- **Streamlit**: For the UI framework
- **LangChain**: For managing conversation chains and memory
- **Google Gemini API**: For AI text generation
- **Python**: Core programming language

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/eshitakundu/espresso-yourself.git
   cd espresso-yourself
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your API key:
   - Create a `.env` file in the project root
   - Add your Google Gemini API key: `GOOGLE_API_KEY=your_api_key_here`

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open your browser at `http://localhost:8501`

3. Select a character and start ranting!

## Project Structure

- `app.py`: Main Streamlit application with UI components
- `chains.py`: LLM configuration and chain setup
- `memory.py`: Conversation memory management
- `prompts.py`: Character-specific prompt templates
- `static/`: Contains UI assets

## Development

### Debug Mode

The app includes a debug panel to inspect conversation memory:
1. Check "Show debug info" in the sidebar
2. View the memory contents as JSON
3. Clear memory if needed

### Adding New Characters

To add a new character:
1. Add prompt template in `prompts.py`
2. Add avatar in `app.py`
3. Add character button in the UI

## License

MIT License

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [LangChain](https://www.langchain.com/) and [Google Gemini](https://deepmind.google/technologies/gemini/)
