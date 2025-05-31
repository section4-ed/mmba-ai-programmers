# Section's AI MMBA Code Repository

Welcome to the course! This repository has all the coding assignments that you'll be completing each week. These assignments are meant to go quickly, with each one taking between 5-10 minutes. Try to do them yourself for a few minutes, then enlist the help of AI to figure it out faster.

## Getting Started

### Prerequisites
- Python 3.8 or higher installed on your computer
- pip (Python package installer) - comes with Python by default
- A code editor (preferably [Cursor](https://www.cursor.com/))

### Setting Up Your Environment

1. **Clone this repository**
   ```bash
   git clone [repository-url]
   cd curriculum_ai_advocate
   ```

2. **Create and activate a virtual environment (recommended)**

   Run the following at the this repository's root directory:

   ```bash
   # On macOS/Linux
   python3 -m venv .venv
   source .venv/bin/activate 

   # On Windows
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

3. **Install required packages**

   ```bash
   pip install -r requirements.txt
   ```

4. **Verify installation**

   ```bash
   python --version  # Should show Python 3.8 or higher
   pip list  # Should show all installed packages
   ```

### Running Python Scripts
To run any Python script in this course:
```bash
python path/to/script.py
```

If you encounter any issues:
1. Make sure your virtual environment is activated
2. Verify all requirements are installed
3. Check that you're in the correct directory
4. Ensure you have the correct Python version