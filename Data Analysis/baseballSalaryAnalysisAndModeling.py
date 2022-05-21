# -*- coding: utf-8 -*-
"""
Created on Sat May 14 14:49:58 2022

@author: Andre Tonkovidov
"""
# Library and package imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import scatter_matrix
#from pandas import set_option
from pandas import read_csv
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE
import statsmodels.api as sm
from matplotlib import pyplot
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

# Reading dataset and inserting column names
filepath = 'C:/Users/Andre/Python Projects/Mission College/Final/'
filename = 'Baseball_salary.csv'
data = read_csv(filepath + filename)

# Cleaning the data
data.isnull().any()
data.dropna(inplace = True)

# Creating input and output dataframes
X = data.drop(["Salary"], axis=1)
Y = data.drop(data.columns[0:19], axis=1)
Y.drop(["NewLeague"], axis=1, inplace = True)

# Checking for categorical data
X.dtypes

# Dropping columns that contain categorical data, except League column
X.drop(["Unnamed: 0", "Division", "NewLeague"], axis=1, inplace = True)
X.dtypes

# Replacing categorical data with integers (A = 1, N = 2)
X.replace('A', 1, inplace = True)
X.replace('N', 2, inplace = True)
X.dtypes

# Looking at descriptive statistics
X.describe()

# Plotting histograms of all columns
X.hist()
plt.show()

# Attempting log transformation of candidate columns
# Had to do one-by-one to figure out which columns worked and which didn't
Xlog1 = np.log(X['CAtBat'])
Xlog2 = np.log(X['CHits'])
Xlog3 = np.log(X['CRBI'])
Xlog4 = np.log(X['CRuns'])
Xlog5 = np.log(X['CWalks'])
Xlog6 = np.log(X['Years'])
Xlog = pd.DataFrame([Xlog1, Xlog2, Xlog3, Xlog4, Xlog5, Xlog6])
Xlog = Xlog.transpose()
Xlog.columns = ['logCAtBat', 'logCHits', 'logCRBI', 'logCRuns', 'logCWalks',
                'logYears']
Xlog.hist()
plt.show()

# Putting transformed input columns back into original input dataframe
"""
I had to do replacement one-by-one as I was getting errors trying to do it all
at once for some reason.
"""
X['CAtBat'] = Xlog['logCAtBat']
X['CHits'] = Xlog['logCHits']
X['CRBI'] = Xlog['logCRBI']
X['CRuns'] = Xlog['logCRuns']
X['CWalks'] = Xlog['logCWalks']
X['Years'] = Xlog['logYears']

# Histogram of updated input dataframe
X.hist()
plt.show()

# Log transformation of Salary
Ylog = np.log(Y)
Ylog.columns = ["logSalary"]

# Exploring normalization transformation
scaler = Normalizer().fit(X)
normalizedX = scaler.transform(X)

dataNormDF = pd.DataFrame(normalizedX, columns = X.columns)
dataNormDF.hist()
plt.show()

# Exploring standardization transformation
scaler = StandardScaler().fit(X)
standardX = scaler.transform(X)

dataStandDF = pd.DataFrame(standardX, columns = X.columns)
dataStandDF.hist()
plt.show()

# Replacing columns with transformed versions (again, one-by-one)
X['CAtBat'] = dataNormDF['CAtBat']
X['CHits'] = dataNormDF['CHits']
X['CRBI'] = dataNormDF['CRBI']
X['CRuns'] = dataNormDF['CRuns']
X['CWalks'] = dataNormDF['CWalks']
X['Hits'] = dataNormDF['Hits']
X['PutOuts'] = dataNormDF['PutOuts']
X['RBI'] = dataNormDF['RBI']
X['Runs'] = dataNormDF['Runs']
X['Walks'] = dataNormDF['Walks']

# Histogram of updated input dataframe
X.hist()
plt.show()

"""
Performing correlation analysis
"""
# Adding output column back to data
cleanData = X.copy()
cleanData['logSalary'] = Ylog

# Correllation
corMat = cleanData.corr(method='pearson')

sns.heatmap(corMat, square=True)
plt.yticks(rotation=0)
plt.xticks(rotation=90)
plt.title("Baseball Salary Matrix Using Heatmap")
plt.show()

# Plotting scatterplots of the data
scatter_matrix(cleanData)
plt.show()

"""
Modeling
"""
# Cleaning the data again due to abnormalities from transformations
X.isnull().any()
X.dropna(inplace = True)
Ylog.isnull().any()
Ylog.dropna(inplace = True)

# Creating arrays for input and output
X1 = X.values
Y1 = Ylog.values
Y1 = Y1.ravel()
#Y2 = Y.values
#Y2 = Y2.ravel()
#Y2 = Y2[:211]
# Matching number of values in the output database
Y1 = Y1[:211]

