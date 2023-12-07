# Some python

! git clone --depth 1 https://github.com/rwightman/pytorch-image-models.git
%cd pytorch-image-models/results
%pip install plotly statsmodels

#

import pandas as pd
df_results = pd.read_csv('results-imagenet.csv')
df.rename(columns={'model': 'model_long'}, inplace=True)
df_results['model'] = df_results['model'].apply(lambda x: x.split('.')[0])
