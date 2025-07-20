# chatbot-page-practice

his project is a simple chat interface design for a Chat Bot. There is no fine tuning or Retrieval-Augmented Generation (RAG) involved. It is suitable for those who want to learn or experiment with basic chat bot UI design.

## Project Structure

```
chat_bot/
  backend/           # Backend code (FastAPI)
    main.py
    model.py
  frontend/          # Files for the chat web page
    index.html
    style.css
    bg.jpg
    bgmusic.mp3
    pop1.mp3
    pop2.mp3
  run.py             # Script to run backend (uvicorn)
```

## How to Run the Project

### 1. Install dependencies (Python 3.8+ recommended)

```bash
pip install fastapi uvicorn
```

### 2. Run the backend server

```bash
python run.py
```

The server will start at `http://127.0.0.1:8000`

### 3. Open the chat web page

Open `frontend/index.html` in your web browser (double-click or right-click and choose Open with Browser).

---

**Note:**
- This project does not connect to any real AI model or database.
- No model fine tuning or RAG techniques are used.
- Suitable for UI/UX prototyping or as a starting point for further development. 
