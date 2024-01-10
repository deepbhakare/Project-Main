import streamlit as st

def main():
    st.title("Crop Disease Classification and Treatment Recommendation System for Amravati District")
    st.write("Objective: The goal of this project is to develop a robust crop disease classification system using machine learning techniques. The primary objective is to accurately identify and classify diseases affecting various crops, enabling early detection and timely intervention for crop protection.")

    # Create two buttons side by side
    col1, col2, col3 = st.beta_columns(3)  # Using beta_columns to create two columns

    if col1.button("Vegetable Plant"):
        st.success("Some well-known websites that provide useful information on growing vegetables include:

1.The Old Farmer's Almanac
2.[University Extension Websites](e.g., University of California Cooperative Extension, Cornell University - Gardening Resources)
3.Gardening Know How
4.Royal Horticultural Society (RHS)")
        # Redirect to the Vegetable Plant website (replace the URL with the actual website)
        st.markdown("[Vegetable Plant Website](https://vegetable.streamlit.app)")

    if col2.button("Cash Crop"):
        st.success("Redirecting to Cash Crop website...")
        # Redirect to the Cash Crop website (replace the URL with the actual website)
        st.markdown("[Cash Crop Website](https://cash-crop.streamlit.app)")

    if col3.button("Cash Crop (BETA)"):
        st.success("Redirecting to Cash Crop (BETA) website...")
        # Redirect to the Cash Crop website (replace the URL with the actual website)
        st.markdown("[Cash Crop [BETA] Website](https://cpddpy-qwhhpsykdudfcplonnvrr7.streamlit.app)")

if __name__ == "__main__":
    main()
