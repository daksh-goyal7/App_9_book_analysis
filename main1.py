import glob
import streamlit as st
import plotly.express as px

from nltk.sentiment import SentimentIntensityAnalyzer

filepaths=sorted(glob.glob("diary/*.txt"))

analyzer=SentimentIntensityAnalyzer()
positively=[]
negatively=[]
for filepath in filepaths:
    with open(filepath) as file:
        content=file.read()
    scores=analyzer.polarity_scores(content)
    positively.append(scores["pos"])
    negatively.append(scores["neg"])

dates=[name.strip(".txt").strip("diary/") for name in filepaths]

st.title("Diary tone")
st.subheader("Positively")
pos_figure=px.line(x=dates,y=positively,labels={"x":"Date","y":"Positively"})
st.plotly_chart(pos_figure)

st.subheader("Negatively")
neg_figure=px.line(x=dates,y=negatively,labels={"x":"Date","y":"Negatively"})
st.plotly_chart(neg_figure)
