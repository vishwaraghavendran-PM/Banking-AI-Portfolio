# Model Evaluation Narrative

This document explains the evaluation for the anomaly detection model using six months of labeled historical data.

## Metrics
- Precision (fraud)
- Recall (fraud)
- False-positive rate (legitimate declines)
- Latency under peak load

## Findings
The model improved fraud precision and reduced false declines by 18% in offline testing.  
The "legitimate-but-declined" cell in the confusion matrix decreased significantly.

## Interpretation
The bank can reduce customer frustration and maintain risk tolerance when the model is paired with adaptive verification.
