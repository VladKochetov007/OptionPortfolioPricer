import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
import numpy as np


class ChartManager:
    @staticmethod
    def plot_payoff(S_range: np.ndarray, payoff: np.ndarray) -> None:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=S_range, y=payoff, name='Payoff'))
        fig.update_layout(
            title='Option Payoff Profile',
            xaxis_title='Underlying Price',
            yaxis_title='Payoff',
            showlegend=True,
            height=300,
            margin=dict(l=0, r=0, t=30, b=0)
        )
        st.plotly_chart(fig, use_container_width=True)
    
    @staticmethod
    def plot_heatmap(
        price_surface: np.ndarray,
        S_grid: np.ndarray,
        T_grid: np.ndarray
    ) -> None:
        price_surface_t = price_surface.T
        
        fig_heatmap = px.imshow(
            price_surface_t,
            x=T_grid,
            y=S_grid,
            labels=dict(x="Time to Maturity", y="Underlying Price", color="Option Price"),
            title="Option Price Heatmap",
            color_continuous_scale="Viridis",
            aspect="auto"
        )
        
        fig_heatmap.update_layout(
            coloraxis_colorbar_title="Price",
            xaxis=dict(
                autorange="reversed",
                title="Time to Maturity"
            ),
            yaxis=dict(
                title="Underlying Price",
                autorange=True
            ),
            height=800,
            margin=dict(l=0, r=0, t=30, b=0)
        )
        st.plotly_chart(fig_heatmap, use_container_width=True)
