import streamlit as st


def apply_global_style() -> None:
    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

            .stApp {
                background: linear-gradient(135deg, #0d0607 0%, #140708 55%, #1c090a 100%);
                color: rgba(255, 255, 255, 0.92);
            }

            html {
                scroll-behavior: smooth;
            }

            :root {
                --bg: #0d0607;
                --panel: rgba(255, 255, 255, 0.04);
                --panel-2: rgba(255, 255, 255, 0.06);
                --border: rgba(255, 255, 255, 0.10);
                --muted: rgba(255, 255, 255, 0.72);
                --muted-2: rgba(255, 255, 255, 0.60);
                --accent: #ff4d2a;
                --accent-2: #ff7a55;
                --shadow: 0 28px 70px rgba(0, 0, 0, 0.42);
            }

            [data-testid="stSidebar"],
            [data-testid="stSidebarCollapsedControl"] {
                display: none !important;
            }

            header[data-testid="stHeader"],
            footer {
                visibility: hidden;
                height: 0 !important;
            }

            section.main > div.block-container {
                max-width: 1140px;
                padding-top: 5.2rem;
                padding-bottom: 3.2rem;
            }

            h1, h2, h3, h4 {
                font-family: "Inter", system-ui, -apple-system, Segoe UI, Roboto, "Helvetica Neue", Arial, sans-serif !important;
                letter-spacing: -0.02em;
                color: rgba(255, 255, 255, 0.94);
            }

            p, li, label, [data-testid="stMarkdownContainer"] {
                font-family: "Inter", system-ui, -apple-system, Segoe UI, Roboto, "Helvetica Neue", Arial, sans-serif !important;
                color: var(--muted);
                font-size: 1rem;
                line-height: 1.55;
            }

            a {
                color: rgba(255, 255, 255, 0.86);
                text-decoration: none;
            }

            a:hover {
                color: rgba(255, 255, 255, 0.96);
            }

            /* top nav */
            .topbar {
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 0.75rem 0;
            }

            .topbar-wrap {
                position: fixed;
                top: 0;
                left: 0;
                right: 0;
                z-index: 1000;
                padding: 0.35rem 0;
                background: linear-gradient(180deg, rgba(13, 6, 7, 0.92) 0%, rgba(13, 6, 7, 0.70) 100%);
                backdrop-filter: blur(10px);
                border-bottom: 1px solid rgba(255, 255, 255, 0.08);
            }

            .topbar-inner {
                max-width: 1140px;
                margin: 0 auto;
                padding: 0 1rem;
            }

            .brand {
                display: inline-flex;
                align-items: center;
                gap: 0.55rem;
                font-weight: 700;
                letter-spacing: 0.02em;
                color: rgba(255, 255, 255, 0.9);
            }

            .brand-dot {
                width: 10px;
                height: 10px;
                border-radius: 999px;
                background: radial-gradient(circle, var(--accent-2) 0%, var(--accent) 70%);
                box-shadow: 0 0 22px rgba(255, 77, 42, 0.35);
            }

            .topnav {
                display: flex;
                gap: 1.1rem;
                color: rgba(255, 255, 255, 0.80);
                font-weight: 500;
                font-size: 0.95rem;
            }

            .topnav a {
                color: rgba(255, 255, 255, 0.78);
                text-decoration: none;
                border-bottom: 2px solid transparent;
                transition: all 200ms ease;
            }

            .topnav a:hover {
                color: rgba(255, 255, 255, 0.92);
                border-bottom: 2px solid rgba(255, 255, 255, 0.92);
            }

            .nav-cta {
                display: inline-flex;
                align-items: center;
                justify-content: center;
                padding: 0.58rem 0.95rem;
                border-radius: 999px;
                border: 1px solid rgba(255, 255, 255, 0.14);
                background: radial-gradient(120% 180% at 20% 0%, var(--accent-2) 0%, var(--accent) 50%, #ff3a1b 100%);
                color: rgba(255, 255, 255, 0.98) !important;
                font-weight: 800;
                letter-spacing: 0.02em;
                font-size: 0.92rem;
                box-shadow: 0 18px 40px rgba(255, 77, 42, 0.18);
                transition: transform 120ms ease, filter 120ms ease;
                white-space: nowrap;
                text-decoration: none !important;
                border-bottom: none !important;
            }

            .nav-cta:visited {
                color: rgba(255, 255, 255, 0.98) !important;
                text-decoration: none !important;
            }

            .nav-cta:hover {
                filter: brightness(1.06);
                transform: translateY(-1px);
                color: rgba(255, 255, 255, 0.98);
                text-decoration: none !important;
                border-bottom: none !important;
            }

            .anchor {
                scroll-margin-top: 130px;
            }

            /* hero */
            .hero {
                position: relative;
                border: 1px solid var(--border);
                border-radius: 26px;
                background: linear-gradient(180deg, rgba(255, 255, 255, 0.06) 0%, rgba(255, 255, 255, 0.03) 100%);
                box-shadow: var(--shadow);
                overflow: hidden;
            }

            .hero-inner {
                padding: 2.0rem 2.3rem 2.2rem;
            }

            .hero-kicker {
                color: rgba(255, 255, 255, 0.68);
                text-transform: uppercase;
                letter-spacing: 0.22em;
                font-size: 0.78rem;
                margin-bottom: 0.75rem;
            }

            .hero-title {
                font-size: 3.1rem;
                font-weight: 800;
                line-height: 1.04;
                margin: 0 0 0.9rem 0;
                color: rgba(255, 255, 255, 0.96);
                letter-spacing: -0.03em;
            }

            .hero-subtitle {
                max-width: 52ch;
                font-size: 1.05rem;
                color: rgba(255, 255, 255, 0.72);
                margin-bottom: 1.4rem;
            }

            .hero-cta {
                display: flex;
                align-items: center;
                gap: 0.75rem;
                margin-top: 0.3rem;
            }

            .hero-meta {
                display: grid;
                grid-template-columns: repeat(4, minmax(0, 1fr));
                gap: 0.8rem;
                margin-top: 1.25rem;
            }

            .meta-card {
                border: 1px solid rgba(255, 255, 255, 0.10);
                background: rgba(0, 0, 0, 0.10);
                border-radius: 16px;
                padding: 0.9rem 0.95rem;
                position: relative;
                overflow: hidden;
            }

            .meta-card::after {
                content: "";
                position: absolute;
                top: -60%;
                left: -45%;
                width: 140%;
                height: 220%;
                background: linear-gradient(
                    120deg,
                    rgba(255, 255, 255, 0) 0%,
                    rgba(255, 255, 255, 0.05) 35%,
                    rgba(255, 255, 255, 0.16) 50%,
                    rgba(255, 255, 255, 0.05) 65%,
                    rgba(255, 255, 255, 0) 100%
                );
                transform: translateX(-22%) rotate(8deg);
                opacity: 0.0;
                transition: opacity 180ms ease, transform 520ms ease;
                pointer-events: none;
            }

            .meta-card:hover::after {
                opacity: 1;
                transform: translateX(30%) rotate(8deg);
            }

            .meta-label {
                color: rgba(255, 255, 255, 0.60);
                font-size: 0.74rem;
                letter-spacing: 0.16em;
                text-transform: uppercase;
            }

            .meta-value {
                margin-top: 0.35rem;
                color: rgba(255, 255, 255, 0.92);
                font-weight: 600;
                font-size: 0.98rem;
            }

            /* sections */
            .section {
                padding: 2.1rem 0 0.2rem 0;
            }

            .section-title {
                font-size: 1.25rem;
                font-weight: 700;
                margin: 0 0 0.55rem 0;
                color: rgba(255, 255, 255, 0.92);
                letter-spacing: -0.01em;
            }

            .section-subtitle {
                color: rgba(255, 255, 255, 0.68);
                margin: 0 0 1.0rem 0;
            }

            .card {
                border: 1px solid var(--border);
                border-radius: 18px;
                background: linear-gradient(180deg, rgba(255, 255, 255, 0.06) 0%, rgba(255, 255, 255, 0.03) 100%);
                padding: 1.0rem 1.05rem;
                box-shadow: 0 14px 40px rgba(0, 0, 0, 0.24);
            }

            .card + .card {
                margin-top: 0.9rem;
            }

            .tall-fit {
                min-height: 380px;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
            }

            .same-height {
                height: 100%;
                min-height: 150px;
                display: flex;
                flex-direction: column;
                justify-content: space-between;
            }

            /* prediction page */
            .predict-hero {
                border: 1px solid var(--border);
                border-radius: 22px;
                padding: 1.05rem 1.1rem;
                background: linear-gradient(180deg, rgba(255, 255, 255, 0.06) 0%, rgba(255, 255, 255, 0.03) 100%);
                box-shadow: var(--shadow);
            }

            .predict-kicker {
                color: rgba(255, 255, 255, 0.68);
                text-transform: uppercase;
                letter-spacing: 0.20em;
                font-size: 0.76rem;
                margin-bottom: 0.45rem;
            }

            .predict-title {
                font-size: 2rem;
                font-weight: 800;
                line-height: 1.06;
                color: rgba(255, 255, 255, 0.96);
                letter-spacing: -0.03em;
            }

            .predict-subtitle {
                margin-top: 0.55rem;
                color: rgba(255, 255, 255, 0.72);
            }

            .predict-layout {
                display: grid;
                gap: 1rem;
            }

            .predict-panel {
                border: 1px solid var(--border);
                border-radius: 18px;
                background: linear-gradient(180deg, rgba(255, 255, 255, 0.05) 0%, rgba(255, 255, 255, 0.03) 100%);
                padding: 1rem 1.05rem;
                box-shadow: 0 14px 40px rgba(0, 0, 0, 0.24);
                margin-bottom: 0.9rem;
            }

            .predict-panel-wide {
                margin-bottom: 0;
            }

            .mode-summary {
                display: flex;
                flex-wrap: wrap;
                gap: 0.55rem;
                margin-top: 0.6rem;
            }

            .mode-pill,
            .mode-chip {
                display: inline-flex;
                align-items: center;
                justify-content: center;
                padding: 0.4rem 0.7rem;
                border-radius: 999px;
                border: 1px solid rgba(255, 255, 255, 0.12);
                background: rgba(0, 0, 0, 0.12);
                color: rgba(255, 255, 255, 0.74);
                font-size: 0.85rem;
                font-weight: 600;
            }

            .mode-chip.active {
                background: linear-gradient(120deg, rgba(255, 122, 85, 0.28), rgba(255, 77, 42, 0.24));
                border-color: rgba(255, 122, 85, 0.45);
                color: rgba(255, 255, 255, 0.96);
            }

            .predict-results {
                margin-top: 1.1rem;
            }

            /* ── Result cards ──────────────────────────────────────────── */
            .result-card {
                border: 1px solid rgba(255,255,255,0.10);
                border-radius: 16px;
                background: linear-gradient(160deg, rgba(255,255,255,0.07) 0%, rgba(255,255,255,0.03) 100%);
                padding: 0.85rem 1rem;
                box-shadow: 0 10px 32px rgba(0,0,0,0.28);
                display: flex;
                flex-direction: column;
                gap: 0.6rem;
            }

            .result-card-title {
                color: rgba(255,255,255,0.50);
                text-transform: uppercase;
                letter-spacing: 0.14em;
                font-size: 0.68rem;
                font-weight: 600;
            }

            .result-card-class {
                font-size: 1.05rem;
                font-weight: 800;
                color: rgba(255,255,255,0.96);
                letter-spacing: -0.01em;
            }

            .result-metric {
                display: flex;
                flex-direction: column;
                gap: 0.25rem;
            }

            .result-metric-header {
                display: flex;
                justify-content: space-between;
                align-items: center;
            }

            .result-metric-label {
                color: rgba(255,255,255,0.48);
                font-size: 0.70rem;
                text-transform: uppercase;
                letter-spacing: 0.12em;
                font-weight: 500;
            }

            .result-metric-value {
                color: rgba(255,255,255,0.88);
                font-size: 0.78rem;
                font-weight: 700;
            }

            .result-bar-track {
                width: 100%;
                height: 7px;
                background: rgba(255,255,255,0.08);
                border-radius: 99px;
                overflow: hidden;
            }

            .result-bar-fill {
                height: 100%;
                border-radius: 99px;
            }

            /* ── Grid layouts ─────────────────────────────────────────── */
            .results-grid {
                display: grid;
                gap: 0.85rem;
                margin-bottom: 1rem;
            }

            .results-grid.single-up {
                grid-template-columns: minmax(0, 320px);
            }

            .results-grid.four-up {
                grid-template-columns: repeat(4, minmax(0, 1fr));
                align-items: stretch;
            }

            @media (max-width: 992px) {
                .hero-meta {
                    grid-template-columns: repeat(2, minmax(0, 1fr));
                }

                .results-grid.four-up {
                    grid-template-columns: repeat(2, minmax(0, 1fr));
                }
            }

            @media (max-width: 700px) {
                section.main > div.block-container {
                    padding-top: 5.5rem;
                }

                .hero-inner {
                    padding: 1.5rem 1.2rem;
                }

                .hero-title {
                    font-size: 2.15rem;
                }

                .predict-title {
                    font-size: 1.55rem;
                }

                .results-grid.four-up {
                    grid-template-columns: 1fr;
                }

                .results-grid.single-up {
                    grid-template-columns: 1fr;
                }
            }

            .hero-cta-btn {
                margin-top: 0.35rem;
            }

            .research-grid {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 1.15rem;
                align-items: start;
            }

            .research-left {
                display: grid;
                grid-template-rows: auto auto;
                gap: 0.75rem;
            }

            .research-right {
                display: grid;
                grid-template-rows: 1fr;
            }

            .pill {
                display: inline-flex;
                align-items: center;
                gap: 0.45rem;
                padding: 0.36rem 0.7rem;
                border-radius: 999px;
                border: 1px solid rgba(255, 255, 255, 0.12);
                background: rgba(0, 0, 0, 0.14);
                color: rgba(255, 255, 255, 0.70);
                font-size: 0.86rem;
                font-weight: 500;
            }

            [data-testid="stImage"] img {
                border-radius: 22px;
            }

            .mars-cutout img {
                border-radius: 999px !important;
                background: transparent !important;
                box-shadow: 0 28px 70px rgba(0, 0, 0, 0.55);
            }

            /* Buttons */
            .stButton > button {
                border-radius: 999px !important;
                border: 1px solid rgba(255, 255, 255, 0.14) !important;
                background: radial-gradient(120% 180% at 20% 0%, var(--accent-2) 0%, var(--accent) 50%, #ff3a1b 100%) !important;
                color: rgba(255, 255, 255, 0.96) !important;
                font-weight: 700 !important;
                letter-spacing: 0.01em !important;
                padding: 0.68rem 1.1rem !important;
                box-shadow: 0 18px 40px rgba(255, 77, 42, 0.22) !important;
                transition: transform 120ms ease, filter 120ms ease;
            }

            .stButton > button:hover {
                filter: brightness(1.06);
                transform: translateY(-1px);
            }

            .stButton > button:active {
                transform: translateY(0px);
            }

            .stButton > button[kind="secondary"] {
                background: rgba(255, 255, 255, 0.06) !important;
                color: rgba(255, 255, 255, 0.92) !important;
                border: 1px solid rgba(255, 255, 255, 0.14) !important;
                box-shadow: none !important;
            }

            .stButton > button[kind="secondary"]:hover {
                background: rgba(255, 255, 255, 0.09) !important;
            }

            /* inputs */
            .stSelectbox div[data-baseweb="select"] > div,
            .stFileUploader > div {
                background: rgba(255, 255, 255, 0.05);
                border: 1px solid rgba(255, 255, 255, 0.12);
                border-radius: 14px;
            }

            .stFileUploader label {
                display: none !important;
            }

            [data-testid="stDataFrame"] {
                border: 1px solid rgba(255, 255, 255, 0.10);
                border-radius: 14px;
                overflow: hidden;
            }

            @media (max-width: 900px) {
                .hero-title {
                    font-size: 2.2rem;
                }

                .hero-meta {
                    grid-template-columns: repeat(2, minmax(0, 1fr));
                }

                .topnav {
                    display: none;
                }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )