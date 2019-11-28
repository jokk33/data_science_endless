# Tricty things for data science

## DataFrame
- when use df1['new_column'] = df2['column'] , it will append to it by df1.index  

## Model
- For simple DecisionTree, sometimes it is not good to make it deep. Control maxdepth when variables are enough;
- Tree models almost not be effected by multicollinearity, because of greedy. Unlike linear models, sometimes some positive independent variables(t-test) will become negative in models(coefficient), because multicollinearity/suppress effect
