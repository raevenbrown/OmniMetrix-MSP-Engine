import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Main Page Canvas Configuration
st.set_page_config(page_title="OmniMetrix Enterprise BI Engine", layout="wide")

# 2. Ingest Managed IT & Cyber Dataset mapped directly to service tiers
tenant_data = {
    "ticket_id": [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    "client_name": ["Apex Logistics", "Summit Health Network", "Apex Logistics", "Vanguard Finance", "Summit Health Network", "Vanguard Finance", "Apex Logistics", "Vanguard Finance", "Summit Health Network", "Horizon Retail"],
    "service_sector": ["Patching & Security", "Dark Web & Compliance", "Help Desk Support", "Threat Detection", "Cybersecurity Team", "Help Desk Support", "Workstation Backup", "Security Training", "Server Backup", "Compliance Auditing"],
    "incident_severity": ["Medium", "Critical", "Low", "High", "Critical", "Low", "Low", "Medium", "Low", "High"],
    "days_open": [1, 3, 5, 12, 0, 2, 0, 4, 1, 9],
    "backup_status": ["Successful", "Failed Retry", "Successful", "Successful", "Successful", "Successful", "Failed Retry", "Successful", "Successful", "Failed Retry"],
    "vulnerabilities_patched": [42, 0, 15, 8, 89, 4, 0, 22, 112, 0],
    "monthly_recurring_revenue": [4250.00, 7000.00, 4250.00, 4375.00, 7000.00, 4375.00, 4250.00, 4375.00, 7000.00, 2125.00],
    "sla_status": ["In Bounds", "Breached SLA", "In Bounds", "Breached SLA", "In Bounds", "In Bounds", "In Bounds", "In Bounds", "In Bounds", "Breached SLA"],
    "service_tier": ["Silver", "Platinum", "Silver", "Gold", "Platinum", "Gold", "Silver", "Gold", "Platinum", "Silver"]
}
df = pd.DataFrame(tenant_data)

# 3. Sidebar: Unified Left-Hand Console (Creative Metrix Theme Design)
st.sidebar.title("💎 OmniMetrix OS")
st.sidebar.markdown("**MSP Management Portal Tier:** `Enterprise Multi-Tenant` ")
st.sidebar.markdown("**Network Engine Status:** `● SOC Live Mesh`")
st.sidebar.write("---")

# Corporate Tenant Switching Matrix
st.sidebar.subheader("🏢 Corporate Client Profile")
client_selection = st.sidebar.selectbox("Select Target Client Tenant:", options=["All Managed Accounts"] + list(df["client_name"].unique()))

# Navigation Links
st.sidebar.subheader("🏁 Operational Navigation")
app_panel = st.sidebar.radio("Go to Infrastructure View:", ["🔒 Cybersecurity & Infrastructure Health", "📈 Tier Revenue & Service SLAs"])

# Apply Multi-Tenant Isolation Filter
if client_selection == "All Managed Accounts":
    filtered_df = df
else:
    filtered_df = df[df["client_name"] == client_selection]

# 4. Main Workspace Header Layout
st.title("🛡️ OmniMetrix — Multi-Tenant Managed IT Command Center")
st.markdown(f"Current Dashboard Console Context: **{client_selection}**")
st.write("---")

# ==========================================
# VIEW 1: CYBERSECURITY & INFRASTRUCTURE HEALTH
# ==========================================
if app_panel == "🔒 Cybersecurity & Infrastructure Health":
    st.header("🔒 Proactive Cyber Threat Mitigation & Data Availability")
    st.markdown("##### *Real-time visualization of protection metrics, dark web risks, and workstation/server backup lifecycles.*")
    st.write("")
    
    # Core Infrastructure Risk KPIs
    m1, m2, m3 = st.columns(3)
    with m1:
        critical_threats = len(filtered_df[filtered_df["incident_severity"] == "Critical"])
        st.metric("Active Critical Cyber Incidents", value=critical_threats)
    with m2:
        total_patches = filtered_df["vulnerabilities_patched"].sum()
        st.metric("Total System Vulnerabilities Patched", value=int(total_patches))
    with m3:
        failed_backups = len(filtered_df[filtered_df["backup_status"] == "Failed Retry"])
        st.metric("Workstation/Server Backup Failures", value=failed_backups)
        
    st.write("---")
    
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        st.subheader("🍩 Service Matrix Incident Distribution")
        incident_mix = filtered_df.groupby("service_sector")["ticket_id"].count().reset_index()
        fig_donut = px.pie(incident_mix, values="ticket_id", names="service_sector", hole=0.5,
                           color_discrete_sequence=["#9C27B0", "#E040FB", "#00B0FF", "#00E676", "#FFEA00"])
        fig_donut.update_traces(texttemplate='%{value} Events<br>(%{percent})', textinfo='value+percent')
        st.plotly_chart(fig_donut, use_container_width=True)
        
    with col_g2:
        st.subheader("⏳ Incident Retention Aging Curve")
        fig_bar = px.bar(filtered_df, x="incident_severity", y="days_open", color="service_sector", barmode="group",
                         labels={"incident_severity": "Threat Severity Tier", "days_open": "Days Sitting Unresolved"})
        st.plotly_chart(fig_bar, use_container_width=True)

# ==========================================
# VIEW 2: REVENUE & SERVICE SLAS
# ==========================================
elif app_panel == "📈 Tier Revenue & Service SLAs":
    st.header("📈 Tier-Based MRR Metrics & Service SLA Performance Curve")
    st.markdown("##### *Auditing contract groupings across active Silver ($85), Gold ($125), and Platinum ($175) portfolios.*")
    st.write("")
    
    m_col1, m_col2 = st.columns(2)
    with m_col1:
        total_mrr = filtered_df.groupby("client_name")["monthly_recurring_revenue"].first().sum() if client_selection == "All Managed Accounts" else filtered_df["monthly_recurring_revenue"].iloc[0]
        st.metric("Total Managed Monthly Recurring Revenue (MRR)", value=f"${total_mrr:,.2f}")
    with m_col2:
        breached_count = len(filtered_df[filtered_df["sla_status"] == "Breached SLA"])
        st.metric("Active SLA Policy Breaches", value=breached_count)
        
    st.write("---")
    
    st.subheader("📊 Revenue Volume Generation by Service Tier")
    fig_tier = px.bar(filtered_df, x="service_tier", y="monthly_recurring_revenue", color="client_name",
                      title="Contract Footprint Value Distribution by Pricing Tier",
                      labels={"service_tier": "Subscribed Service Plan", "monthly_recurring_revenue": "Aggregated Value ($)"})
    st.plotly_chart(fig_tier, use_container_width=True)
    
    st.write("---")
    st.subheader("📋 Relational Service-Level Infrastructure Record Log")
    st.dataframe(filtered_df, use_container_width=True)
