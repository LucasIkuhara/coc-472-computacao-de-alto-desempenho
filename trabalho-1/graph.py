# %%
from matplotlib.pyplot import title
import pandas as pd
import plotly.graph_objects as go

# %%
c = pd.read_csv('c.log')
c_rev = pd.read_csv('c_reverse.log')
fortran = pd.read_csv('fortran.log')
fortran_rev = pd.read_csv('fortran_reverse.log')

complexityEstimate = {
    'x': [x for x in range(0, 50_001, 1000)],
    'y': [(0.0001*x)**2 for x in range(0, 50_001, 1000)]
}

# %%
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=c['n'],
    y=c['time_in_mil'],
    name='C',
    mode='lines'
))

fig.add_trace(go.Scatter(
    x=c_rev['n'],
    y=c_rev['time_in_mil'],
    name='C reverse',
    mode='lines'
))

fig.add_trace(go.Scatter(
    x=fortran['n'],
    y=fortran['time_in_mil'],
    name='fortran',
    mode='lines'
))

fig.add_trace(go.Scatter(
    x=fortran_rev['n'],
    y=fortran_rev['time_in_mil'],
    name='fortran reverse',
    mode='lines'
))

fig.add_trace(go.Scatter(
    complexityEstimate,
    name='Estimate O(N^2)',
    mode='lines'
))

fig.update_xaxes(title='N')
fig.update_yaxes(title='tempo (s)')
fig.update_layout(title='Tempo de execução em função de N')


fig.show()
