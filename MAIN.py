import streamlit as st

def main():
    st.title("Crop Selection App")

    # Create two buttons side by side
    col1, col2 = st.beta_columns(2)  # Using beta_columns to create two columns

    if col1.button("Vegetable Plant"):
        st.success("Redirecting to Vegetable Plant website...")
        # Redirect to the Vegetable Plant website (replace the URL with the actual website)
        st.markdown("[Vegetable Plant Website](https://www.example-vegetable-plant.com)")

    if col2.button("Cash Crop"):
        st.success("Redirecting to Cash Crop website...")
        # Redirect to the Cash Crop website (replace the URL with the actual website)
        st.markdown("[Cash Crop Website](https://www.example-cash-crop.com)")

if __name__ == "__main__":
    main()
