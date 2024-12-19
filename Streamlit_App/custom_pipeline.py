import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin

# Variables finales souhaitées
FINAL_COLUMNS = [
    'OverallQual', 'HeatingQC', 'MSSubClass', 'BsmtQual', 'GarageFinish',
    'Neighborhood', 'Exterior1st', 'GarageCars', 'FullBath', 'Dure_house',
    'TotRmsAbvGrd', 'Dure_garage'
]

class DurationCalculator(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.max_dure_garage = None
        
    def fit(self, X, y=None):
        X = pd.DataFrame(X).copy()
        X['Dure_house'] = pd.to_numeric(X['YrSold'] - X['YearRemodAdd'])
        X['Dure_garage'] = pd.to_numeric(X['YrSold'] - X['GarageYrBlt'])
        self.max_dure_garage = X['Dure_garage'].max()
        return self
        
    def transform(self, X):
        X = pd.DataFrame(X).copy()
        X['Dure_house'] = pd.to_numeric(X['YrSold'] - X['YearRemodAdd'])
        X['Dure_garage'] = pd.to_numeric(X['YrSold'] - X['GarageYrBlt'])
        X['Dure_garage'] = X['Dure_garage'].fillna(self.max_dure_garage)
        return X

class EnhancedOrdinalEncoder(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.ordinal_mappings = {
            'BsmtQual': {'None': 0, 'Po': 1, 'Fa': 2, 'TA': 3, 'Gd': 4, 'Ex': 5},
            'HeatingQC': {'Po': 0, 'Fa': 1, 'TA': 2, 'Gd': 3, 'Ex': 4},
            'GarageFinish': {'None': 0, 'Unf': 1, 'RFn': 2, 'Fin': 3}
        }
        self.columns = ['BsmtQual', 'HeatingQC', 'GarageFinish']
        
    def fit(self, X, y=None):
        return self
        
    def transform(self, X):
        X = pd.DataFrame(X).copy()
        for col in self.columns:
            X[col] = X[col].fillna('None')
            X[col] = X[col].map(self.ordinal_mappings[col]).astype(float)
        return X[self.columns]

class FrequencyEncoder(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.freq_maps = {}
        self.columns = ['Exterior1st', 'Neighborhood']
        
    def fit(self, X, y=None):
        X = pd.DataFrame(X)
        for col in self.columns:
            self.freq_maps[col] = X[col].value_counts(normalize=True).to_dict()
        return self
        
    def transform(self, X):
        X = pd.DataFrame(X).copy()
        for col in self.columns:
            X[col] = X[col].map(self.freq_maps[col])
        return X[self.columns]

class DataFrameFormatter(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
        
    def transform(self, X):
        all_features = (['BsmtQual', 'HeatingQC', 'GarageFinish'] +
                      ['Neighborhood', 'Exterior1st'] +
                      ['GarageCars', 'FullBath', 'TotRmsAbvGrd'] +
                      ['Dure_house', 'Dure_garage'] +
                      ['OverallQual', 'MSSubClass'])
        X_df = pd.DataFrame(X, columns=all_features)
        return X_df[FINAL_COLUMNS]
