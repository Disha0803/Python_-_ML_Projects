# import dash
# from dash import dcc, html
# import pandas as pd
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.metrics import mean_squared_error

# # Load the dataset
# data = pd.read_csv('Battery_RUL.csv')

# # Define features and target variable
# X = data.drop(columns=['Cycle_Index', 'RUL'])
# y = data['Cycle_Index']

# # Initialize Random Forest Regressor
# rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)

# # Train the model
# rf_regressor.fit(X, y)

# # Predict battery cycle for each battery in the dataset
# data['Predicted_Cycle'] = rf_regressor.predict(X)

# # Initialize Dash app
# app = dash.Dash(__name__)

# # Define app layout
# app.layout = html.Div([
#     html.H1("Battery Remaining Useful Life Prediction Dashboard"),
    
#     dcc.Graph(
#         id='cycle-plot',
#         figure={
#             'data': [
#                 {'x': data['Cycle_Index'], 'y': data['Predicted_Cycle'], 'type': 'scatter', 'name': 'Predicted Cycle'},
#                 {'x': data['Cycle_Index'], 'y': data['RUL'], 'type': 'scatter', 'name': 'Actual Cycle'}
#             ],
#             'layout': {
#                 'title': 'Actual vs Predicted Battery Cycles',
#                 'xaxis': {'title': 'Cycle Index'},
#                 'yaxis': {'title': 'Cycle'}
#             }
#         }
#     )
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)

# import dash
# from dash import dcc, html
# import pandas as pd
# from sklearn.ensemble import RandomForestRegressor

# # Load the dataset
# data = pd.read_csv('Battery_RUL.csv')

# # Define features and target variable
# X = data.drop(columns=['Cycle_Index', 'RUL'])
# y = data['Cycle_Index']

# # Initialize Random Forest Regressor
# rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)

# # Train the model
# rf_regressor.fit(X, y)

# # Predict battery cycle for each battery in the dataset
# data['Predicted_Cycle'] = rf_regressor.predict(X)

# # Calculate number of cycles left
# data['Cycles_Left'] = data['RUL'] - data['Predicted_Cycle']

# # Initialize Dash app
# app = dash.Dash(__name__)

# # Define app layout
# app.layout = html.Div([
#     html.H1("Battery Remaining Useful Life Prediction Dashboard"),
    
#     html.H3("Number of Cycles Left for Each Battery:"),
#     html.Ul([
#         html.Li(f"Cycle {index + 1}: {cycles_left:.2f} cycles left") 
#         for index, cycles_left in enumerate(data['Cycles_Left'])
#     ]),
    
#     dcc.Graph(
#         id='cycle-plot',
#         figure={
#             'data': [
#                 {'x': data['Cycle_Index'], 'y': data['Predicted_Cycle'], 'type': 'scatter', 'name': 'Predicted Cycle'},
#                 {'x': data['Cycle_Index'], 'y': data['RUL'], 'type': 'scatter', 'name': 'Actual Cycle'}
#             ],
#             'layout': {
#                 'title': 'Actual vs Predicted Battery Cycles',
#                 'xaxis': {'title': 'Cycle Index'},
#                 'yaxis': {'title': 'Cycle'}
#             }
#         }
#     )
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)

# import dash
# from dash import dcc, html
# import pandas as pd
# from sklearn.ensemble import RandomForestRegressor

# # Load the dataset
# data = pd.read_csv('Battery_RUL.csv')

# # Define features and target variable
# X = data.drop(columns=['Cycle_Index', 'RUL'])
# y = data['RUL']

# # Initialize Random Forest Regressor
# rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)

# # Train the model
# rf_regressor.fit(X, y)

# # Predict battery cycle for each battery in the dataset
# data['Predicted_Cycle'] = rf_regressor.predict(X)

# # Calculate number of cycles left
# data['Cycles_Left'] = data['Predicted_Cycle'] - data['RUL']

# # Initialize Dash app
# app = dash.Dash(__name__)

# # Define app layout
# app.layout = html.Div([
#     html.H1("Battery Remaining Useful Life Prediction Dashboard"),
    
#     html.H3("Number of Cycles Left for Each Battery:"),
#     html.Ul([
#         html.Li(f"Serial Number {index + 1}: {cycles_left:.2f} cycles left") 
#         for index, cycles_left in enumerate(data['Cycles_Left'])
#     ]),
    
#     dcc.Graph(
#         id='cycle-plot',
#         figure={
#             'data': [
#                 {'x': data.index, 'y': data['Predicted_Cycle'], 'type': 'scatter', 'name': 'Predicted Cycle'},
#                 {'x': data.index, 'y': data['RUL'], 'type': 'scatter', 'name': 'Actual Cycle'}
#             ],
#             'layout': {
#                 'title': 'Predicted Battery Cycles vs Serial Number',
#                 'xaxis': {'title': 'Serial Number'},
#                 'yaxis': {'title': 'Cycle'}
#             }
#         }
#     )
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)


# import dash
# from dash import dcc, html
# import pandas as pd
# import plotly.graph_objs as go
# from sklearn.ensemble import RandomForestRegressor

# # Load the dataset
# data = pd.read_csv('Battery_RUL.csv')

# # Define features and target variable
# X = data.drop(columns=['Cycle_Index', 'RUL'])
# y = data['RUL']

# # Initialize Random Forest Regressor
# rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)

# # Train the model
# rf_regressor.fit(X, y)

# # Predict battery cycle for each battery in the dataset
# data['Predicted_Cycle'] = rf_regressor.predict(X)

# # Calculate number of cycles left
# data['Cycles_Left'] = data['Predicted_Cycle'] - data['RUL']

# # Initialize Dash app
# app = dash.Dash(__name__)

# # Define app layout
# app.layout = html.Div([
#     html.H1("Battery Remaining Useful Life Prediction Dashboard"),
    
#     html.H3("Number of Cycles Left for Each Battery:"),
#     html.Ul([
#         html.Li(f"Serial Number {index + 1}: {cycles_left:.2f} cycles left") 
#         for index, cycles_left in enumerate(data['Cycles_Left'])
#     ]),
    
#     dcc.Graph(
#         id='cycle-plot',
#         figure={
#             'data': [
#                 go.Scatter(
#                     x=data.index,
#                     y=data['Predicted_Cycle'],
#                     mode='lines+markers',
#                     name='Predicted Cycle',
#                     line=dict(color='blue')
#                 ),
#                 go.Scatter(
#                     x=data.index,
#                     y=data['RUL'],
#                     mode='lines+markers',
#                     name='Actual Cycle',
#                     line=dict(color='green')
#                 ),
#                 go.Scatter(
#                     x=data.index,
#                     y=data['Cycles_Left'],
#                     mode='lines+markers',
#                     name='Cycles Left',
#                     line=dict(color='red')
#                 )
#             ],
#             'layout': {
#                 'title': 'Battery Cycles Overview',
#                 'xaxis': {'title': 'Serial Number'},
#                 'yaxis': {'title': 'Cycle'}
#             }
#         }
#     )
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)

# import dash
# from dash import dcc, html
# import pandas as pd
# import plotly.graph_objs as go
# from sklearn.ensemble import RandomForestRegressor

# # Load the dataset
# data = pd.read_csv('Battery_RUL.csv')

# # Define features and target variable
# X = data.drop(columns=['RUL'])
# y = data['RUL']

# # Initialize Random Forest Regressor
# rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)

# # Train the model
# rf_regressor.fit(X, y)

# # Predict battery cycle for each battery in the dataset
# data['Predicted_Cycle'] = rf_regressor.predict(X)

# # Calculate number of cycles left
# data['Cycles_Left'] = data['Predicted_Cycle'] - data['Cycle_Index']

# # Initialize Dash app
# app = dash.Dash(__name__)

# # Define app layout
# app.layout = html.Div([
#     html.H1("Battery Remaining Useful Life Prediction Dashboard"),
    
#     html.H3("Number of Cycles Left for Each Battery:"),
#     html.Ul([
#         html.Li(f"Serial Number {index + 1}: {cycles_left:.2f} cycles left") 
#         for index, cycles_left in enumerate(data['Cycles_Left'])
#     ]),
    
