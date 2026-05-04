import streamlit as st
from PIL import Image, ImageDraw
from pathlib import Path


ASSETS_DIR = Path(__file__).resolve().parents[1] / "assets"
Image.MAX_IMAGE_PIXELS = None


@st.cache_data(show_spinner=False)
def _mars_circle_cutout(image_path: Path) -> Image.Image:
    img = Image.open(image_path).convert("RGBA")

    w, h = img.size
    size = min(w, h)
    left = (w - size) // 2
    top = (h - size) // 2
    img = img.crop((left, top, left + size, top + size))

    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size - 1, size - 1), fill=255)
    img.putalpha(mask)
    return img


@st.cache_data(show_spinner=False)
def _prepare_local_image(image_path: Path, output_name: str, max_width: int = 1800) -> Path:
    output_path = ASSETS_DIR / output_name
    if output_path.exists():
        return output_path

    img = Image.open(image_path)
    if img.width > max_width:
        new_height = int(img.height * max_width / img.width)
        img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
    img.save(output_path, quality=90, optimize=True)
    return output_path


def render_home_page(*, on_go_to_predict) -> None:
    st.markdown(
        """
        <div class="topbar-wrap">
            <div class="topbar-inner">
                <div class="topbar">
                    <div class="brand"><span class="brand-dot"></span> Mars Landform AI</div>
                    <nav class="topnav">
                        <a href="#introduction">Introduction</a>
                        <a href="#research">Research</a>
                        <a href="#data">Data</a>
                        <a href="#useful">Why useful</a>
                        <a href="#how">Instructions</a>
                    </nav>
                    <a class="nav-cta" href="?page=predict">PREDICT IMAGE</a>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div id="introduction" class="anchor"></div>', unsafe_allow_html=True)
    left, right = st.columns([1.35, 1], gap="large", vertical_alignment="center")
    with left:
        st.markdown(
            """
            <section class="hero" id="top">
                <div class="hero-inner">
                    <div class="hero-kicker">planetary surface intelligence</div>
                    <div class="hero-title">Classify Mars landforms from imagery.</div>
                    <div class="hero-subtitle">
                        Upload a Mars surface image and get instant automated classification using deep learning models.
                        Compare predictions across multiple architectures and accelerate your geological analysis workflow.
                    </div>
                    <div class="hero-cta">
                        <!-- Buttons rendered by Streamlit below -->
                    </div>
                    <div class="hero-meta">
                        <div class="meta-card">
                            <div class="meta-label">Models</div>
                            <div class="meta-value">4 with comparison</div>
                        </div>
                        <div class="meta-card">
                            <div class="meta-label">Input</div>
                            <div class="meta-value">JPG / PNG</div>
                        </div>
                        <div class="meta-card">
                            <div class="meta-label">Output</div>
                            <div class="meta-value">Class + confidence</div>
                        </div>
                        <div class="meta-card">
                            <div class="meta-label">Goal</div>
                            <div class="meta-value">Faster review</div>
                        </div>
                    </div>
                </div>
            </section>
            """,
            unsafe_allow_html=True,
        )

        # Keep the landing clean: primary CTA is in the navbar.
        # Provide an optional in-body CTA only on small screens.
        st.markdown('<div class="hero-cta-btn"></div>', unsafe_allow_html=True)
        if st.button("Predict image", type="primary", use_container_width=False):
            on_go_to_predict()

    with right:
        mars = _mars_circle_cutout(ASSETS_DIR / "mars_cutout.jpg")
        st.markdown('<div class="mars-cutout">', unsafe_allow_html=True)
        st.image(mars, caption=None, width=420)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="section anchor" id="research"></div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="section-title">Introduction & research context</div>
        <div class="section-subtitle">
            Automated recognition of Mars surface features to accelerate planetary science workflows and research.
        </div>
        """,
        unsafe_allow_html=True,
    )
    r_left, r_right = st.columns([1.15, 1], gap="large", vertical_alignment="center")
    with r_left:
        st.markdown(
            """
            <div class="card">
                <span class="pill">What does this website do?</span>
                <div style="height: 10px"></div>
                Analyzes Mars surface images using deep learning models to automatically classify landforms (craters, dunes, ridges, etc.)
                and returns the predicted class with a confidence score for expert review.
            </div>
            <div class="card">
                <span class="pill">Why is it useful?</span>
                <div style="height: 10px"></div>
                <b>Real-world applications:</b> Geologists and planetary scientists can dramatically reduce manual analysis time. Use for rapid priority mapping,
                identifying regions of scientific interest, automating large-scale surveys, and supporting rover mission planning. Also valuable for
                educational datasets, research publications, and validating analysis pipelines before deployment.
            </div>
            """,
            unsafe_allow_html=True,
        )
    with r_right:
        st.markdown(
            """
            <div class="card tall-fit" style="min-height: 350px;">
                <div style="font-size: 1.18rem; font-weight: 700; margin: 0 0 6px 0; color: rgba(255,255,255,0.92); letter-spacing: -0.01em;">Where this fits</div>
                <div style="height: 8px;"></div>
                <p style="margin: 0 0 8px 0; color: rgba(255,255,255,0.84);">
                    A practical tool for speeding expert workflows — not a replacement for domain review. Common uses include:
                </p>
                <ul style="margin: 6px 0 8px 18px; color: rgba(255,255,255,0.72);">
                    <li><b>Automated screening:</b> Triage large imagery collections to surface likely craters, dunes, and other features for human review.</li>
                    <li><b>Model benchmarking:</b> Compare outputs across architectures to find consensus and failure modes.</li>
                    <li><b>Data curation & QA:</b> Flag low-quality or mislabeled images to improve training sets.</li>
                    <li><b>Mission planning support:</b> Quickly identify candidate regions of interest for further analysis.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown('<div class="section anchor" id="data"></div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="section-title">Data source</div>
        <div class="section-subtitle">Training data from high-resolution Mars orbital imagery.</div>
        """,
        unsafe_allow_html=True,
    )
    d_left, d_right = st.columns([1.2, 1], gap="large", vertical_alignment="top")
    with d_left:
        st.markdown(
            """
            <div class="card">
                <span class="pill">Dataset overview</span>
                <div style="height: 10px"></div>
                <b>Source:</b> Mars Reconnaissance Orbiter (MRO) and HIRISE instrument products
                <div style="height: 8px"></div>
                <b>Classes:</b> Craters, dunes, ridges, and other geological features
                <div style="height: 8px"></div>
                <b>Preprocessing:</b> Image normalization, augmentation for model robustness, and standardized sizing
                <div style="height: 8px"></div>
                <b>Split:</b> Training, validation, and test sets for comprehensive model evaluation
                <div style="height: 8px"></div>
                All data is sourced from publicly available NASA planetary science archives.
            </div>
            """,
            unsafe_allow_html=True,
        )
    with d_right:
        st.markdown('<div style="display: flex; justify-content: center; align-items: flex-start; height: 30%; min-height: 50px;"><div style="width: 84%; max-width: 240px; margin-top: 20px;">', unsafe_allow_html=True)
        mars_surface_path = _prepare_local_image(ASSETS_DIR / "mars_surface_detail.jpg", "mars_surface_detail_small.jpg")
        st.image(
            str(mars_surface_path),
            caption="Mars surface detail (NASA/JPL)",
            width="stretch",
        )
        st.markdown('</div></div>', unsafe_allow_html=True)

    st.markdown('<div class="section anchor" id="models"></div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="section-title">Models</div>
        <div class="section-subtitle">Choose one model or compare all models side-by-side.</div>
        """,
        unsafe_allow_html=True,
    )
    m1, m2, m3, m4 = st.columns(4, gap="medium")
    model_descriptions = {
        "EfficientNet-B0": "Efficient architecture with excellent parameter efficiency strong accuracy on varied surface textures while remaining compact.",
        "MobileNet-V2": "Lightweight and fast: optimized for mobile/edge use with a good speed/accuracy trade-off on terrain patches.",
        "ResNet-50": "Deep residual backbone delivering robust feature extraction and high accuracy on complex terrain structures.",
        "Custom CNN": "Task-tailored model trained on curated Mars data — tuned for niche classes and dataset-specific performance improvements.",
    }

    for col, name in zip([m1, m2, m3, m4], list(model_descriptions.keys()), strict=False):
        desc = model_descriptions.get(name, "General-purpose model suitable for surface classification tasks.")
        with col:
            st.markdown(
                f"""
                <div class="card">
                    <span class="pill">Model</span>
                    <div style="height: 10px"></div>
                    <div style="font-weight: 700; color: rgba(255,255,255,0.92); font-size: 1.05rem;">{name}</div>
                    <div style="height: 8px"></div>
                    <div style="color: rgba(255,255,255,0.68);">
                        {desc}
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown('<div class="section anchor" id="how"></div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="section-title">How to use</div>
        <div class="section-subtitle">Simple 4-step workflow for fast predictions and model comparison.</div>
        """,
        unsafe_allow_html=True,
    )
    h_left, h_right = st.columns([1, 1], gap="large", vertical_alignment="top")
    with h_left:
        st.markdown(
            """
            <div class="card same-height">
                <div>
                    <span class="pill">Instructions</span>
                    <div style="height: 10px"></div>
                <ol style="margin: 0 0 0 18px; padding: 0; color: rgba(255,255,255,0.72);">
                    <li style="margin: 8px 0;"><b>Click "Predict Image"</b> in the top right</li>
                    <li style="margin: 8px 0;"><b>Upload a Mars surface image</b> (JPG or PNG)</li>
                    <li style="margin: 8px 0;"><b>Select a model or "All Models"</b> to compare</li>
                    <li style="margin: 8px 0;"><b>Click "Predict"</b> and review results</li>
                </ol>
                </div>
                <div style="height: 8px;"></div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with h_right:
        st.markdown(
            """
            <div class="card same-height">
                <div>
                    <span class="pill">What you'll see</span>
                    <div style="height: 10px"></div>
                <ul style="margin: 0 0 0 18px; padding: 0; color: rgba(255,255,255,0.72);">
                    <li style="margin: 8px 0;"><b>Single model:</b> Predicted class and confidence %</li>
                    <li style="margin: 8px 0;"><b>All models:</b> Side-by-side comparison for consensus</li>
                    <li style="margin: 8px 0;"><b>Confidence scores:</b> Certainty level for each prediction</li>
                </ul>
                <div style="height: 14px"></div>
                <div>
                    <span class="pill">Tip</span>
                    <span style="color: rgba(255,255,255,0.68); margin-left: 8px; font-size: 0.95rem;">
                        Use centered, clear terrain patches for best accuracy.
                    </span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

