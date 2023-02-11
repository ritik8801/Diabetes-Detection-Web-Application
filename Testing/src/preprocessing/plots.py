# import global libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Plot:

    def __init__(self, data, path):
        self.data = data
        self.path = path
        self.hist_observation()
        self.heatmap_observation()

    def hist_observation(self):
        fig, ax = plt.subplots()
        self.data[['Insulin', 'Glucose', 'BloodPressure',]].hist(bins=30, figsize=(1500,1000), ax=ax)
        path = "https://raw.githubusercontent.com/ritik8801/Diabetes-Detection-Web-Application/main/Testing/tests/unit_tests/test_data/histogram.png"
        fig.savefig(path)

    def heatmap_observation(self):
        fig, ax = plt.subplots()
        d = self.data[['Pregnancies', 'Glucose', 'BloodPressure',
       'SkinThickness', 'Insulin',
       'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']]
        dataplot = sns.heatmap(d.corr(), annot=True, cmap="YlGnBu")
        path = "https://raw.githubusercontent.com/ritik8801/Diabetes-Detection-Web-Application/main/Testing/tests/unit_tests/test_data/heatmap.png"
        fig.savefig(path)
