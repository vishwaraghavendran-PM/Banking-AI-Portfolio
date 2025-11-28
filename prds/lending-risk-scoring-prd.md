# Product Requirements Document  
## AI-Enhanced Lending Risk Scoring System

### 1. Purpose
Improve underwriting accuracy, reduce credit losses, and streamline operational workload through a machine learning–based risk scoring framework.

### 2. Background
The bank’s rule-driven risk engine produced inconsistent outcomes, high manual review volume, and low approval rates. An adaptive and explainable ML model is required to support better lending decisions.

### 3. Goals
- 15% reduction in default rate  
- 8% increase in approval rate  
- 25% reduction in manual underwriting  
- Compliance with explainability and fairness guidelines  

### 4. Users
Underwriters, risk teams, credit product managers, loan operations.

### 5. Functional Requirements
#### 5.1 Data Ingestion
- Bureau data integration  
- KYC + income verification  
- Bank transaction ingestion  

#### 5.2 Feature Engineering
- Debt-to-income, cash flow stability  
- Spending anomaly detection  
- Repayment velocity  
- Dynamic borrower profile store  

#### 5.3 Model Scoring
- Predict PD  
- Latency < 50 ms  
- Provide top contributing features  

#### 5.4 Decisioning Engine
- Auto-approve low-risk  
- Auto-decline high-risk  
- Manual review for mid-band  
- Reason code generation  

#### 5.5 Monitoring
- Drift detection  
- Fairness dashboard  
- Monthly stability reporting  

### 6. Non-Functional Requirements
Latency, auditability, encryption, fairness controls.

### 7. Rollout Plan
Shadow mode → controlled rollout → credit card expansion → full deployment.
