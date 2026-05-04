import streamlit as st
from PIL import Image

from utils.model_utils import load_models, preprocess_image, predict_with_model, BEST_MODEL_NAME


MODEL_SEQUENCE = ["EfficientNet-B0", "MobileNet-V2", "ResNet-50", "Custom CNN"]


@st.cache_resource(show_spinner="loading models...")
def _get_models():
    return load_models()


@st.dialog("Preview image")
def _show_preview_dialog(image: Image.Image) -> None:
    st.image(image, caption="Attached Mars image", width=320)


def _render_result_card(
    *,
    title: str,
    predicted_class: str,
    confidence: str,
    probabilities: dict,
    error: str | None = None,
) -> None:
    with st.container(border=True):
        st.markdown(f'<div class="result-card-title">{title}</div>', unsafe_allow_html=True)
        if error:
            st.error(f"model error: {error}")
            return
        st.markdown(f'<div class="result-card-class">{predicted_class}</div>', unsafe_allow_html=True)
        st.write(f"Prediction: **{predicted_class}**")
        st.write(f"Confidence: **{confidence}**")
        if probabilities:
             with st.expander(" ", expanded=False):
                for cls, prob in sorted(probabilities.items(), key=lambda x: x[1], reverse=True):
                    st.write(f"{cls}: {prob:.1%}")

def render_prediction_page(*, on_back_to_home) -> None:
    # ── Back button ──────────────────────────────────────────────────────────
    back_col, _ = st.columns([1, 5])
    with back_col:
        if st.button("Back", type="secondary", use_container_width=True):
            on_back_to_home()
            st.rerun()

    st.markdown('<div class="section-title" style="margin-top:0.6rem;">Predict</div>',
                unsafe_allow_html=True)

    if "prediction_preview_visible" not in st.session_state:
        st.session_state.prediction_preview_visible = False
    if "prediction_mode_compare" not in st.session_state:
        st.session_state.prediction_mode_compare = False

    # ── load models once ─────────────────────────────────────────────────────
    models = _get_models()

    # ── Setup panel ──────────────────────────────────────────────────────────
    with st.container(border=True):
        st.markdown('<div class="section-title">Prediction setup</div>', unsafe_allow_html=True)
        st.toggle("Compare all 4 models", key="prediction_mode_compare")

        st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
        st.markdown('<div class="section-subtitle">Drop MARS image here</div>', unsafe_allow_html=True)

        uploaded_file = st.file_uploader(
            "Upload MARS image",
            type=["jpg", "jpeg", "png"],
            accept_multiple_files=False,
            label_visibility="collapsed",
        )

        st.markdown("<div style='height:0.55rem'></div>", unsafe_allow_html=True)

        preview_col, predict_col = st.columns(2)
        with preview_col:
            if st.button("Preview image", use_container_width=True):
                st.session_state.prediction_preview_visible = True
        with predict_col:
            predict_clicked = st.button("Predict", type="primary", use_container_width=True)

        if st.session_state.prediction_preview_visible:
            if uploaded_file is not None:
                _show_preview_dialog(Image.open(uploaded_file))
                st.session_state.prediction_preview_visible = False
            else:
                st.info("Upload an image first, then click Preview image.")

    # ── Prediction output ────────────────────────────────────────────────────
    if predict_clicked:
        if uploaded_file is None:
            st.warning("Please upload a Mars image before predicting.")
        else:
            image = preprocess_image(Image.open(uploaded_file))

            st.markdown(
                '<div class="section-title" style="margin-top:1.2rem;">Prediction output</div>',
                unsafe_allow_html=True,
            )

            if st.session_state.prediction_mode_compare:
                columns = st.columns(4)
                for column, model_name in zip(columns, MODEL_SEQUENCE):
                    result = predict_with_model(models[model_name], image)
                    with column:
                        _render_result_card(
                            title=model_name,
                            predicted_class=result["predicted_class"],
                            confidence=f"{result['confidence']:.1%}",
                            probabilities=result.get("probabilities", {}),
                            error=result.get("error"),
                        )
            else:
                result = predict_with_model(models[BEST_MODEL_NAME], image)
                _render_result_card(
                    title=f"Best Model — {BEST_MODEL_NAME}",
                    predicted_class=result["predicted_class"],
                    confidence=f"{result['confidence']:.1%}",
                    probabilities=result.get("probabilities", {}),
                    error=result.get("error"),
                )

    st.caption(f"Available models: {', '.join(MODEL_SEQUENCE)}")