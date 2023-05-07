from flask import Flask
import pandas as pd

df = pd.read_csv('.data/diagnoses2019.csv')
app = Flask(__name__)

app.route('/', methods=["GET"])
def home():
        return 'this is a API service for MN ICD code details'
