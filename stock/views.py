from django.shortcuts import render, get_object_or_404
from .models import Company
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import statsmodels.api as sm
from statistics import mean
from .forms import UserInputFormSales, UserInputFormProfit, UserInputFormDemand, InvestorsForm
from .graph import draw_graph


def index(request):
    return render(request, 'stock/index.html')


def detail(request, id, slug):
    company = get_object_or_404(Company, id=id, slug=slug)
    return render(request, 'stock/detail.html', {'company': company})


def predict_sales(request, id):
    company = get_object_or_404(Company, id=id)
    file = company.file
    user_value = 0
    checker = True
    data = pd.read_csv(file)
    visual = data.head()
    reg = LinearRegression()
    X = data['People'].values.reshape(-1, 1)
    y = data['Sales'].values.reshape(-1, 1)
    mean_value = np.average(y)
    print(mean_value)
    reg.fit(X, y)
    if request.method == 'POST':
        user_sales = UserInputFormSales(data=request.POST)
        invest_form = InvestorsForm(data=request.POST)
        if invest_form.is_valid():
            new_form = invest_form.save(commit=False)
            new_form.user = request.user
            new_form.company = company
            new_form.save()
        if user_sales.is_valid():
            user_value = user_sales.cleaned_data['user_input']
            checker = False

    else:
        user_sales = UserInputFormSales()
    invest_form = InvestorsForm()
    predict = reg.intercept_[0] + reg.coef_[0][0] * float(user_value)
    percentage = ((predict-mean_value)/mean_value)*100
    return render(request, 'stock/predict_sales.html', {'percentage': percentage,
                                                        'predict': predict,
                                                        'visual': visual,
                                                        'company': company,
                                                        'invest_form':invest_form,
                                                        'user_sales': user_sales,
                                                        'checker': checker})


def predict_profit(request, id):
    company = get_object_or_404(Company, id=id)
    file = company.file
    user_value = 0
    checker = True
    name = ""
    data = pd.read_csv(file)
    visual = data.head()
    reg = LinearRegression()
    X = data['Sales'].values.reshape(-1, 1)
    y = data['Profit'].values.reshape(-1, 1)
    mean_value = np.average(y)
    print(mean_value)
    reg.fit(X, y)
    if request.method == 'POST':
        user_sales = UserInputFormProfit(data=request.POST)
        invest_form = InvestorsForm(data=request.POST)
        if invest_form.is_valid():
            new_form = invest_form.save(commit=False)
            new_form.user = request.user
            new_form.company = company
            new_form.save()
        if user_sales.is_valid():
            user_value = user_sales.cleaned_data['user_input']
            checker = False

    else:
        user_sales = UserInputFormProfit()
    invest_form = InvestorsForm()
    predict = reg.intercept_[0] + reg.coef_[0][0] * float(user_value)
    percentage = ((predict - mean_value) / mean_value) * 100
    return render(request, 'stock/predict_profit.html', {'percentage': percentage,
                                                         'predict': predict,
                                                         'visual': visual,
                                                         'company': company,
                                                         'invest_form': invest_form,
                                                         'user_sales': user_sales,
                                                         'checker': checker,
                                                         'name': name})


def predict_demand(request, id):
    company = get_object_or_404(Company, id=id)
    file = company.file
    user_value = 0
    checker = True
    data = pd.read_csv(file)
    visual = data.head()
    reg = LinearRegression()
    X = data['Demand'].values.reshape(-1, 1)
    y = data['Supply'].values.reshape(-1, 1)
    mean_value = np.average(y)
    print(mean_value)
    reg.fit(X, y)
    if request.method == 'POST':
        user_sales = UserInputFormDemand(data=request.POST)
        invest_form = InvestorsForm(data=request.POST)
        if invest_form.is_valid():
            new_form = invest_form.save(commit=False)
            new_form.user = request.user
            new_form.company = company
            new_form.save()
        if user_sales.is_valid():
            user_value = user_sales.cleaned_data['user_input']
            checker = False

    else:
        user_sales = UserInputFormDemand()
    invest_form = InvestorsForm()
    predict = reg.intercept_[0] + reg.coef_[0][0] * float(user_value)
    percentage = ((predict - mean_value) / mean_value) * 100
    return render(request, 'stock/demands.html', {'percentage': percentage,
                                                  'predict': predict,
                                                  'visual': visual,
                                                  'invest_form': invest_form,
                                                  'company': company,
                                                  'user_sales': user_sales,
                                                  'checker': checker})


def investor(request, id):
    compan = get_object_or_404(Company, id=id)
    if request.method == 'POST':
        invest_form = InvestorsForm(data=request.POST)
        if invest_form.is_valid():
            new_form = invest_form.save(commit=False)
            new_form.user = request.user
            new_form.save()
    else:
        invest_form = InvestorsForm()
    return render(request, 'stock/i.html', {'invest_form': invest_form, 'compan': compan})


def graphics_profit(request, id):
    compony = get_object_or_404(Company, id=id)
    file = compony.file
    data = pd.read_csv(file)
    X = data['People'].values.reshape(-1, 1)
    y = data['Sales'].values.reshape(-1, 1)
    reg = LinearRegression()
    reg.fit(X, y)
    predictions = reg.predict(X)

    plt.figure(figsize=(16, 8))
    plt.scatter(
        data['People'],
        data['Sales'],
        c='black'
    )
    plt.plot(
        data['People'],
        predictions,
        c='blue',
        linewidth=2
    )
    plt.xlabel("Profit")
    plt.ylabel("Sales")
    plt.show()
    return render(request, 'stock/p.html', {'compony': compony})


def graphics_demand(request, id):
    compony = get_object_or_404(Company, id=id)
    file = compony.file
    data = pd.read_csv(file)
    X = data['Demand'].values.reshape(-1, 1)
    y = data['Supply'].values.reshape(-1, 1)
    reg = LinearRegression()
    reg.fit(X, y)
    predictions = reg.predict(X)

    plt.figure(figsize=(16, 8))
    plt.scatter(
        data['Demand'],
        data['Supply'],
        c='black'
    )
    plt.plot(
        data['Demand'],
        predictions,
        c='blue',
        linewidth=2
    )
    plt.xlabel("Demand")
    plt.ylabel("Supply")
    plt.show()
    return render(request, 'stock/p.html', {'compony': compony})


def graphics_sales(request, id):
    compony = get_object_or_404(Company, id=id)
    file = compony.file
    data = pd.read_csv(file)
    X = data['Sales'].values.reshape(-1, 1)
    y = data['Profit'].values.reshape(-1, 1)
    reg = LinearRegression()
    reg.fit(X, y)
    predictions = reg.predict(X)

    plt.figure(figsize=(16, 8))
    plt.scatter(
        data['Sales'],
        data['Profit'],
        c='black'
    )
    plt.plot(
        data['Sales'],
        predictions,
        c='blue',
        linewidth=2
    )
    plt.xlabel("Sales")
    plt.ylabel("Profit")
    plt.show()
    return render(request, 'stock/s.html', {'compony': compony})















