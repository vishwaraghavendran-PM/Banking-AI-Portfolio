# Real-time Card Transaction Anomaly Detection with Human-in-the-Loop Confirmation

**Outcome:** Reduced false declines by 27% while maintaining fraud losses below threshold through an adaptive verification model.

## Problem / Context
The bank processed millions of card transactions daily. Customers frequently reported false declines, especially while traveling. Fraud losses were rising due to attack patterns that evaded rule-based controls.

## Hypothesis
A real-time anomaly detection model supported by dynamic customer verification will reduce false declines without increasing fraud losses.

## Success Metrics
**Primary**
- False decline rate: target -20%
- Fraud loss within existing tolerance

**Guardrails**
- Customer confirmation success ≥ 85%
- Added latency < 30 ms

## Solution Overview
The model scores each transaction using behavioral and contextual features.  
Based on confidence thresholds:
- Approve  
- Trigger verification in mobile app  
- Decline + fraud flag  

Customer confirmation influences future training.

## Architecture (High-Level)
Inputs → Feature generation → Anomaly model → Confidence thresholds →  
(1) auto-approve  
(2) adaptive verification  
(3) auto-decline  

## Rollout
1. Shadow mode  
2. Limited rollout to low-risk domestic segments  
3. Expansion to international transactions

## Risks & Mitigations
- Notification failure → fallback SMS  
- Model drift → monthly recalibration  
- Biased declines → slice analysis across groups

## Outcome
Pilot results indicated a 27% reduction in false declines with stable fraud-loss ratios.  
The approach scaled to multiple regions with feature tuning for travel-intensive markets.
