import streamlit as st
import pandas as pd
import plotly.express as px

# Centralizing 40 High-Density IoT Hardware Monitored Assets
if "generator_fleet_db" not in st.session_state:
    st.session_state.generator_fleet_db = pd.DataFrame({
        "asset_id": [f"OMNI-{300+i}" for i in range(1, 41)],
        "client_account": ["Bunch LLC" if i % 4 == 0 else f"Enterprise Client {i}" for i in range(40)],
        "generator_brand": ["Generac", "Kohler", "Cummins", "Caterpillar", "MTU"] * 8,
        "transmission_type": ["LTE Cellular", "Iridium Satellite", "LAN/Ethernet", "LTE Cellular"] * 10,
        "battery_voltage": [13.4 - (i % 3) * 0.4 for i in range(40)],
        "fuel_level_pct": [85 - (i * 2) % 45 for i in range(40)],
        "telemetry_sync_status": ["Good Standing - Regular Sync" if i % 5 != 0 else "Alarms Pending - Charger Failure" for i in range(40)]
    })

# Centralizing 20 Detailed Field Service Staff Tech Profiles
if "field_tech_db" not in st.session_state:
    st.session_state.field_tech_db = pd.DataFrame({
        "tech_id": [f"TECH-{100+i}" for i in range(1, 21)],
        "tech_name": [f"Technician Specialist {i}" for i in range(20)],
        "assigned_region": ["North East", "South East", "Mid West", "West Coast"] * 5,
        "cert_level": ["Master Senior Engineer", "Tenured Field Tech", "Associate Apprentice"] * 6 + ["Master Senior Engineer", "Tenured Field Tech"],
        "active_tickets_load": [3, 5, 2, 6, 1, 4, 3, 5, 2, 4] * 2,
        "retention_risk_tier": ["Low Risk" if i % 6 != 0 else "High Risk - Workload Burnout" for i in range(20)]
    })
