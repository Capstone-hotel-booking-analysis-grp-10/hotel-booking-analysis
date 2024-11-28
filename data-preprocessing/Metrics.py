import pandas as pd
import plotly.express as px

# Load only numeric columns from both files
df1 = pd.read_csv('extended_file_e.csv')
df2 = pd.read_csv('hbe.csv')

# Compute correlation matrices
corr1 = df1.corr()
corr2 = df2.corr()

# Plot heatmaps for both datasets
fig2 = px.imshow(corr2, 
                 labels=dict(x="Features", y="Features", color="Correlation"),
                 title="Correlation Heatmap - hb.csv")
fig2.show()
fig1 = px.imshow(corr1, 
                 labels=dict(x="Features", y="Features", color="Correlation"),
                 title="Correlation Heatmap - extended_file.csv")
fig1.show()

