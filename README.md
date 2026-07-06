# 🛠️ Cognifyz Level 2 – Task 3: Restaurant Feature Engineering

## 📌 Project Overview

This project was completed as part of the *Cognifyz Technologies Data Science Internship (Level 2 – Task 3).*

The objective of this task is to perform *Feature Engineering* on the Zomato Restaurant Dataset by creating meaningful features from existing data and encoding categorical variables for improved data analysis.

---

## 🎯 Objectives

- Extract meaningful features from existing columns.
- Create text-based features using restaurant information.
- Encode categorical variables into numerical format.
- Prepare the dataset for further data analysis.
- Improve data usability through feature engineering.

---

## 📂 Dataset

The project uses *Dataset.csv*, which contains restaurant-related information such as:

- Restaurant Name
- Address
- Locality
- City
- Cuisines
- Price Range
- Aggregate Rating
- Rating Color
- Table Booking
- Online Delivery
- Votes

---

## 🛠️ Technologies Used

- Python
- Pandas

---

## ✨ Features Created

### 📝 Text-Based Features

- Restaurant Name Length
- Address Length
- Locality Length

### 🔄 Encoded Features

- Has Table Booking Encoded
- Has Online Delivery Encoded

---

## 📁 Repository Contents

- feature_engineering.py — Main source code
- Dataset.csv — Original dataset
- Feature_Engineered_Dataset.csv — Dataset after feature engineering
- README.md — Project documentation

---

## 📂 Project Structure

```text
COGNIFYZ_LEVEL2_TASK3/
│
├── Dataset.csv
├── Feature_Engineered_Dataset.csv
├── feature_engineering.py
└── README.md
```

---

## 📊 Analysis Performed

### 1️⃣ Text Feature Extraction

- Calculated the length of each restaurant name.
- Calculated the length of each restaurant address.
- Calculated the length of each locality.

### 2️⃣ Categorical Encoding

- Converted *Has Table Booking* into binary values (Yes = 1, No = 0).
- Converted *Has Online Delivery* into binary values (Yes = 1, No = 0).

---

## ▶️ How to Run

### 1. Install the required library

```bash
pip install pandas
```

### 2. Place the dataset

Keep *Dataset.csv* inside the project folder.

### 3. Run the project

```bash
python feature_engineering.py
```

---

## 💡 Key Insights

- Feature Engineering transforms raw data into meaningful information.
- Text-based features provide additional characteristics that can improve analysis.
- Encoding categorical variables makes the dataset suitable for machine learning algorithms.
- The generated dataset is enriched with meaningful engineered features.

---

## 🎓 Learning Outcomes

Through this project, I strengthened my understanding of:

- Feature Engineering
- Text Feature Extraction
- Categorical Encoding
- Data Preparation
- Data Preprocessing using Pandas

---

## 👩‍💻 Author

*Alfishan Khan*

B.Tech – Computer Science Engineering (Artificial Intelligence & Machine Learning)

Data Science Intern – Cognifyz Technologies

---

⭐ Completed as part of the Cognifyz Technologies Data Science Internship Program.
