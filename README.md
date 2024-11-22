
# Travel Package Purchase Prediction

This project predicts whether a customer will purchase a travel package based on a variety of factors, including demographic data, past purchasing behavior, and interactions with sales representatives. The model is built using machine learning techniques and trained on customer data to provide accurate predictions.

## Table of Contents
- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Model Details](#model-details)
- [Data Preprocessing](#data-preprocessing)
- [Technologies](#technologies)
- [License](#license)

## Project Overview
This project aims to predict travel package purchases by analyzing various customer-related features. The goal is to classify customers into two categories:
- **Will Purchase**: The customer is likely to purchase the travel package.
- **Not Purchase**: The customer is unlikely to purchase the travel package.

The model is built using popular machine learning algorithms such as **XGBoost** and **LightGBM**. The project also employs data preprocessing techniques such as feature encoding and normalization.

## Installation

To run this project locally, follow the steps below:

### 1. Clone the repository
```bash
git clone https://github.com/Pvidhim/TravelPackagePurchasePrediction.git
cd TravelPackagePurchasePrediction
```

### 2. Set up a virtual environment (optional but recommended)
Create a virtual environment to isolate the project dependencies:
```bash
python -m venv venv
```

Activate the virtual environment:
- **Windows**:
  ```bash
  .\venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 3. Install dependencies
Install the required packages using pip:
```bash
pip install -r requirements.txt
```

Make sure you have the necessary packages installed. The `requirements.txt` file includes dependencies like `Flask`, `pandas`, `xgboost`, and `lightgbm`.

## Usage

### Running the Flask Application
Once you've set up the environment and installed the dependencies, you can start the Flask web application:

```bash
python app.py
```

This will start a local server. Open your browser and visit the following URL to use the app:
```
http://127.0.0.1:5000/
```
### 📷 DEMO PHOTO
![image](https://github.com/user-attachments/assets/036298b9-a51e-4a5d-bfa7-53c8a9d91aed)
## ⏳Data Source
[Travel Package Data](https://www.kaggle.com/code/yogidsba/travelpackageprediction-ensemble-techniques/input)
***
 ## 🖥️Library Used
 There will be file named requirement.txt which will contain all these libraries used in project.
 ```
pandas
numpy
seaborn
matplotlib
scikit-learn
xgboost
LightGBM
flask
 ```
### Web Interface
The user can input details such as:
- Age
- Gender
- City Tier
- Number of Persons Visiting
- Preferred Property Star
- Monthly Income
- Occupation, etc.

The model will output whether the customer is likely to purchase the travel package based on these inputs.

## Features
- **Customer Information Input**: Users can input various details about the customer, such as age, occupation, city tier, etc.
- **Prediction**: Based on the input features, the model predicts whether the customer will purchase the travel package.
- **Web Interface**: The Flask web app allows easy interaction and visualization of predictions.

## Model Details

The machine learning models used in this project are:
- **XGBoost**: A gradient boosting algorithm known for its efficiency and speed.
- **LightGBM**: Another gradient boosting framework that is optimized for large datasets.

The models are trained to classify whether a customer is likely to purchase the package based on the provided features.

## Data Preprocessing
Data preprocessing steps include:
- **Feature Encoding**: Categorical variables are encoded using techniques such as one-hot encoding or label encoding.
- **Normalization**: Continuous variables are normalized to improve model performance.
- **Handling Missing Data**: Missing values are handled using imputation techniques.

## Technologies

- **Flask**: A micro web framework for building the web interface.
- **pandas**: For data manipulation and preprocessing.
- **xgboost**: For building the prediction model using gradient boosting.
- **lightgbm**: For an alternative gradient boosting model.
- **scikit-learn**: For machine learning utilities like splitting the data and evaluating models.

## Deployment

-The project was deployed on render . The link to the same is : https://travelpackagepurchaseprediction.onrender.com
You can access the model directly through this link and try inputting various data .

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

