import streamlit as st

col1, col2 = st.columns([2, 3])
tab1, tab2 = st.tabs(['은', '총'])
with col1 :
    st.title("here is column1 title")
    with tab1 :
        st.write('은총이...솔직히종종바보같을때있긴 해')
        st.write('은총이...솔직히종종바보같을때있긴 해')
    with tab2 :
        st.write("은총아...\n\n\n\n\n\n\n\n\n\n\n\n\n캘빈이 뭐에요?????????")

with col2 :
    st.title("here is column2 title")
    st.checkbox("this is checkbox1 in col2")

col1.subheader("i am column1 subheader")
col2.checkbox("this i checkbox2 in col2")