# RFE method for feature selection
# Added * to print entire list of selection and rank
# Turned into method for repeated usage
def rfe_selection (X1, Y1, NUM_FEATURES):
    #NUM_FEATURES = 6
    model = LinearRegression()
    rfe = RFE(model, NUM_FEATURES)
    fit = rfe.fit(X1, Y1)
    print("Num Features:", fit.n_features_)
    print("Selected Features:", *fit.support_)
    print("Feature Ranking:", *fit.ranking_)
    # calculate the score for the selected features
    score = rfe.score(X1,Y1)
    print("Model Score with selected features is: ", score)
    print('\nCoefficients: ', *rfe.estimator_.coef_)
    print('Intercept: ', rfe.estimator_.intercept_)

# RFE Selection and the coefficient and intercepts of the model
# Changing the number of features as needed
rfe_selection(X1, Y1, 15)

# Stepwise selection method found online
def forward_regression(X, y,
                       threshold_in = 0.01,
                       verbose=False):
    initial_list = []
    included = list(initial_list)
    while True:
        changed=False
        excluded = list(set(X.columns)-set(included))
        new_pval = pd.Series(index=excluded)
        for new_column in excluded:
            model = sm.OLS(y, sm.add_constant(pd.DataFrame(X[included+[new_column]]))).fit()
            new_pval[new_column] = model.pvalues[new_column]
        best_pval = new_pval.min()
        if best_pval < threshold_in:
            best_feature = new_pval.idxmin()
            included.append(best_feature)
            changed=True
            if verbose:
                print('Add  {:30} with p-value {:.6}'.format(best_feature, best_pval))

        if not changed:
            break

    return included

def backward_regression(X, y,
                           threshold_out = 0.05,
                           verbose=False):
    included=list(X.columns)
    while True:
        changed=False
        model = sm.OLS(y, sm.add_constant(pd.DataFrame(X[included]))).fit()
        # use all coefs except intercept
        pvalues = model.pvalues.iloc[1:]
        worst_pval = pvalues.max() # null if pvalues is empty
        if worst_pval > threshold_out:
            changed=True
            worst_feature = pvalues.idxmax()
            included.remove(worst_feature)
            if verbose:
                print('Drop {:30} with p-value {:.6}'.format(worst_feature, worst_pval))
        if not changed:
            break
    return included

# Results of stepwise selection
# Adjusting length of Ylog to match X
Ylog1 = Ylog[:211]

result1 = forward_regression(X, Ylog1)

print('resulting features (forward):')
print(result1)

result2 = backward_regression(X, Ylog1)

print('\nresulting features (backward):')
print(result2)

"""
Cross-validation
"""
# Prepare models
models = []

# Adding models
model = LinearRegression()

# From previous RFE selection
NUM_FEATURES = 15
rfe_15 = RFE(model, NUM_FEATURES)
models.append(('rfe_15', rfe_15))

# This model had a more significant drop off
NUM_FEATURES = 12
rfe_12 = RFE(model, NUM_FEATURES)
models.append(('rfe_12', rfe_12))

# From previous step-wise selection
# Forward step
NUM_FEATURES = 5
rfe_5 = RFE(model, NUM_FEATURES)
models.append(('rfe_5', rfe_5))

# Backward step
NUM_FEATURES = 2
rfe_2 = RFE(model, NUM_FEATURES)
models.append(('rfe_2', rfe_2))

# Evaluating each model in turn
results = []
names = []
scoring = 'r2'
for name, mod in models:
    kfold = KFold(n_splits=10, random_state=7)
    cv_results = cross_val_score(mod, X, Y1, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)
    
# Boxplot comparison
fig = pyplot.figure()
fig.suptitle('RFE Model Comparison')
ax = fig.add_subplot(111)
pyplot.boxplot(results)
ax.set_xticklabels(names)
pyplot.show()

# Additional investigation
models = []

NUM_FEATURES = 15
rfe_15 = RFE(model, NUM_FEATURES)
models.append(('rfe_15', rfe_15))

NUM_FEATURES = 14
rfe_14 = RFE(model, NUM_FEATURES)
models.append(('rfe_14', rfe_14))

NUM_FEATURES = 13
rfe_13 = RFE(model, NUM_FEATURES)
models.append(('rfe_13', rfe_13))


NUM_FEATURES = 12
rfe_12 = RFE(model, NUM_FEATURES)
models.append(('rfe_12', rfe_12))

NUM_FEATURES = 11
rfe_11 = RFE(model, NUM_FEATURES)
models.append(('rfe_11', rfe_11))

# Evaluating each model in turn
results = []
names = []
scoring = 'r2'
for name, mod in models:
    kfold = KFold(n_splits=10, random_state=7)
    cv_results = cross_val_score(mod, X, Y1, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)
    
# Boxplot comparison
fig = pyplot.figure()
fig.suptitle('RFE 15-11 Model Comparison')
ax = fig.add_subplot(111)
pyplot.boxplot(results)
ax.set_xticklabels(names)
pyplot.show()
