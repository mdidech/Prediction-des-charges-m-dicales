import streamlit as st
from predict_helper import predict

st.title("Predictions des charges médicales")
categorical_options={
    "sex":["female","male"],
    "smoker":["yes","no"],
    "region":["southwest","southeast","northwest","northeast"]
}
row1=st.columns(2)
row2=st.columns(2)
row3=st.columns(2)

with row1[0]:
    age=st.number_input("Age",min_value=18,max_value=100,step=1)
with row1[1]:
    sex=st.selectbox("Sex",categorical_options["sex"])
with row2[0]:
    bmi=st.number_input("BMI",min_value=5.0,max_value=60.0,step=.25)
with row2[1]:
    children=st.number_input("Children",min_value=0,max_value=20,step=1)
with row3[0]:
    smoker=st.selectbox("Smoking",categorical_options["smoker"])
with row3[1]:
    region=st.selectbox("Region",categorical_options["region"])

predict_inputs={
    "age":age,
    "bmi":bmi,
    "children":children,
    "sex":sex,
    "smoker":smoker,
    "region":region
}
if st.button("Predire"):
    try:
        prediction=predict(predict_inputs)
        st.success(f"les charges médicales estimées sont: {prediction:.2f}")

    except Exception as e:
        st.error(f"Une erreur inattendue s'est produite : {e}")
    
