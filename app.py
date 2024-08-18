import streamlit as st 
import numpy as np 
import pandas as pd 
import pickle 

# Load the trained model
pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)

# Function for prediction
def predict_credit_score(
    Age, Annual_Income, Monthly_Inhand_Salary, Num_Bank_Accounts, 
    Num_Credit_Card, Interest_Rate, Num_of_Loan, Delay_from_due_date, 
    Credit_Mix, Credit_History_Age, Monthly_Balance): 

    # One-hot encode Credit Mix
    Credit_Mix_encoded = [0, 0, 0]  # Assuming 3 categories for Credit_Mix: Good, Average, Bad
    if Credit_Mix == "Good":  # Example: 2 = "Good"
        Credit_Mix_encoded[0] = 1
    elif Credit_Mix == "Average":  # Example: 1 = "Average"
        Credit_Mix_encoded[1] = 1
    elif Credit_Mix == "Bad":  # Example: 0 = "Bad"
        Credit_Mix_encoded[2] = 1

    # Combine all inputs (numeric and one-hot encoded)
    features = [
        Age, Annual_Income, Monthly_Inhand_Salary, Num_Bank_Accounts, 
        Num_Credit_Card, Interest_Rate, Num_of_Loan, Delay_from_due_date,Credit_History_Age, Monthly_Balance
    ] + Credit_Mix_encoded  # Append the one-hot encoded categorical feature

    # Make the prediction
    prediction = classifier.predict([features])
    return prediction

# Main function for Streamlit app
def main(): 
    st.title("Credit Score Classifier")
    
    # UI elements for numeric inputs
    Age = st.text_input("Age", "Type Here")
    Annual_Income = st.text_input("Annual Income", "Type Here")
    Monthly_Inhand_Salary = st.text_input("Monthly Inhand Salary", "Type Here")
    Num_Bank_Accounts = st.text_input("Number of Bank Accounts", "Type Here")
    Num_Credit_Card = st.text_input("Number of Credit Cards", "Type Here")
    Interest_Rate = st.text_input("Interest Rate", "Type Here")
    Num_of_Loan = st.text_input("Number of Loans", "Type Here")
    Delay_from_due_date = st.text_input("Delay from Due Date", "Type Here")
    Credit_History_Age = st.text_input("Credit History Age", "Type Here")
    Monthly_Balance = st.text_input("Monthly Balance", "Type Here")

    # Categorical input for Credit Mix
    Credit_Mix = st.selectbox("Credit Mix", ("Good", "Average", "Bad"))  
    
    result = ""

    if st.button("Predict"):
        # Convert input values to numeric
        result = predict_credit_score(
            float(Age), float(Annual_Income), float(Monthly_Inhand_Salary), 
            float(Num_Bank_Accounts), float(Num_Credit_Card), float(Interest_Rate), 
            float(Num_of_Loan), float(Delay_from_due_date), Credit_Mix, float(Credit_History_Age), float(Monthly_Balance)
        )
    
    st.success(f'The predicted credit score is: {result}')

    if st.button("About"):
        st.text("This is a Machine Learning model deployed using Streamlit.")

# Call main function
if __name__ == '__main__':
    main()