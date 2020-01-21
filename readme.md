# Tricty things for data science

## DataFrame
- when use df1['new_column'] = df2['column'] , it will append to it by df1.index
### Pandas is too slow
- when use apply function, it may cost lots of time, plz try:  
  - when bin: use pd.cut()
  - joblib
  - tranform to np
- use df[~df.variable.isin(case)] conditional choose df
  

## Model
- For simple DecisionTree, sometimes it is not good to make it deep. Control maxdepth when variables are enough;
- Tree models almost not be effected by multicollinearity, because of greedy. Unlike linear models, sometimes some positive independent variables(t-test) will become negative in models(coefficient), because multicollinearity/suppress effect