#     dcc.Graph(
#         id='cycle-plot',
#         figure={
#             'data': [
#                 go.Scatter(
#                     x=data['Cycle_Index'],
#                     y=data['Predicted_Cycle'],
#                     mode='lines+markers',
#                     name='Predicted Cycle',
#                     line=dict(color='blue')
#                 ),
#                 go.Scatter(
#                     x=data['Cycle_Index'],
#                     y=data['RUL'],
#                     mode='lines+markers',
#                     name='Actual Cycle',
#                     line=dict(color='green')
#                 ),
#                 go.Scatter(
#                     x=data['Cycle_Index'],
#                     y=data['Cycles_Left'],
#                     mode='lines+markers',
#                     name='Cycles Left',
#                     line=dict(color='red')
#                 )
#             ],
#             'layout': {
#                 'title': 'Battery Cycles Overview',
#                 'xaxis': {'title': 'Cycle Index'},
#                 'yaxis': {'title': 'Cycle'}
#             }
#         }
#     )
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)

import dash
from dash import dcc, html
import pandas as pd
import plotly.graph_objs as go
from sklearn.ensemble import RandomForestRegressor

# Load the dataset
data = pd.read_csv('Battery_RUL.csv')

# Define features and target variable
X = data.drop(columns=['Cycle_Index', 'RUL'])
y = data['RUL']

# Initialize Random Forest Regressor
rf_regressor = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model
rf_regressor.fit(X, y)

# Predict battery cycle for each battery in the dataset
data['Predicted_Cycle'] = rf_regressor.predict(X)

# Calculate number of cycles left
data['Cycles_Left'] = data['Predicted_Cycle'] - data['Cycle_Index']

# Initialize Dash app
app = dash.Dash(__name__)

# Define app layout
app.layout = html.Div([
    html.H1("Battery Remaining Useful Life Prediction Dashboard"),
    
    html.H3("Number of Cycles Left for Each Battery:"),
    html.Ul([
        html.Li(f"Serial Number {index + 1}: {cycles_left:.2f} cycles left") 
        for index, cycles_left in enumerate(data['Cycles_Left'])
    ]),
    
    dcc.Graph(
        id='cycle-plot',
        figure={
            'data': [
                go.Scatter(
                    x=data['Cycle_Index'],
                    y=data['Predicted_Cycle'],
                    mode='lines+markers',
                    name='Predicted Cycle',
                    line=dict(color='blue')
                ),
                go.Scatter(
                    x=data['Cycle_Index'],
                    y=data['RUL'],
                    mode='lines+markers',
                    name='Actual Cycle',
                    line=dict(color='green')
                ),
                go.Scatter(
                    x=data['Cycle_Index'],
                    y=data['Cycles_Left'],
                    mode='lines+markers',
                    name='Cycles Left',
                    line=dict(color='red')
                )
            ],
            'layout': {
                'title': 'Battery Cycles Overview',
                'xaxis': {'title': 'Cycle Index'},
                'yaxis': {'title': 'Cycle'},
                'showlegend': True
            }
        }
    ),
    
    dcc.Graph(
        id='box-plot',
        figure={
            'data': [
                go.Box(
                    y=data['Predicted_Cycle'],
                    name='Predicted Cycle',
                    marker=dict(color='blue')
                ),
                go.Box(
                    y=data['RUL'],
                    name='Actual Cycle',
                    marker=dict(color='green')
                )
            ],
            'layout': {
                'title': 'Box Plot of Predicted and Actual Cycles',
                'yaxis': {'title': 'Cycle'}
            }
        }
    ),
    
    dcc.Graph(
        id='scatter-plot',
        figure={
            'data': [
                go.Scatter(
                    x=data['Cycle_Index'],
                    y=data['Decrement 3.6-3.4V (s)'],
                    mode='markers',
                    name='Decrement 3.6-3.4V (s)',
                    marker=dict(color='orange')
                ),
                go.Scatter(
                    x=data['Cycle_Index'],
                    y=data['Max. Voltage Dischar. (V)'],
                    mode='markers',
                    name='Max. Voltage Dischar. (V)',
                    marker=dict(color='purple')
                )
            ],
            'layout': {
                'title': 'Scatter Plot of Decrement 3.6-3.4V and Max. Voltage Dischar.',
                'xaxis': {'title': 'Cycle Index'},
                'yaxis': {'title': 'Value'}
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
