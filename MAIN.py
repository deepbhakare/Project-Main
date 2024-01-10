import streamlit as st

def main():
    st.title("Crop Disease Classification and Treatment Recommendation System for Amravati District")
    st.write("Objective: The goal of this project is to develop a robust crop disease classification system using machine learning techniques. The primary objective is to accurately identify and classify diseases affecting various crops, enabling early detection and timely intervention for crop protection.")

    # Create three buttons side by side
    col1, col2, col3 = st.beta_columns(3)  # Using beta_columns to create two columns

    if col1.button("Vegetable Plant"):
        st.success("Website that provide useful information on growing vegetables https://www.almanac.com/gardening/growing-guides#Vegetable")
        st.write("Click Here --> [Vegetable Plant Website](https://vegetable.streamlit.app)")

    if col2.button("Cash Crop"):
        st.success("Website that provide useful information on growing Cotton Plant https://cottontoday.cottoninc.com/cotton-and-water-better-management-of-an-increasingly-scarce-resource")
        st.write("Click Here --> [Cash Crop Website](https://cash-crop.streamlit.app)")

    if col3.button("Cash Crop (BETA)"):
        st.success("Note - This website may not give you an accurate result because, its under development")
        st.write("Click Here --> [Cash Crop [BETA] Website](https://cpddpy-qwhhpsykdudfcplonnvrr7.streamlit.app)")

if __name__ == "__main__":
    main()
