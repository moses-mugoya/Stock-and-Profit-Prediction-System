from .models import Company
from django.shortcuts import get_object_or_404
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def draw_graph(request, id, x, y):
    company = get_object_or_404(Company, id=id)
    file = company.file
    data = pd.read_csv(file)
    X = data[x].values.reshape(-1, 1)
    y = data[y].values.reshape(-1, 1)
    reg = LinearRegression()
    predictions = reg.predict(X)

    plt.figure(figsize=(16, 8))
    plt.scatter(
        data[x],
        data[y],
        c='black'
    )
    plt.plot(
        data[x],
        predictions,
        c='blue',
        linewidth=2
    )
