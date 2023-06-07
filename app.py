import streamlit as st 
import joblib

#load the joblib model
model_nb=joblib.load('spam-ham')

st.title('SPAM-HAM MODEL)
ip = st.text_input('ENTER YOUR MESSAGE')
op = model_nb.predict([ip])
if st.button('predict'):
         st.title(op[0])
         
         
