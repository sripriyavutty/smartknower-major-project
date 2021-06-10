import streamlit as st
import pickle

st.set_page_config(page_title="Major Project")

st.markdown("<h1 style='text-align: center;'>Twitter Climate Change Sentimental Analysis</h1>", unsafe_allow_html=True)

filename = 'svm_model.sav'

model = pickle.load(open(filename, 'rb'))

select = st.text_input('Enter Tweet or Message')

if(st.markdown(
    '<span> Emotional Tone </span> ',
    unsafe_allow_html=True
)):
  op = model.predict([select])
  ans=op[0]
  if ans == 'Positive':
    st.success("Positive 🙂")
  if ans == 'Negative':
    st.error("Negative 😠")
  if ans== 'Neutral':
    st.warning("Neutral 😐")

st.markdown('<style> .foo {  position: fixed;  left: 0;  bottom: 0;  width: 100%;  background-color: #170F13;  color: white;  text-align: center;}</style> <div class ="foo"> <p>Submitted as Major Project to <a href="https://www.smartknower.com/">SmartKnower</a> as part of Machine Learning Internship by <a href="https://github.com/sripriyavutty">Sripriya Vutty👨‍💻</a></p></div>',unsafe_allow_html=True)
