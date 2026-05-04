import streamlit as st

from views.home import render_home_page
from views.prediction import render_prediction_page
from ui.styles import apply_global_style


st.set_page_config(
    page_title="Mars Landform Classification",
    page_icon="M",
    layout="wide",
    initial_sidebar_state="collapsed",
)

apply_global_style()

if "page" not in st.session_state:
    st.session_state.page = "home"

query_page = st.query_params.get("page")
if query_page in {"home", "predict"} and st.session_state.page != query_page:
    st.session_state.page = query_page


def _go_to_predict() -> None:
    st.session_state.page = "predict"
    st.query_params["page"] = "predict"


def _go_to_home() -> None:
    st.session_state.page = "home"
    st.query_params["page"] = "home"


if st.session_state.page == "home":
    render_home_page(on_go_to_predict=_go_to_predict)
else:
    render_prediction_page(on_back_to_home=_go_to_home)
