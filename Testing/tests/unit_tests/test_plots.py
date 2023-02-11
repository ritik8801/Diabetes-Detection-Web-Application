"""
Test Cases for plots
"""
import pytest
import os
import pandas as pd
from src.preprocessing.plots import Plot


def test_hist_observation(mocker):
    mocker.patch("src.preprocessing.plots.Plot.hist_observation", return_value=None)
    path = "https://raw.githubusercontent.com/ritik8801/Diabetes-Detection-Web-Application/main/Testing/tests/unit_tests/test_data/histogram.png"
    data = pd.read_csv("https://raw.githubusercontent.com/ritik8801/Diabetes-Detection-Web-Application/main/Testing/tests/unit_tests/test_data/sample.csv")

def test_heatmap_observation(mocker):
    mocker.patch("src.preprocessing.plots.Plot.heatmap_observation", return_value=None)
    path = "https://raw.githubusercontent.com/ritik8801/Diabetes-Detection-Web-Application/main/Testing/tests/unit_tests/test_data/heatmap.png"
    data = pd.read_csv("https://raw.githubusercontent.com/ritik8801/Diabetes-Detection-Web-Application/main/Testing/tests/unit_tests/test_data/sample.csv")
    
