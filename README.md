# exhibitors-scrapper
A tiny scrapper of techspodenver.com with feature to search for more data about companies, using ChatGPT

## Architecture
![architecture](.docs/FlowDiagram.png)

## Setup and Run

### Setup
- Install Python 3.8 or later
- Install project dependencies:
```bash
pip install -r requirements.txt
```

### Setup with Pipenv
If you prefer to use Pipenv for managing dependencies, you can follow these steps:
1. Install Pipenv if it's not already installed: 
```bash
pip install pipenv
```
2. Navigate to the project's directory and install the dependencies using Pipenv: 
```bash
pipenv sync
```
3. Install the development packages using Pipenv: 
```bash
pipenv install --dev
```
4. Run the project using Pipenv: 
```bash
pipenv run python main.py
```

### Run
- Set environment variables in .env file
- Run scrapper:
```bash
python main.py
```

After getting results, you can import exhibitors.csv file in Google Spreadsheet