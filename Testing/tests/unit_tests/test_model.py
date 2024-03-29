"""
Unit Test cases for model.py file
"""
import pytest
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import src.modelbuilding.model as M
import pandas as pd
import os
from src.modelbuilding.model import ModelBuilding
def test_split(mocker):
    mocker.patch("src.modelbuilding.model.ModelBuilding.train", return_value=None)
    mocker.patch("src.modelbuilding.model.ModelBuilding.predict", return_value=None)
    df = pd.read_csv("https://raw.githubusercontent.com/ritik8801/Diabetes-Detection-Web-Application/main/Testing/tests/unit_tests/test_data/sample.csv")
    m = ModelBuilding(df, path="test_data")
    assert isinstance(m.X_train, pd.DataFrame)
    assert isinstance(m.X_test, pd.DataFrame)
    assert isinstance(m.y_train, pd.Series)
    assert isinstance(m.y_test, pd.Series)

@pytest.fixture()
def sample_split(mocker):
    data = pd.read_csv("https://raw.githubusercontent.com/ritik8801/Diabetes-Detection-Web-Application/main/Testing/tests/unit_tests/test_data/sample.csv")
    X = data[['Pregnancies', 'Glucose', 'BloodPressure',
       'SkinThickness', 'Insulin',
       'BMI', 'DiabetesPedigreeFunction', 'Age']]
    y = data['Outcome']
    X_train, X_test, y_train, y_test = train_test_split(X, y,
        test_size=0.2)
    return X_train, X_test, y_train, y_test

def test_train(mocker, sample_split):
    mocker.patch("src.modelbuilding.model.ModelBuilding.split", return_value=None)
    mocker.patch("src.modelbuilding.model.ModelBuilding.predict", return_value=None)
    df = pd.read_csv("https://raw.githubusercontent.com/ritik8801/Diabetes-Detection-Web-Application/main/Testing/tests/unit_tests/test_data/sample.csv")
    print("sample split")
    print(sample_split[0])
    m = ModelBuilding(df, X_train= sample_split[0], X_test=sample_split[1],
    y_train=sample_split[2], y_test=sample_split[3], path="test_data")
    assert m.rcb is not None
