import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# ==========================================
# KONFIGURASI HALAMAN
# ==========================================

st.set_page_config(
    page_title="SPK Influencer - SAW Method",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# CUSTOM CSS / DESAIN MODERN & MINIMALIS
# ==========================================

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&display=swap');

    /* Global Typography & Colors */
    html, body, [class*="css"], .stApp {
        font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
        background-color: #f8fafc !important;
        color: #1e293b;
    }

    /* Top Accent Line */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #1d4ed8, #2563eb, #3b82f6, #60a5fa);
        z-index: 999999;
    }

    /* Headings */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-weight: 700 !important;
        color: #0f172a !important;
        letter-spacing: -0.02em;
    }

    /* Page Header */
    .header-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 5px 14px;
        border-radius: 9999px;
        font-size: 11.5px;
        font-weight: 700;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        background: #eff6ff;
        color: #2563eb;
        border: 1px solid #bfdbfe;
        margin-bottom: 8px;
    }

    .main-title {
        font-size: 28px;
        font-weight: 800;
        color: #0f172a;
        margin: 0 0 4px 0;
        line-height: 1.25;
    }

    .sub-title {
        color: #64748b;
        font-size: 14.5px;
        margin: 0 0 24px 0;
        line-height: 1.5;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #091428 0%, #0d2146 50%, #172554 100%) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
    }

    .sidebar-brand-card {
        padding: 16px;
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 14px;
        margin-bottom: 20px;
        backdrop-filter: blur(10px);
    }

    .sidebar-brand-title {
        font-size: 17px;
        font-weight: 800;
        color: #ffffff !important;
        letter-spacing: -0.01em;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .sidebar-brand-sub {
        font-size: 12px;
        color: #93c5fd !important;
        margin-top: 3px;
        font-weight: 400;
    }

    .sidebar-tag {
        display: inline-block;
        padding: 2px 8px;
        background: rgba(37, 99, 235, 0.4);
        border: 1px solid rgba(96, 165, 250, 0.4);
        border-radius: 6px;
        font-size: 10px;
        color: #dbeafe !important;
        font-weight: 600;
        margin-top: 8px;
    }

    /* Sidebar Nav Radio Options */
    [data-testid="stSidebar"] [data-testid="stRadio"] > div {
        gap: 8px !important;
    }

    [data-testid="stSidebar"] [data-testid="stRadio"] label {
        background: rgba(255, 255, 255, 0.04) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        padding: 10px 14px !important;
        border-radius: 10px !important;
        color: #f1f5f9 !important;
        transition: all 0.2s ease !important;
        cursor: pointer !important;
        font-size: 13.5px !important;
        font-weight: 500 !important;
    }

    [data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
        background: rgba(255, 255, 255, 0.12) !important;
        border-color: rgba(96, 165, 250, 0.5) !important;
        transform: translateX(3px);
    }

    [data-testid="stSidebar"] [data-testid="stRadio"] label[data-checked="true"] {
        background: linear-gradient(90deg, rgba(37, 99, 235, 0.6) 0%, rgba(59, 130, 246, 0.35) 100%) !important;
        border: 1px solid #3b82f6 !important;
        box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25) !important;
        font-weight: 600 !important;
    }

    .sidebar-info-box {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 14px;
        margin-top: 20px;
    }

    .sidebar-info-box p {
        color: #cbd5e1 !important;
        font-size: 12px !important;
        margin: 0 !important;
        line-height: 1.5;
    }

    /* Metric Cards */
    div[data-testid="stMetric"] {
        background-color: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        padding: 18px 20px !important;
        border-radius: 14px !important;
        box-shadow: 0 4px 12px -2px rgba(15, 23, 42, 0.04), 0 2px 4px -1px rgba(15, 23, 42, 0.02) !important;
        transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;
        position: relative;
        overflow: hidden;
    }

    div[data-testid="stMetric"]::before {
        content: "";
        position: absolute;
        top: 0;
        left: 0;
        width: 4px;
        height: 100%;
        background: linear-gradient(180deg, #2563eb 0%, #3b82f6 100%);
    }

    div[data-testid="stMetric"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px -3px rgba(37, 99, 235, 0.12) !important;
        border-color: #cbd5e1 !important;
    }

    div[data-testid="stMetricLabel"] {
        color: #64748b !important;
        font-size: 12.5px !important;
        font-weight: 600 !important;
        text-transform: uppercase;
        letter-spacing: 0.03em;
    }

    div[data-testid="stMetricValue"] {
        color: #0f172a !important;
        font-weight: 800 !important;
        font-size: 26px !important;
    }

    /* Unified Modern Table / Dataframe / DataEditor Styling */
    [data-testid="stDataFrame"], [data-testid="stDataEditor"] {
        background-color: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 14px !important;
        overflow: hidden !important;
        box-shadow: 0 4px 12px -2px rgba(15, 23, 42, 0.04) !important;
    }

    /* Force background inside glide data grid container to stay pure light */
    div[data-testid="stDataFrame"] > div, 
    div[data-testid="stDataEditor"] > div {
        background-color: #ffffff !important;
    }

    /* Hero Winner Spotlight Card */
    .winner-card {
        background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 55%, #3b82f6 100%);
        border-radius: 16px;
        padding: 24px;
        color: #ffffff;
        box-shadow: 0 10px 25px -5px rgba(37, 99, 235, 0.3), 0 8px 10px -6px rgba(37, 99, 235, 0.2);
        position: relative;
        overflow: hidden;
    }

    .winner-card::after {
        content: "";
        position: absolute;
        top: -30%;
        right: -15%;
        width: 180px;
        height: 180px;
        background: radial-gradient(circle, rgba(255,255,255,0.2) 0%, rgba(255,255,255,0) 70%);
        border-radius: 50%;
        pointer-events: none;
    }

    .winner-badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        background: rgba(255, 255, 255, 0.2);
        border: 1px solid rgba(255, 255, 255, 0.3);
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 11.5px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 12px;
        backdrop-filter: blur(4px);
    }

    .winner-name {
        font-size: 26px;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 4px;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .winner-score-box {
        background: rgba(255, 255, 255, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.25);
        border-radius: 12px;
        padding: 12px 18px;
        margin-top: 14px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .winner-score-val {
        font-size: 28px;
        font-weight: 800;
        color: #ffffff;
        line-height: 1;
    }

    .winner-score-lbl {
        font-size: 11.5px;
        color: #dbeafe;
        font-weight: 600;
        letter-spacing: 0.03em;
    }

    /* Buttons */
    div.stButton > button {
        background: linear-gradient(180deg, #2563eb 0%, #1d4ed8 100%) !important;
        color: #ffffff !important;
        border: 1px solid #1d4ed8 !important;
        border-radius: 10px !important;
        padding: 9px 20px !important;
        font-weight: 600 !important;
        font-size: 13.5px !important;
        box-shadow: 0 4px 10px rgba(37, 99, 235, 0.22) !important;
        transition: all 0.2s ease !important;
    }

    div.stButton > button:hover {
        background: linear-gradient(180deg, #1d4ed8 0%, #1e40af 100%) !important;
        box-shadow: 0 6px 14px rgba(37, 99, 235, 0.35) !important;
        transform: translateY(-1px);
    }

    /* Secondary / Alternate Buttons */
    div.stButton > button[kind="secondary"] {
        background: #ffffff !important;
        color: #334155 !important;
        border: 1px solid #cbd5e1 !important;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05) !important;
    }
    div.stButton > button[kind="secondary"]:hover {
        background: #f8fafc !important;
        border-color: #94a3b8 !important;
        color: #0f172a !important;
    }

    /* Expanders */
    div[data-testid="stExpander"] {
        background-color: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
        border-radius: 12px !important;
        box-shadow: 0 2px 6px -1px rgba(15, 23, 42, 0.04) !important;
        margin-bottom: 14px !important;
    }

    div[data-testid="stExpander"] summary {
        font-weight: 650 !important;
        color: #0f172a !important;
        padding: 14px 18px !important;
    }

    /* Minimalist Info Card */
    .info-card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 20px;
        margin-bottom: 16px;
        box-shadow: 0 4px 12px -2px rgba(15, 23, 42, 0.04);
    }

    .info-card-header {
        font-size: 15px;
        font-weight: 700;
        color: #0f172a;
        margin-bottom: 6px;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .info-card-body {
        font-size: 13.5px;
        color: #64748b;
        line-height: 1.5;
    }

    /* Badges */
    .badge-benefit {
        display: inline-block;
        padding: 3px 10px;
        border-radius: 6px;
        font-size: 11.5px;
        font-weight: 600;
        background-color: #eff6ff;
        color: #1d4ed8;
        border: 1px solid #bfdbfe;
    }

    .badge-cost {
        display: inline-block;
        padding: 3px 10px;
        border-radius: 6px;
        font-size: 11.5px;
        font-weight: 600;
        background-color: #fff7ed;
        color: #c2410c;
        border: 1px solid #fed7aa;
    }

    /* Clean Dividers */
    hr {
        border: none;
        height: 1px;
        background-color: #e2e8f0;
        margin: 24px 0;
    }

    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# DATA DEFAULT & INISIALISASI SESSION STATE
# ==========================================

DEFAULT_DATA = pd.DataFrame({
    "Alternatif": [
        "Creator A",
        "Creator B",
        "Creator C",
        "Creator D",
        "Creator E"
    ],
    "Engagement Rate": [6.5, 4.8, 8.0, 5.5, 7.2],
    "Kesesuaian Audiens": [85, 95, 75, 90, 80],
    "Biaya Kerja Sama": [
        1500000, 2000000, 1000000, 1200000, 1800000
    ],
    "Kualitas Konten": [4, 5, 3, 4, 5],
    "Brand Safety": [5, 5, 4, 4, 3]
})

DEFAULT_WEIGHTS = {
    "Engagement Rate": 0.25,
    "Kesesuaian Audiens": 0.25,
    "Biaya Kerja Sama": 0.20,
    "Kualitas Konten": 0.15,
    "Brand Safety": 0.15
}

if "data" not in st.session_state:
    st.session_state.data = DEFAULT_DATA.copy()

if "weights" not in st.session_state:
    st.session_state.weights = DEFAULT_WEIGHTS.copy()

# ==========================================
# FUNGSI PERHITUNGAN SAW
# ==========================================

def calculate_saw(data, weights):
    criteria = list(weights.keys())
    matrix = data[criteria].astype(float)

    normalized = pd.DataFrame(index=data.index)

    for col in criteria:
        if col == "Biaya Kerja Sama":  # Kriteria Cost
            minimum = matrix[col].min()
            normalized[col] = minimum / matrix[col]
        else:  # Kriteria Benefit
            maximum = matrix[col].max()
            normalized[col] = (
                matrix[col] / maximum
                if maximum != 0 else 0
            )

    scores = sum(
        normalized[col] * weights[col]
        for col in criteria
    )

    result = data[["Alternatif"]].copy()
    result["Nilai Preferensi"] = scores

    result = result.sort_values(
        "Nilai Preferensi",
        ascending=False
    ).reset_index(drop=True)

    result.insert(
        0,
        "Peringkat",
        range(1, len(result) + 1)
    )

    # Tambahkan visual status rekomendasi
    def assign_status(rank):
        if rank == 1:
            return "🥇 Sangat Direkomendasikan (Utama)"
        elif rank == 2:
            return "🥈 Alternatif Cadangan 1"
        elif rank == 3:
            return "🥉 Alternatif Cadangan 2"
        else:
            return "Pertimbangan Lanjutan"

    result["Status"] = result["Peringkat"].apply(assign_status)

    return normalized, result


# ==========================================
# SIDEBAR MODERN & AESTHETIC
# ==========================================

with st.sidebar:
    st.markdown("""
        <div class="sidebar-brand-card">
            <div class="sidebar-brand-title">
                <span>🎯</span>
                <span>SPK INFLUENCER</span>
            </div>
            <div class="sidebar-brand-sub">Decision Support System Campaign</div>
            <div class="sidebar-tag">Metode SAW • v2.0</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<p style='font-size: 11px; font-weight: 700; color: #93c5fd; letter-spacing: 0.08em; text-transform: uppercase; margin-bottom: 8px;'>Navigasi Menu</p>", unsafe_allow_html=True)

    menu = st.radio(
        "Navigasi",
        [
            "📊 Dashboard Utama",
            "👥 Data Alternatif",
            "⚖️ Kriteria & Bobot",
            "🧮 Perhitungan SAW",
            "🏆 Hasil Perangkingan"
        ],
        label_visibility="collapsed"
    )

    st.divider()

    # Hitung data saat ini untuk ringkasan di sidebar
    data = st.session_state.data
    weights = st.session_state.weights
    normalized, ranking = calculate_saw(data, weights)
    top_creator = ranking.iloc[0]

    st.markdown(f"""
        <div class="sidebar-info-box">
            <p style="font-weight: 700; color: #ffffff !important; font-size: 12.5px !important; margin-bottom: 6px !important;">
                🏆 Rekomendasi Teratas
            </p>
            <p style="color: #93c5fd !important; font-size: 13.5px !important; font-weight: 600 !important;">
                {top_creator['Alternatif']}
            </p>
            <p style="color: #cbd5e1 !important; font-size: 11.5px !important; margin-top: 4px !important;">
                Skor Preferensi: <b style="color: #ffffff;">{top_creator['Nilai Preferensi']:.4f}</b>
            </p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div style="margin-top: 24px; padding: 10px; text-align: center;">
            <p style="font-size: 11px; color: #94a3b8; margin: 0;">Pengembang: <b>Nafi Fathurohim</b></p>
            <p style="font-size: 10.5px; color: #64748b; margin-top: 2px;">SPK Seleksi Influencer Brand</p>
        </div>
    """, unsafe_allow_html=True)


# ==========================================
# 1. DASHBOARD UTAMA
# ==========================================

if "Dashboard Utama" in menu:

    st.markdown("""
        <div class="header-badge">🚀 Overview Dashboard</div>
        <div class="main-title">Dashboard Seleksi Influencer</div>
        <div class="sub-title">
            Sistem Pendukung Keputusan untuk seleksi mitra Content Creator & Influencer Campaign Brand menggunakan metode Simple Additive Weighting (SAW).
        </div>
    """, unsafe_allow_html=True)

    # METRIC CARDS
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("👥 Total Influencer", f"{len(data)} Mitra")
    with col2:
        st.metric("📋 Kriteria Penilaian", f"{len(weights)} Kriteria")
    with col3:
        st.metric("🏆 Rekomendasi #1", ranking.iloc[0]["Alternatif"])
    with col4:
        st.metric("📈 Skor Tertinggi", f"{ranking.iloc[0]['Nilai Preferensi']:.4f}")

    st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)

    col_left, col_right = st.columns([1.4, 1.0])

    with col_left:
        st.markdown("### 📊 Peringkat Rekomendasi Influencer")
        st.caption("Daftar alternatif diurutkan dari nilai preferensi tertinggi ke terendah.")

        # Format dataframe dengan styling selaras dan elegan
        display_ranking = ranking[["Peringkat", "Alternatif", "Nilai Preferensi", "Status"]].copy()
        
        st.dataframe(
            display_ranking.style.format({
                "Nilai Preferensi": "{:.4f}"
            }),
            use_container_width=True,
            hide_index=True,
            column_config={
                "Peringkat": st.column_config.NumberColumn("Rank", width="small"),
                "Alternatif": st.column_config.TextColumn("Nama Influencer", width="medium"),
                "Nilai Preferensi": st.column_config.NumberColumn("Skor Preferensi (V)", format="%.4f"),
                "Status": st.column_config.TextColumn("Status Rekomendasi", width="large")
            }
        )

    with col_right:
        winner = ranking.iloc[0]
        # Cari data detail pemenang
        winner_details = data[data["Alternatif"] == winner["Alternatif"]].iloc[0]

        st.markdown(f"""
            <div class="winner-card">
                <div class="winner-badge">✨ REKOMENDASI UTAMA</div>
                <div class="winner-name">
                    <span>🏆</span>
                    <span>{winner['Alternatif']}</span>
                </div>
                <p style="color: #dbeafe; font-size: 13px; margin: 0 0 16px 0;">
                    Influencer paling optimal berdasarkan keseimbangan performa engagement, kualitas konten, dan efisiensi biaya.
                </p>
                <div class="winner-score-box">
                    <div>
                        <div class="winner-score-lbl">SKOR PREFERENSI (V)</div>
                        <div class="winner-score-val">{winner['Nilai Preferensi']:.4f}</div>
                    </div>
                    <div style="text-align: right;">
                        <div class="winner-score-lbl">PERINGKAT</div>
                        <div style="font-size: 20px; font-weight: 800; color: #fef08a;">Peringkat 1</div>
                    </div>
                </div>
                <div style="margin-top: 16px; padding-top: 14px; border-top: 1px solid rgba(255,255,255,0.2); font-size: 12.5px; display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
                    <div>Engagement: <b>{winner_details['Engagement Rate']}%</b></div>
                    <div>Audiens: <b>{winner_details['Kesesuaian Audiens']}%</b></div>
                    <div>Biaya: <b>Rp {winner_details['Biaya Kerja Sama']:,}</b></div>
                    <div>Safety: <b>{winner_details['Brand Safety']}/5 ⭐</b></div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

    # SECTION GRAFIK BOBOT & RINGKASAN
    st.divider()
    col_chart1, col_chart2 = st.columns([1.2, 1])

    with col_chart1:
        st.markdown("### 🍩 Komposisi Bobot Kriteria SAW")
        st.caption("Distribusi persentase bobot masing-masing kriteria dalam proses penilaian.")

        weight_chart = pd.DataFrame({
            "Kriteria": list(weights.keys()),
            "Bobot": list(weights.values())
        })

        fig = px.pie(
            weight_chart,
            names="Kriteria",
            values="Bobot",
            hole=0.55,
            color_discrete_sequence=['#1e40af', '#2563eb', '#3b82f6', '#60a5fa', '#93c5fd']
        )

        fig.update_traces(
            textposition='inside',
            textinfo='percent+label',
            marker=dict(line=dict(color='#ffffff', width=2)),
            hovertemplate="<b>%{label}</b><br>Bobot: %{value:.0%}<extra></extra>"
        )

        fig.update_layout(
            showlegend=False,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(family="Plus Jakarta Sans, sans-serif", size=12, color="#1e293b"),
            margin=dict(t=10, b=10, l=10, r=10),
            height=320,
            annotations=[dict(
                text='<b>Bobot</b><br>100%',
                x=0.5, y=0.5,
                font_size=15,
                font_family="Plus Jakarta Sans, sans-serif",
                font_color="#1e3a8a",
                showarrow=False
            )]
        )

        st.plotly_chart(fig, use_container_width=True)

    with col_chart2:
        st.markdown("### 💡 Informasi Kriteria Seleksi")
        st.markdown("""
            <div class="info-card">
                <div class="info-card-header">
                    <span>📌</span> Aturan & Karakteristik Metode SAW
                </div>
                <div class="info-card-body">
                    Metode <b>Simple Additive Weighting</b> menjumlahkan bobot ternormalisasi pada setiap alternatif:
                    <ul style="margin: 8px 0 0 -15px;">
                        <li><b>Kriteria Benefit (4)</b>: Engagement Rate, Kesesuaian Audiens, Kualitas Konten, Brand Safety. Nilai lebih tinggi lebih disukai.</li>
                        <li style="margin-top: 4px;"><b>Kriteria Cost (1)</b>: Biaya Kerja Sama. Nilai lebih murah lebih disukai untuk efisiensi anggaran brand.</li>
                        <li style="margin-top: 4px;">Total seluruh bobot kriteria harus tepat <b>100%</b>.</li>
                    </ul>
                </div>
            </div>
        """, unsafe_allow_html=True)


# ==========================================
# 2. DATA ALTERNATIF
# ==========================================

elif "Data Alternatif" in menu:

    st.markdown("""
        <div class="header-badge">📋 Kelola Data</div>
        <div class="main-title">Data Alternatif Influencer</div>
        <div class="sub-title">
            Kelola, tambah, atau ubah nilai calon mitra influencer yang akan dievaluasi dalam proses seleksi campaign brand.
        </div>
    """, unsafe_allow_html=True)

    # STATS RINGKAS DATA
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Jumlah Mitra", len(data))
    with c2:
        st.metric("Rata-rata ER", f"{data['Engagement Rate'].mean():.2f}%")
    with c3:
        st.metric("Rata-rata Audiens", f"{data['Kesesuaian Audiens'].mean():.1f}%")
    with c4:
        st.metric("Rentang Biaya", f"Rp {data['Biaya Kerja Sama'].min():,} - Rp {data['Biaya Kerja Sama'].max():,}")

    st.markdown("<div style='height: 14px;'></div>", unsafe_allow_html=True)

    st.info("💡 **Tips Interaktif**: Anda dapat langsung mengklik sel tabel di bawah untuk mengedit angka atau menambah baris baru.")

    edited_data = st.data_editor(
        data,
        use_container_width=True,
        num_rows="dynamic",
        hide_index=True,
        column_config={
            "Alternatif": st.column_config.TextColumn(
                "Nama Influencer",
                required=True,
                help="Nama akun atau nama mitra creator"
            ),
            "Engagement Rate": st.column_config.NumberColumn(
                "Engagement Rate (%)",
                min_value=0.0,
                max_value=100.0,
                step=0.1,
                format="%.2f %%",
                help="Tingkat interaksi audiens dalam persen"
            ),
            "Kesesuaian Audiens": st.column_config.NumberColumn(
                "Kesesuaian Audiens (%)",
                min_value=0,
                max_value=100,
                step=1,
                format="%d %%",
                help="Persentase kesesuaian demografi audiens dengan target market brand"
            ),
            "Biaya Kerja Sama": st.column_config.NumberColumn(
                "Biaya Kerja Sama (Rp)",
                min_value=1,
                format="Rp %,d",
                help="Biaya rate card kerja sama per campaign"
            ),
            "Kualitas Konten": st.column_config.NumberColumn(
                "Kualitas Konten (1–5)",
                min_value=1,
                max_value=5,
                step=1,
                format="%d ⭐",
                help="Skala estetika, visual, dan penyampaian pesan konten (1–5)"
            ),
            "Brand Safety": st.column_config.NumberColumn(
                "Brand Safety (1–5)",
                min_value=1,
                max_value=5,
                step=1,
                format="%d 🛡️",
                help="Skala rekam jejak, kredibilitas, dan keamanan reputasi brand (1–5)"
            )
        },
        key="editor_data"
    )

    st.caption("ℹ️ *Catatan: Nilai Kualitas Konten dan Brand Safety menggunakan skala bulat 1 hingga 5.*")

    col_btn1, col_btn2, _ = st.columns([1.2, 1.2, 3])

    with col_btn1:
        save_pressed = st.button("💾 Simpan Data Alternatif", type="primary", use_container_width=True)
    with col_btn2:
        reset_pressed = st.button("🔄 Reset ke Data Awal", use_container_width=True)

    if reset_pressed:
        st.session_state.data = DEFAULT_DATA.copy()
        st.success("Data berhasil dikembalikan ke nilai default.")
        st.rerun()

    if save_pressed:
        numeric_columns = [
            "Engagement Rate",
            "Kesesuaian Audiens",
            "Biaya Kerja Sama",
            "Kualitas Konten",
            "Brand Safety"
        ]

        valid = True

        if edited_data.empty:
            st.error("Data alternatif tidak boleh kosong.")
            valid = False
        elif edited_data["Alternatif"].astype(str).str.strip().eq("").any():
            st.error("Nama influencer tidak boleh kosong.")
            valid = False
        elif edited_data["Alternatif"].astype(str).str.strip().duplicated().any():
            st.error("Nama influencer tidak boleh ada yang kembar/duplikat.")
            valid = False
        elif edited_data[numeric_columns].isnull().any().any():
            st.error("Semua kolom kriteria harus diisi secara lengkap.")
            valid = False
        elif (edited_data[numeric_columns] < 0).any().any():
            st.error("Nilai kriteria tidak boleh bernilai negatif.")
            valid = False
        elif (edited_data["Biaya Kerja Sama"] <= 0).any():
            st.error("Biaya kerja sama harus lebih dari Rp 0.")
            valid = False
        elif (edited_data["Kesesuaian Audiens"] > 100).any():
            st.error("Kesesuaian audiens maksimal 100%.")
            valid = False
        elif not edited_data[["Kualitas Konten", "Brand Safety"]].isin([1, 2, 3, 4, 5]).all().all():
            st.error("Kualitas Konten dan Brand Safety harus bernilai bilangan bulat 1 sampai 5.")
            valid = False

        if valid:
            st.session_state.data = edited_data.reset_index(drop=True)
            st.success("✅ Perubahan data alternatif berhasil disimpan!")
            st.rerun()


# ==========================================
# 3. KRITERIA DAN BOBOT
# ==========================================

elif "Kriteria & Bobot" in menu:

    st.markdown("""
        <div class="header-badge">⚖️ Pengaturan Kriteria</div>
        <div class="main-title">Kriteria dan Bobot Penilaian</div>
        <div class="sub-title">
            Konfigurasikan tingkat kepentingan (prioritas) masing-masing kriteria. Total seluruh bobot harus tepat 100% (1.00).
        </div>
    """, unsafe_allow_html=True)

    criteria_table = pd.DataFrame({
        "Kode": ["C1", "C2", "C3", "C4", "C5"],
        "Nama Kriteria": list(weights.keys()),
        "Tipe / Sifat": [
            "Benefit (Keuntungan)",
            "Benefit (Keuntungan)",
            "Cost (Biaya)",
            "Benefit (Keuntungan)",
            "Benefit (Keuntungan)"
        ],
        "Bobot Saat Ini": [
            f"{val * 100:.0f}%" for val in weights.values()
        ],
        "Keterangan": [
            "Semakin tinggi persentase engagement, semakin potensial interaksi audiens.",
            "Semakin sesuai demografi audiens dengan brand, semakin tepat sasaran.",
            "Semakin hemat biaya kerja sama, semakin efisien anggaran campaign brand.",
            "Kualitas produksi konten, estetika visual, dan kreativitas penyampaian.",
            "Rekam jejak, kredibilitas, dan keamanan reputasi influencer dari isu negatif."
        ]
    })

    st.dataframe(
        criteria_table,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Kode": st.column_config.TextColumn("Kode", width="small"),
            "Nama Kriteria": st.column_config.TextColumn("Kriteria", width="medium"),
            "Tipe / Sifat": st.column_config.TextColumn("Tipe", width="medium"),
            "Bobot Saat Ini": st.column_config.TextColumn("Bobot", width="small"),
            "Keterangan": st.column_config.TextColumn("Deskripsi Kriteria", width="large")
        }
    )

    st.divider()

    st.markdown("### 🎚️ Atur Bobot Kepentingan")
    st.caption("Ubah nilai bobot untuk setiap kriteria. Perubahan akan langsung mempengaruhi hasil pemeringkatan.")

    col1, col2 = st.columns(2)
    new_weights = {}

    for index, (criterion, value) in enumerate(weights.items()):
        target_col = col1 if index % 2 == 0 else col2
        with target_col:
            new_weights[criterion] = st.number_input(
                f"{criterion} ({'Cost' if criterion == 'Biaya Kerja Sama' else 'Benefit'})",
                min_value=0.0,
                max_value=1.0,
                value=float(value),
                step=0.05,
                format="%.2f",
                key=f"weight_input_{index}",
                help=f"Nilai desimal (contoh: 0.25 = 25%)"
            )

    total_weight = sum(new_weights.values())

    st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

    # Indikator Total Bobot
    col_t1, col_t2 = st.columns([1, 2])
    with col_t1:
        st.metric(
            "Total Bobot Terhitung",
            f"{total_weight * 100:.0f}%",
            delta="100% Sesuai" if np.isclose(total_weight, 1.0) else f"Selisih {(1.0 - total_weight)*100:+.0f}%",
            delta_color="normal" if np.isclose(total_weight, 1.0) else "inverse"
        )
    with col_t2:
        if np.isclose(total_weight, 1.0):
            st.success("✅ **Total bobot valid (100%)**. Siap digunakan untuk perhitungan preferensi SAW.")
        else:
            st.warning(f"⚠️ **Total bobot saat ini {total_weight * 100:.0f}%**. Mohon sesuaikan bobot hingga total tepat 100%.")

    col_save1, col_save2, _ = st.columns([1.2, 1.2, 3])
    with col_save1:
        save_w_pressed = st.button("💾 Simpan Bobot Baru", type="primary", use_container_width=True)
    with col_save2:
        reset_w_pressed = st.button("🔄 Reset Bobot Default", use_container_width=True)

    if reset_w_pressed:
        st.session_state.weights = DEFAULT_WEIGHTS.copy()
        st.success("Bobot kriteria dikembalikan ke default.")
        st.rerun()

    if save_w_pressed:
        if not np.isclose(total_weight, 1.0):
            st.error("Gagal menyimpan: Total bobot kriteria harus tepat 100% (1.00).")
        else:
            st.session_state.weights = new_weights
            st.success("✅ Bobot kriteria baru berhasil disimpan!")
            st.rerun()


# ==========================================
# 4. PERHITUNGAN METODE SAW
# ==========================================

elif "Perhitungan SAW" in menu:

    st.markdown("""
        <div class="header-badge">🧮 Langkah Perhitungan</div>
        <div class="main-title">Tahapan Metode Simple Additive Weighting (SAW)</div>
        <div class="sub-title">
            Transparansi proses perhitungan matematis mulai dari pembentukan matriks keputusan, normalisasi nilai benefit/cost, hingga penjumlahan terbobot.
        </div>
    """, unsafe_allow_html=True)

    criteria = list(weights.keys())

    # LANGKAH 1
    with st.expander("1️⃣ Langkah 1: Matriks Keputusan (X)", expanded=True):
        st.markdown("""
            Matriks keputusan $X$ berukuran $m \\times n$ dibentuk dari data nilai asli masing-masing alternatif terhadap seluruh kriteria.
        """)
        raw_display = data[["Alternatif"] + criteria].copy()
        st.dataframe(
            raw_display.style.format({
                "Biaya Kerja Sama": "Rp {:,.0f}",
                "Engagement Rate": "{:.2f}%",
                "Kesesuaian Audiens": "{:.0f}%"
            }),
            use_container_width=True,
            hide_index=True
        )

    # LANGKAH 2
    with st.expander("2️⃣ Langkah 2: Matriks Ternormalisasi (R)", expanded=True):
        st.markdown("""
            Normalisasi dilakukan untuk menyamakan skala seluruh kriteria ke rentang [0, 1] menggunakan aturan:
            - **Kriteria Benefit**: $r_{ij} = \\frac{x_{ij}}{\\max_i(x_{ij})}$ (Semakin besar semakin baik)
            - **Kriteria Cost**: $r_{ij} = \\frac{\\min_i(x_{ij})}{x_{ij}}$ (Semakin kecil semakin baik)
        """)

        normalized_display = normalized.copy()
        normalized_display.insert(0, "Alternatif", data["Alternatif"])

        st.dataframe(
            normalized_display.style.format({
                col: "{:.4f}" for col in criteria
            }),
            use_container_width=True,
            hide_index=True
        )

        st.caption("ℹ️ *Kolom 'Biaya Kerja Sama' dinormalisasi dengan rumus Cost (Min/X), kriteria lainnya dengan rumus Benefit (X/Max).*")

    # LANGKAH 3
    with st.expander("3️⃣ Langkah 3: Vektor Bobot Preferensi (W)", expanded=True):
        st.markdown("""
            Vektor bobot preferensi $W = [w_1, w_2, \\dots, w_n]$ merepresentasikan tingkat kepentingan relatif masing-masing kriteria.
        """)

        weight_display = pd.DataFrame({
            "Kode": [f"C{i+1}" for i in range(len(weights))],
            "Kriteria": list(weights.keys()),
            "Tipe": ["Benefit" if k != "Biaya Kerja Sama" else "Cost" for k in weights.keys()],
            "Bobot Desimal (W)": list(weights.values()),
            "Persentase": [f"{v * 100:.0f}%" for v in weights.values()]
        })

        st.dataframe(
            weight_display.style.format({
                "Bobot Desimal (W)": "{:.2f}"
            }),
            use_container_width=True,
            hide_index=True
        )

    # LANGKAH 4
    with st.expander("4️⃣ Langkah 4: Nilai Preferensi Akhir (V)", expanded=True):
        st.markdown("""
            Nilai preferensi ($V_i$) untuk setiap alternatif diperoleh dari penjumlahan hasil kali matriks ternormalisasi dengan bobot kriteria:
            $$V_i = \\sum_{j=1}^{n} w_j \\cdot r_{ij}$$
        """)

        pref_table = data[["Alternatif"]].copy()
        pref_table["Nilai Preferensi"] = (
            normalized.mul(pd.Series(weights)).sum(axis=1)
        )
        pref_table = pref_table.sort_values("Nilai Preferensi", ascending=False).reset_index(drop=True)
        pref_table.insert(0, "Peringkat", range(1, len(pref_table) + 1))

        st.dataframe(
            pref_table.style.format({
                "Nilai Preferensi": "{:.4f}"
            }),
            use_container_width=True,
            hide_index=True,
            column_config={
                "Peringkat": st.column_config.NumberColumn("Rank", width="small"),
                "Alternatif": st.column_config.TextColumn("Nama Influencer", width="medium"),
                "Nilai Preferensi": st.column_config.NumberColumn("Skor Preferensi (V)", format="%.4f")
            }
        )


# ==========================================
# 5. HASIL PERANGKINGAN
# ==========================================

elif "Hasil Perangkingan" in menu:

    st.markdown("""
        <div class="header-badge">🏆 Rekomendasi Seleksi</div>
        <div class="main-title">Hasil Perangkingan Influencer</div>
        <div class="sub-title">
            Keputusan akhir pemeringkatan calon mitra influencer berdasarkan nilai preferensi tertinggi menggunakan metode Simple Additive Weighting (SAW).
        </div>
    """, unsafe_allow_html=True)

    winner = ranking.iloc[0]
    winner_details = data[data["Alternatif"] == winner["Alternatif"]].iloc[0]

    # HERO WINNER CARD
    st.markdown(f"""
        <div class="winner-card">
            <div class="winner-badge">⭐ REKOMENDASI UTAMA UNTUK CAMPAIGN BRAND</div>
            <div class="winner-name">
                <span>🏆</span>
                <span>{winner['Alternatif']}</span>
            </div>
            <p style="color: #dbeafe; font-size: 14px; margin: 4px 0 16px 0;">
                Menempati peringkat pertama dengan nilai preferensi tertinggi sebesar <b>{winner['Nilai Preferensi']:.4f}</b>.
            </p>
            <div class="winner-score-box">
                <div>
                    <div class="winner-score-lbl">SKOR PREFERENSI TERTINGGI</div>
                    <div class="winner-score-val">{winner['Nilai Preferensi']:.4f}</div>
                </div>
                <div style="text-align: right;">
                    <div class="winner-score-lbl">STATUS REKOMENDASI</div>
                    <div style="font-size: 20px; font-weight: 800; color: #fef08a;">Peringkat #1</div>
                </div>
            </div>
            <div style="margin-top: 16px; padding-top: 14px; border-top: 1px solid rgba(255,255,255,0.2); font-size: 13px; display: grid; grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); gap: 10px;">
                <div>Engagement: <b>{winner_details['Engagement Rate']}%</b></div>
                <div>Audiens: <b>{winner_details['Kesesuaian Audiens']}%</b></div>
                <div>Biaya: <b>Rp {winner_details['Biaya Kerja Sama']:,}</b></div>
                <div>Kualitas: <b>{winner_details['Kualitas Konten']}/5 ⭐</b></div>
                <div>Brand Safety: <b>{winner_details['Brand Safety']}/5 🛡️</b></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)

    # METRICS
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Total Kandidat Dievaluasi", f"{len(ranking)} Influencer")
    with c2:
        st.metric("Skor Tertinggi (#1)", f"{winner['Nilai Preferensi']:.4f}")
    with c3:
        selisih = winner['Nilai Preferensi'] - ranking.iloc[1]['Nilai Preferensi']
        st.metric("Selisih dengan Peringkat 2", f"+{selisih:.4f}")

    st.markdown("<div style='height: 14px;'></div>", unsafe_allow_html=True)

    # TABEL PERANGKINGAN
    st.markdown("### 📋 Tabel Rekomendasi Peringkat Lengkap")

    st.dataframe(
        ranking.style.format({
            "Nilai Preferensi": "{:.4f}"
        }),
        use_container_width=True,
        hide_index=True,
        column_config={
            "Peringkat": st.column_config.NumberColumn("Rank", width="small"),
            "Alternatif": st.column_config.TextColumn("Nama Influencer", width="medium"),
            "Nilai Preferensi": st.column_config.NumberColumn("Nilai Preferensi (V)", format="%.4f"),
            "Status": st.column_config.TextColumn("Status Rekomendasi", width="large")
        }
    )

    # DOWNLOAD REPORT BUTTON
    csv_data = ranking.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Laporan Hasil Perangkingan (CSV)",
        data=csv_data,
        file_name="hasil_perangkingan_influencer_saw.csv",
        mime="text/csv",
    )

    st.divider()

    # GRAFIK PERBANDINGAN NILAI
    st.markdown("### 📊 Visualisasi Perbandingan Nilai Preferensi")
    st.caption("Perbandingan skor preferensi seluruh calon influencer yang dievaluasi.")

    chart = px.bar(
        ranking,
        x="Alternatif",
        y="Nilai Preferensi",
        text="Nilai Preferensi",
        color="Nilai Preferensi",
        color_continuous_scale=[
            [0.0, "#93c5fd"],
            [0.5, "#3b82f6"],
            [1.0, "#1d4ed8"]
        ]
    )

    chart.update_traces(
        texttemplate="%{text:.4f}",
        textposition="outside",
        marker=dict(
            line=dict(width=1, color="#1e40af"),
            cornerradius=8
        )
    )

    chart.update_layout(
        yaxis_title="Nilai Preferensi (V)",
        xaxis_title="Alternatif Influencer",
        showlegend=False,
        coloraxis_showscale=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Plus Jakarta Sans, sans-serif", size=13, color="#1e293b"),
        height=420,
        margin=dict(t=30, b=40, l=40, r=20),
        yaxis=dict(
            gridcolor="#f1f5f9",
            zerolinecolor="#cbd5e1",
            range=[0, max(ranking["Nilai Preferensi"]) * 1.15]
        ),
        xaxis=dict(
            gridcolor="rgba(0,0,0,0)"
        )
    )

    st.plotly_chart(chart, use_container_width=True)


# ==========================================
# FOOTER MODERN
# ==========================================

st.divider()

st.markdown(
    """
    <div style="text-align: center; color: #94a3b8; font-size: 12.5px; padding: 12px 0 20px 0;">
        <span style="font-weight: 600; color: #64748b;">Sistem Pendukung Keputusan Seleksi Influencer</span> 
        • Metode Simple Additive Weighting (SAW)
        <br>
        <span style="font-size: 11.5px; color: #94a3b8;">Desain UI Modern & Minimalis Biru • Dikembangkan oleh Nafi Fathurohim</span>
    </div>
    """,
    unsafe_allow_html=True
)
