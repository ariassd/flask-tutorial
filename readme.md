# Flask Tutorial Project

This is a small Flask example project with:

- A home page at `/`
- A dynamic hello page at `/hello/<name>/<last_name>`
- A goodbye endpoint at `/goodby/<name>/<last_name>`
- A BMI calculator at `/bmi-calc`

## Requirements

- Python 3
- `pip`

## Install Dependencies

From the project folder:

```bash
cd flask-tutorial
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

If you already have the virtual environment created, just activate it:

```bash
cd flask-tutorial
source .venv/bin/activate
```

## Run The Project

Start the Flask app with:

```bash
cd flask-tutorial
source .venv/bin/activate
python main.py
```

The server will run on:

```text
http://127.0.0.1:5000
```

## Available Routes

- `/` : Home page
- `/author` : Author page text
- `/copyright` : Copyright page text
- `/post/<name>` : Shows a post name
- `/hello/<name>/<last_name>` : Renders the styled hello page
- `/goodby/<name>/<last_name>` : Returns a goodbye message
- `/bmi-calc` : BMI calculator form

## Example URLs

```text
http://127.0.0.1:5000/
http://127.0.0.1:5000/hello/luis/perez
http://127.0.0.1:5000/goodby/luis/perez
http://127.0.0.1:5000/bmi-calc
```
