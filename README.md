# E-commerce Spammer Group Detection

An end-to-end machine learning and graph-based system for detecting coordinated spammer groups in e-commerce review data.

## 📌 Project Overview

E-commerce platforms can be affected by coordinated groups of users who generate misleading or spam reviews. Detecting individual suspicious users is not always enough because multiple users may operate together as a community.

This project combines:

- Data preprocessing
- User and review feature engineering
- Graph-based community detection
- Spam Probability Score (SPS)
- Machine learning
- Community-level risk analysis
- Final spam group classification
- REST API
- Web-based frontend

The system identifies suspicious users, detects their communities, calculates community-level risk, and produces a final spam decision.

## 🎯 Objectives

- Identify suspicious review behavior.
- Extract meaningful user and textual features.
- Build user interaction graphs.
- Detect communities of users.
- Calculate Spam Probability Scores.
- Apply machine learning for spam classification.
- Identify high-risk coordinated spammer groups.
- Provide results through an API and frontend interface.

## 🏗️ System Workflow

```text
E-commerce Review Data
          ↓
Data Preprocessing
          ↓
Feature Engineering
          ↓
User & Textual Features
          ↓
User Interaction Graph
          ↓
Community Detection
          ↓
Spam Probability Score (SPS)
          ↓
Machine Learning Model
          ↓
Community Risk Analysis
          ↓
Final Spam Decision
          ↓
REST API + Frontend


🧠 Key Features
1. Data Preprocessing

Cleans and prepares review data for further analysis.

2. Feature Engineering

Generates user-level and textual features from review activity.

3. Graph-Based Detection

Represents relationships between users and reviews as a graph to identify coordinated communities.

4. Community Detection

Groups related users and analyzes their collective behavior.

5. Spam Probability Score

Calculates a score representing the likelihood of suspicious behavior.

6. Machine Learning

Uses a Random Forest model to classify suspicious users.

7. Community Risk Analysis

Combines individual user signals to determine community-level risk.

8. REST API

Provides an interface for accessing spam detection results.

9. Frontend

Provides a web interface for interacting with the detection system.

🛠️ Technologies Used
Python
Pandas
NumPy
Scikit-learn
NetworkX
Graph-based Community Detection
Machine Learning
REST API
HTML
CSS
JavaScript
JSON


spammer_group_detection/
│
├── backend/
│   ├── app.py
│   ├── preprocessing.py
│   ├── user_features.py
│   ├── textual_features.py
│   ├── graph_builder.py
│   ├── community_detection.py
│   ├── community_risk.py
│   ├── sps_calculation.py
│   ├── ml_model.py
│   ├── ml_model_rf.py
│   ├── ml_inference.py
│   └── ...
│
├── data/
│   ├── reviews.json
│   ├── user_features.json
│   ├── user_communities.json
│   ├── user_community_risk.json
│   └── ...
│
├── frontend/
│   └── index.html
│
├── models/
│   └── spam_rf_model.pkl
│
├── .gitignore
└── README.md