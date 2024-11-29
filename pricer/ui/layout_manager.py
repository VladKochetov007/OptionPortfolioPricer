import streamlit as st
from streamlit.delta_generator import DeltaGenerator

class LayoutManager:
    """Manages application layout and styling"""
    @staticmethod
    def setup_page() -> None:
        st.set_page_config(layout="wide")
        st.markdown("""
            <style>
            .block-container {
                padding-top: 1rem;
                padding-bottom: 0rem;
                padding-left: 2rem;
                padding-right: 2rem;
            }
            </style>
        """, unsafe_allow_html=True)
        st.title("Option Portfolio Pricer")
    
    @staticmethod
    def create_columns() -> tuple[DeltaGenerator, DeltaGenerator]:
        return st.columns([1, 1])