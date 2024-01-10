import streamlit as st

def main():
    st.title("Crop Selection App")

    # Create two buttons side by side
    col1, col2, col3 = st.beta_columns(3)  # Using beta_columns to create two columns

    if col1.button("Vegetable Plant"):
        st.success("Redirecting to Vegetable Plant website...")
        # Redirect to the Vegetable Plant website (replace the URL with the actual website)
        st.markdown("[Vegetable Plant Website](https://vegetable.streamlit.app)")

    if col2.button("Cash Crop"):
        st.success("Redirecting to Cash Crop website...")
        # Redirect to the Cash Crop website (replace the URL with the actual website)
        st.markdown("[Cash Crop Website](https://cash-crop.streamlit.app)")

    if col3.button("Cash Crop (BETA)"):
        st.success("Redirecting to Cash Crop (BETA) website...")
        # Redirect to the Cash Crop website (replace the URL with the actual website)
        st.markdown("[Cash Crop Website](https://cpddpy-qwhhpsykdudfcplonnvrr7.streamlit.app)")

if __name__ == "__main__":
    main()
