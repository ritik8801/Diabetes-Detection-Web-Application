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
        fig.savefig("{}/histogram.png".format(self.path))

    def heatmap_observation(self):
        fig, ax = plt.subplots()
        d = self.data[['Pregnancies', 'Glucose', 'BloodPressure',
       'SkinThickness', 'Insulin',
       'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']]
        dataplot = sns.heatmap(d.corr(), annot=True, cmap="YlGnBu")
        fig.savefig("{}/heatmap.png".format(self.path))