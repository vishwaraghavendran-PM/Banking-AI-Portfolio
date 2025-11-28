# demos/app.py
import streamlit as st
import numpy as np
from sklearn.linear_model import LogisticRegression

st.title("Credit Risk Score Simulator")
st.caption("Toy model to demonstrate decision thresholds and trade-offs")

income = st.slider("Monthly income ($)", 1000, 20000, 6000, 500)
debt    = st.slider("Monthly debt ($)", 0, 10000, 1500, 250)
history = st.selectbox("Payment history", ["Good", "Average", "Poor"])

X = np.array([[income, debt, {"Good":2,"Average":1,"Poor":0}[history]]])
model = LogisticRegression()
# Fake fit for demo display
model.coef_ = np.array([[0.0001, -0.0002, 0.4]])
model.intercept_ = np.array([ -1.2 ])
model.classes_ = np.array([0,1])

score = 1/(1+np.exp(-(X @ model.coef_.T + model.intercept_)))[0][0]
st.metric("Risk score (0–1)", f"{score:.2f}")

threshold = st.slider("Approval threshold", 0.1, 0.9, 0.5, 0.05)
decision = "Approve" if score < threshold else "Review/Decline"
st.success(f"Decision: {decision}")
