from plotly.offline import plot
import plotly.graph_objects as go
import numpy as np

def plotlyData(data, timestamp = None):    
    if (data is None):
        timestamp = np.linspace(0, len(data), len(data)) #if needed
        
    fig = go.Figure()    
    fig.add_trace(go.Scatter(x=timestamp, y=data,
                        #mode='lines+markers',
                        mode='lines',
                        name='lines'))    
    plot(fig)    
    
randData = np.random.rand(10)
plotlyData(randData)
