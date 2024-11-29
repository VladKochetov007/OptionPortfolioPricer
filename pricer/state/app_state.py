from dataclasses import dataclass
import streamlit as st

@dataclass
class AppState:
    """Manages application state"""
    @staticmethod
    def initialize() -> None:
        if 'options' not in st.session_state:
            st.session_state.options = []
    
    @staticmethod
    def add_option(option: dict[str, any]) -> None:
        st.session_state.options.append(option)
    
    @staticmethod
    def get_options() -> list[dict[str, any]]:
        return st.session_state.options 
