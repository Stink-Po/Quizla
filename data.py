import requests

data = requests.get(url="https://opentdb.com/api.php?amount=20&type=boolean")
data.raise_for_status()
question_data = data.json()["results"]

