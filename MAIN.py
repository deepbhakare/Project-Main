import streamlit as st

def main():
    st.title("Crop Selection App")

    # Create two buttons side by side
    col1, col2 = st.beta_columns(2)  # Using beta_columns to create two columns

    if col1.button("Vegetable Plant"):
        st.success("Redirecting to Vegetable Plant website...")
        redirect_js = f"window.open('https://vegetable.streamlit.app', '_blank')"
        st.markdown(f'<script>{redirect_js}</script>', unsafe_allow_html=True)

    if col2.button("Cash Crop"):
        st.success("Redirecting to Cash Crop website...")
        redirect_js = f"window.open('https://www.example-cash-crop.com', '_blank')"
        st.markdown(f'<script>{redirect_js}</script>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
