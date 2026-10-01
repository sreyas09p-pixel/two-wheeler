# pyrefly: ignore [missing-import]
import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Two Wheeler Management System",
    page_icon="🏍️",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

/* Dark gradient background */
.stApp {
    background: linear-gradient(135deg, #0f0c29 0%, #1a1a2e 40%, #16213e 100%);
    color: #e2e8f0;
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #1a1a3e 0%, #0f0c29 100%);
    border-right: 1px solid rgba(99, 102, 241, 0.3);
}
[data-testid="stSidebar"] * { color: #e2e8f0 !important; }

/* Hero banner */
.hero-banner {
    background: linear-gradient(135deg, rgba(99,102,241,0.25) 0%, rgba(168,85,247,0.2) 50%, rgba(236,72,153,0.15) 100%);
    border: 1px solid rgba(99,102,241,0.4);
    border-radius: 20px;
    padding: 32px 28px 24px 28px;
    text-align: center;
    margin-bottom: 28px;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 32px rgba(99,102,241,0.2);
}
.hero-title {
    font-size: 2.4rem;
    font-weight: 800;
    background: linear-gradient(90deg, #818cf8, #c084fc, #f472b6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0 0 6px 0;
    line-height: 1.2;
}
.hero-sub {
    font-size: 0.95rem;
    color: #94a3b8;
    margin: 0;
    font-weight: 400;
}

/* Result cards */
.result-card {
    background: linear-gradient(135deg, rgba(30,27,75,0.9) 0%, rgba(15,12,41,0.9) 100%);
    border: 1px solid rgba(99,102,241,0.35);
    border-radius: 16px;
    padding: 22px 26px;
    margin-top: 18px;
    box-shadow: 0 4px 24px rgba(99,102,241,0.15);
    backdrop-filter: blur(8px);
}
.result-title {
    font-size: 1.05rem;
    font-weight: 600;
    color: #818cf8;
    margin-bottom: 14px;
    letter-spacing: 0.5px;
}
.metric-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 0;
    border-bottom: 1px solid rgba(99,102,241,0.12);
}
.metric-row:last-child { border-bottom: none; }
.metric-label { color: #94a3b8; font-size: 0.9rem; font-weight: 400; }
.metric-value { color: #e2e8f0; font-size: 1.05rem; font-weight: 600; }

/* Status badges */
.badge {
    display: inline-block;
    padding: 6px 16px;
    border-radius: 999px;
    font-size: 0.85rem;
    font-weight: 700;
    letter-spacing: 0.5px;
    margin-top: 10px;
}
.badge-excellent { background: rgba(16,185,129,0.2); color: #34d399; border: 1px solid rgba(16,185,129,0.4); }
.badge-good      { background: rgba(59,130,246,0.2); color: #60a5fa; border: 1px solid rgba(59,130,246,0.4); }
.badge-low       { background: rgba(245,158,11,0.2); color: #fbbf24; border: 1px solid rgba(245,158,11,0.4); }
.badge-danger    { background: rgba(239,68,68,0.2);  color: #f87171; border: 1px solid rgba(239,68,68,0.4); }
.badge-warning   { background: rgba(245,158,11,0.2); color: #fbbf24; border: 1px solid rgba(245,158,11,0.4); }
.badge-safe      { background: rgba(16,185,129,0.2); color: #34d399; border: 1px solid rgba(16,185,129,0.4); }
.badge-due       { background: rgba(239,68,68,0.2);  color: #f87171; border: 1px solid rgba(239,68,68,0.4); }
.badge-ok        { background: rgba(16,185,129,0.2); color: #34d399; border: 1px solid rgba(16,185,129,0.4); }

/* Streamlit widget overrides */
.stNumberInput label, .stTextInput label, .stSelectbox label {
    color: #94a3b8 !important;
    font-size: 0.88rem !important;
    font-weight: 500 !important;
}
div[data-testid="stNumberInput"] input {
    background: rgba(30,27,75,0.7) !important;
    border: 1px solid rgba(99,102,241,0.4) !important;
    border-radius: 10px !important;
    color: #e2e8f0 !important;
    font-size: 1rem !important;
}
div[data-testid="stNumberInput"] input:focus {
    border-color: #818cf8 !important;
    box-shadow: 0 0 0 2px rgba(129,140,248,0.25) !important;
}

/* Primary button */
.stButton > button {
    background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    padding: 12px 36px !important;
    font-size: 0.95rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.5px !important;
    width: 100% !important;
    transition: all 0.3s ease !important;
    box-shadow: 0 4px 15px rgba(99,102,241,0.35) !important;
    margin-top: 8px !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #4f46e5, #7c3aed) !important;
    box-shadow: 0 6px 20px rgba(99,102,241,0.5) !important;
    transform: translateY(-1px) !important;
}

/* Sidebar nav buttons */
.sidebar-nav-btn {
    background: rgba(99,102,241,0.1);
    border: 1px solid rgba(99,102,241,0.25);
    border-radius: 12px;
    padding: 12px 16px;
    margin-bottom: 8px;
    cursor: pointer;
    width: 100%;
    text-align: left;
    color: #e2e8f0;
    font-size: 0.92rem;
    font-weight: 500;
    transition: all 0.2s ease;
}

/* Section header */
.section-header {
    font-size: 1.5rem;
    font-weight: 700;
    color: #c084fc;
    margin-bottom: 4px;
}
.section-desc {
    color: #64748b;
    font-size: 0.9rem;
    margin-bottom: 24px;
}

/* Divider */
hr { border-color: rgba(99,102,241,0.2) !important; }

/* Hide default Streamlit elements */
#MainMenu, footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

# ── Hero Banner ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero-banner">
    <p class="hero-title">🏍️ Two Wheeler Management System</p>
    <p class="hero-sub">Smart tools for every rider — mileage, fuel, trips, service & safety</p>
</div>
""", unsafe_allow_html=True)

# ── Sidebar Navigation ────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🧭 Navigation")
    st.markdown("---")
    menu = {
        "⛽ Mileage Calculator":    "mileage",
        "💰 Fuel Cost Calculator":  "fuel_cost",
        "🗺️ Trip Cost Calculator":  "trip_cost",
        "🔧 Service Reminder":      "service",
        "🚨 Speed Warning System":  "speed",
    }
    if "page" not in st.session_state:
        st.session_state.page = "mileage"

    for label, key in menu.items():
        active_style = "border-color: rgba(129,140,248,0.7); background: rgba(99,102,241,0.2);" if st.session_state.page == key else ""
        if st.button(label, key=f"nav_{key}"):
            st.session_state.page = key

    st.markdown("---")
    st.markdown("<small style='color:#475569;'>© 2025 Two Wheeler MS</small>", unsafe_allow_html=True)

page = st.session_state.page

# ══════════════════════════════════════════════════════════════════════════════
# 1. MILEAGE CALCULATOR
# ══════════════════════════════════════════════════════════════════════════════
if page == "mileage":
    st.markdown('<p class="section-header">⛽ Mileage Calculator</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-desc">Find out how efficiently your two-wheeler is running.</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        distance = st.number_input("Distance Travelled (km)", min_value=0.0, value=0.0, step=1.0, format="%.2f")
    with col2:
        fuel = st.number_input("Fuel Consumed (liters)", min_value=0.0, value=0.0, step=0.1, format="%.2f")

    if st.button("📊 Calculate Mileage"):
        if fuel > 0:
            mileage = distance / fuel
            if mileage >= 50:
                status_badge = '<span class="badge badge-excellent">✅ Excellent Mileage</span>'
                status_text = "Your bike is running exceptionally well!"
            elif mileage >= 35:
                status_badge = '<span class="badge badge-good">👍 Good Mileage</span>'
                status_text = "Your bike is performing well."
            else:
                status_badge = '<span class="badge badge-low">⚠️ Low Mileage</span>'
                status_text = "Consider servicing your bike for better performance."

            st.markdown(f"""
            <div class="result-card">
                <div class="result-title">📈 Results</div>
                <div class="metric-row">
                    <span class="metric-label">Distance Travelled</span>
                    <span class="metric-value">{distance:.2f} km</span>
                </div>
                <div class="metric-row">
                    <span class="metric-label">Fuel Consumed</span>
                    <span class="metric-value">{fuel:.2f} L</span>
                </div>
                <div class="metric-row">
                    <span class="metric-label">Mileage</span>
                    <span class="metric-value">{mileage:.2f} km/L</span>
                </div>
                <div style="margin-top:14px;">
                    {status_badge}
                    <p style="color:#64748b; font-size:0.85rem; margin-top:8px;">{status_text}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.error("Fuel consumed cannot be zero.")

# ══════════════════════════════════════════════════════════════════════════════
# 2. FUEL COST CALCULATOR
# ══════════════════════════════════════════════════════════════════════════════
elif page == "fuel_cost":
    st.markdown('<p class="section-header">💰 Fuel Cost Calculator</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-desc">Know exactly how much you\'ll spend on fuel for any journey.</p>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        distance = st.number_input("Distance (km)", min_value=0.0, value=0.0, step=1.0, format="%.2f")
    with col2:
        mileage = st.number_input("Mileage (km/L)", min_value=0.0, value=0.0, step=0.5, format="%.2f")
    with col3:
        fuel_price = st.number_input("Fuel Price (₹/L)", min_value=0.0, value=0.0, step=0.5, format="%.2f")

    if st.button("💸 Calculate Fuel Cost"):
        fuel_needed = distance / mileage
        fuel_cost = fuel_needed * fuel_price

        st.markdown(f"""
        <div class="result-card">
            <div class="result-title">💸 Cost Breakdown</div>
            <div class="metric-row">
                <span class="metric-label">Distance</span>
                <span class="metric-value">{distance:.2f} km</span>
            </div>
            <div class="metric-row">
                <span class="metric-label">Vehicle Mileage</span>
                <span class="metric-value">{mileage:.2f} km/L</span>
            </div>
            <div class="metric-row">
                <span class="metric-label">Fuel Price</span>
                <span class="metric-value">₹ {fuel_price:.2f} / L</span>
            </div>
            <div class="metric-row">
                <span class="metric-label">Fuel Needed</span>
                <span class="metric-value">{fuel_needed:.3f} L</span>
            </div>
            <div class="metric-row">
                <span class="metric-label" style="font-weight:600; color:#c084fc;">Total Fuel Cost</span>
                <span class="metric-value" style="font-size:1.3rem; color:#818cf8;">₹ {fuel_cost:.2f}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# 3. TRIP COST CALCULATOR
# ══════════════════════════════════════════════════════════════════════════════
elif page == "trip_cost":
    st.markdown('<p class="section-header">🗺️ Trip Cost Calculator</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-desc">Plan your trip budget before you hit the road.</p>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        distance = st.number_input("Trip Distance (km)", min_value=0.0, value=0.0, step=5.0, format="%.2f")
    with col2:
        mileage = st.number_input("Vehicle Mileage (km/L)", min_value=0.0, value=0.0, step=0.5, format="%.2f")
    with col3:
        fuel_price = st.number_input("Fuel Price (₹/L)", min_value=0.0, value=0.0, step=0.5, format="%.2f")

    if st.button("🧮 Calculate Trip Cost"):
        fuel = distance / mileage
        cost = fuel * fuel_price
        cost_per_km = cost / distance if distance > 0 else 0

        st.markdown(f"""
        <div class="result-card">
            <div class="result-title">🗺️ Trip Summary</div>
            <div class="metric-row">
                <span class="metric-label">Total Distance</span>
                <span class="metric-value">{distance:.2f} km</span>
            </div>
            <div class="metric-row">
                <span class="metric-label">Fuel Required</span>
                <span class="metric-value">{fuel:.3f} L</span>
            </div>
            <div class="metric-row">
                <span class="metric-label">Fuel Price</span>
                <span class="metric-value">₹ {fuel_price:.2f} / L</span>
            </div>
            <div class="metric-row">
                <span class="metric-label">Cost per km</span>
                <span class="metric-value">₹ {cost_per_km:.2f}</span>
            </div>
            <div class="metric-row">
                <span class="metric-label" style="font-weight:600; color:#c084fc;">💰 Total Trip Cost</span>
                <span class="metric-value" style="font-size:1.3rem; color:#818cf8;">₹ {cost:.2f}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Round-trip estimate
        st.markdown(f"""
        <div class="result-card" style="border-color:rgba(168,85,247,0.35); margin-top:12px;">
            <div class="result-title" style="color:#c084fc;">🔄 Round Trip Estimate</div>
            <div class="metric-row">
                <span class="metric-label">Total Distance (Round)</span>
                <span class="metric-value">{distance * 2:.2f} km</span>
            </div>
            <div class="metric-row">
                <span class="metric-label">Fuel Required (Round)</span>
                <span class="metric-value">{fuel * 2:.3f} L</span>
            </div>
            <div class="metric-row">
                <span class="metric-label" style="font-weight:600; color:#c084fc;">💰 Round Trip Cost</span>
                <span class="metric-value" style="font-size:1.3rem; color:#818cf8;">₹ {cost * 2:.2f}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════════════
# 4. SERVICE REMINDER
# ══════════════════════════════════════════════════════════════════════════════
elif page == "service":
    st.markdown('<p class="section-header">🔧 Service Reminder</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-desc">Stay on top of your bike\'s maintenance schedule (every 3000 km).</p>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        current = st.number_input("Current Odometer Reading (km)", min_value=0, value=0, step=100)
    with col2:
        last = st.number_input("Last Service Reading (km)", min_value=0, value=0, step=100)

    if st.button("🔍 Check Service Status"):
        next_service = last + 3000
        km_since_service = current - last

        if current >= next_service:
            overdue = current - next_service
            badge = '<span class="badge badge-due">🔴 Service Due!</span>'
            msg = f"Your bike is <strong>{overdue} km overdue</strong> for service. Please visit a service center immediately."
            progress_color = "#ef4444"
            progress_val = 100
        else:
            remaining = next_service - current
            pct = int((km_since_service / 3000) * 100)
            badge = '<span class="badge badge-ok">✅ Service Not Due</span>'
            msg = f"Your next service is due in <strong>{remaining} km</strong> (at {next_service:,} km)."
            progress_color = "#6366f1"
            progress_val = min(pct, 100)

        st.markdown(f"""
        <div class="result-card">
            <div class="result-title">🔧 Service Status</div>
            <div class="metric-row">
                <span class="metric-label">Current Odometer</span>
                <span class="metric-value">{current:,} km</span>
            </div>
            <div class="metric-row">
                <span class="metric-label">Last Service At</span>
                <span class="metric-value">{last:,} km</span>
            </div>
            <div class="metric-row">
                <span class="metric-label">km Since Last Service</span>
                <span class="metric-value">{km_since_service:,} km</span>
            </div>
            <div class="metric-row">
                <span class="metric-label">Next Service At</span>
                <span class="metric-value">{next_service:,} km</span>
            </div>
            <div style="margin-top:14px;">
                {badge}
                <p style="color:#94a3b8; font-size:0.88rem; margin-top:10px;">{msg}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Progress bar (via Streamlit native)
        st.markdown("<p style='color:#64748b; font-size:0.85rem; margin-top:16px; margin-bottom:4px;'>Service Interval Progress (3000 km cycle)</p>", unsafe_allow_html=True)
        st.progress(progress_val / 100)

# ══════════════════════════════════════════════════════════════════════════════
# 5. SPEED WARNING SYSTEM
# ══════════════════════════════════════════════════════════════════════════════
elif page == "speed":
    st.markdown('<p class="section-header">🚨 Speed Warning System</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-desc">Check if your riding speed is within safe limits.</p>', unsafe_allow_html=True)

    speed = st.number_input("Vehicle Speed (km/h)", min_value=0.0, value=0.0, step=1.0, format="%.1f")

    if st.button("⚡ Check Speed"):
        if speed <= 60:
            badge = '<span class="badge badge-safe">✅ Safe Speed</span>'
            icon = "🟢"
            msg = "You are riding within the safe speed limit. Keep it up!"
            tip = "Maintain safe speeds to save fuel and protect yourself."
            color = "#10b981"
        elif speed <= 80:
            badge = '<span class="badge badge-warning">⚠️ Warning: High Speed</span>'
            icon = "🟡"
            msg = "You are exceeding the recommended speed limit."
            tip = "Slow down to 60 km/h for safer riding and better mileage."
            color = "#f59e0b"
        else:
            badge = '<span class="badge badge-danger">🚨 Danger: Overspeed!</span>'
            icon = "🔴"
            msg = "CRITICAL! You are riding at a dangerously high speed!"
            tip = "Reduce speed immediately. Overspeed is a leading cause of accidents."
            color = "#ef4444"

        st.markdown(f"""
        <div class="result-card" style="border-color:{color}44;">
            <div class="result-title">⚡ Speed Analysis</div>
            <div class="metric-row">
                <span class="metric-label">Current Speed</span>
                <span class="metric-value" style="font-size:1.4rem; color:{color};">{speed:.1f} km/h</span>
            </div>
            <div class="metric-row">
                <span class="metric-label">Safe Limit</span>
                <span class="metric-value">≤ 60 km/h</span>
            </div>
            <div class="metric-row">
                <span class="metric-label">Warning Zone</span>
                <span class="metric-value">61 – 80 km/h</span>
            </div>
            <div class="metric-row">
                <span class="metric-label">Danger Zone</span>
                <span class="metric-value">> 80 km/h</span>
            </div>
            <div style="margin-top:14px;">
                {badge}
                <p style="color:#94a3b8; font-size:0.88rem; margin-top:10px;">{msg}</p>
                <p style="color:#64748b; font-size:0.83rem; margin-top:4px;">💡 {tip}</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Speed gauge bar
        st.markdown("<p style='color:#64748b; font-size:0.85rem; margin-top:16px; margin-bottom:4px;'>Speed Gauge (max 120 km/h reference)</p>", unsafe_allow_html=True)
        st.progress(min(speed / 120, 1.0))
