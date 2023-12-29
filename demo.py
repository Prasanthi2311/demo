import streamlit as st
st.set_page_config(page_title='cats')
st.markdown("## Types of Cats")
col1,col2,col3=st.columns(3)
with col1:
  st.image("./cat1.jpg",width=320,use_column_width=True)
  st.write("- Persian Cat")
  st.write("Persian Cats Are Cute")
with col2:  
  st.image("./cat2.jpg")
  st.write("- White Cat",use_column_width=True)
   st.write("White Cats Are Cute")
with col3:  
  st.image("https://yt3.ggpht.com/a/AGF-l7-3jWa9P55VQ8-0kYWPJLAyC6ZyUcpyHo-gNw%3ds900-c-k-c0xffffffff-no-rj-mo",width=320,use_column_width=True)
  st.write("- Burmese Cat")
  st.write("Burmese Cats Are Cute")
