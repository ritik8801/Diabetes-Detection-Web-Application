"""
Test Cases for plots
"""
import pytest
import os
import pandas as pd
from src.preprocessing.plots import Plot


def test_hist_observation(mocker):
    mocker.patch("src.preprocessing.plots.Plot.hist_observation", return_value=None)
    path = "https://raw.githubusercontent.com/ritik8801/Diabetes-Detection-Web-Application/main/Testing/tests/unit_tests/test_data/"
    data = pd.read_csv("https://raw.githubusercontent.com/ritik8801/Diabetes-Detection-Web-Application/main/Testing/tests/unit_tests/test_data/sample.csv")
    p = Plot(data, path)
    plot_path = "https://raw.githubusercontent.com/ritik8801/Diabetes-Detection-Web-Application/main/Testing/tests/unit_tests/test_data/histogram.png"
    if os.path.isfile(plot_path):
        with open(plot_path, 'rb') as f:
            plot_content = f.read()
        assert plot_content, "Plot content is empty"
    else:
        raise FileNotFoundError(f"{plot_path} not found")
    

def test_heatmap_observation(mocker):
    mocker.patch("src.preprocessing.plots.Plot.heatmap_observation", return_value=None)
    path = "https://raw.githubusercontent.com/ritik8801/Diabetes-Detection-Web-Application/main/Testing/tests/unit_tests/test_data/"
    data = pd.read_csv("https://raw.githubusercontent.com/ritik8801/Diabetes-Detection-Web-Application/main/Testing/tests/unit_tests/test_data/sample.csv")
    p = Plot(data, path)
    plot_path = "https://raw.githubusercontent.com/ritik8801/Diabetes-Detection-Web-Application/main/Testing/tests/unit_tests/test_data/heatmap.png"
    if os.path.isfile(plot_path):
        with open(plot_path, 'rb') as f:
            plot_content = f.read()
        assert plot_content, "Plot content is empty"
    else:
        raise FileNotFoundError(f"{plot_path} not found")

    
