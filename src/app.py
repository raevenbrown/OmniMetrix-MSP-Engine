import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Main Page Canvas Configuration
st.set_page_config(page_title="OmniMetrix Enterprise BI Engine", layout="wide")

# 2. Ingest Multi-Tenant B2B Managed IT & Cyber Dataset
tenant_data = {
    "ticket_id": [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    "client_name": ["Apex Logistics", "Summit Health Network", "Apex Logistics", "Vanguard Finance", "Summit Health Network", "Vanguard Finance", "Apex Logistics", "Vanguard Finance", "Summit Health Network", "Horizon Retail"],
    "service_sector": ["Cybersecurity", "Backup & Recovery", "Helpdesk Tier 2", "Compliance Auditing", "Cybersecurity", "Helpdesk Tier 1", "Backup & Recovery", "Cybersecurity", "Cloud Ops", "Compliance Auditing"],
    "incident_severity": ["Critical", "High", "Medium", "High", "Critical", "Low", "Low", "Medium", "Low", "High"],
    "days_open": [1, 3, 5, 12, 0, 2, 0, 4, 1, 9],
    "backup_status": ["Successful", "Failed Retry", "Successful", "Successful", "Successful", "Successful", "Failed Retry", "Successful", "Successful", "Failed Retry"],
    "vulnerabilities_patched": [42, 0, 15, 8, 89, 4, 0, 22, 112, 0],
    "monthly_recurring_revenue": [4500.00, 7200.00, 4500.00, 5800.00, 7200.00, 5800.00, 4500.00, 5800.00, 7200.00, 3900.00],
    "sla_status": ["In Bounds", "Breached SLA", "In Bounds", "Breached SLA", "In Bounds", "In Bounds", "In Bounds", "In Bounds", "In Bounds", "Breached SLA"]
}
df = pd.DataFrame(tenant_data)

# 3. Sidebar: Unified Left-Hand Console (Creative Metrix Theme Design)
st.sidebar.title("💎 OmniMetrix OS")
st.sidebar.markdown("**MSP Management Portal Tier:** `Enterprise Multi-Tenant` ")
st.sidebar.markdown("**Network Engine Status:** `● SOC Live Mesh`")
st.sidebar.write("---")

# Account Profile Synchronizer Module
st.sidebar.subheader("👤 Portal Management")
uploaded_file = st.sidebar.file_uploader("🔄 Sync Active Profile / Drop Local CSV Batch", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

# Corporate Tenant Switching Matrix
st.sidebar.subheader("🏢 Corporate Client Profile")
client_selection = st.sidebar.selectbox("Select Target Client Tenant:", options=["All Managed Accounts"] + list(df["client_name"].unique()))

# Navigation Links
st.sidebar.subheader("🏁 Operational Navigation")
app_panel = st.sidebar.radio("Go to Infrastructure View:", ["🔒 Cybersecurity & Infrastructure Health", "📈 Revenue & Service SLAs"])

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
    st.markdown("##### *Real-time vulnerability distribution tracking, disaster recovery validation, and resolution lifecycle metrics.*")
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
        st.metric("Disaster Recovery Redundancy Failures", value=failed_backups)
        
    st.write("---")
    
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        st.subheader("🍩 Security Incident Infrastructure Distribution")
        incident_mix = filtered_df.groupby("service_sector")["ticket_id"].count().reset_index()
        fig_donut = px.pie(incident_mix, values="ticket_id", names="service_sector", hole=0.5,
                           color_discrete_sequence=["#9C27B0", "#E040FB", "#00B0FF", "#00E676"])
        fig_donut.update_traces(texttemplate='%{value} Events<br>(%{percent})', textinfo='value+percent')
        st.plotly_chart(fig_donut, use_container_width=True)
        st.caption("**Analytical Threat Breakdown:** This donut chart visualizes absolute event volume alongside relative percentage breakdowns across core infrastructure sectors, surfacing precisely which layers create the largest support burden.")
        
    with col_g2:
        st.subheader("⏳ Cyber Incident Resolution Lifecycles")
        fig_bar = px.bar(filtered_df, x="incident_severity", y="days_open", color="service_sector", barmode="group",
                         labels={"incident_severity": "Threat Classification Tier", "days_open": "Consecutive Days Unresolved"})
        st.plotly_chart(fig_bar, use_container_width=True)
        st.caption("**Operational Cycle Explanation:** This group distribution tracks the consecutive calendar days that infrastructure vulnerabilities or system incidents remain unresolved, highlighting processing bottlenecks.")

# ==========================================
# VIEW 2: REVENUE & SERVICE SLAS
# ==========================================
elif app_panel == "📈 Revenue & Service SLAs":
    st.header("📈 Financial Contract Value & Service SLA Performance Curve")
    st.markdown("##### *Monitoring aggregated monthly recurring revenue pools, tracking compliance rules, and verifying contract health.*")
    st.write("")
    
    m_col1, m_col2 = st.columns(2)
    with m_col1:
        total_mrr = filtered_df.groupby("client_name")["monthly_recurring_revenue"].first().sum() if client_selection == "All Managed Accounts" else filtered_df["monthly_recurring_revenue"].iloc[0]
        st.metric("Total Account Monthly Recurring Revenue (MRR)", value=f"${total_mrr:,.2f}")
    with m_col2:
        breached_count = len(filtered_df[filtered_df["sla_status"] == "Breached SLA"])
        st.metric("Active Service Level Agreement (SLA) Breaches", value=breached_count)
        
    st.write("---")
    
    st.subheader("📈 Chronological Contract Generation Trends")
    fig_line = px.line(filtered_df, x="ticket_id", y="monthly_recurring_revenue", color="client_name", markers=True,
                       title="MRR Production Generation Pipeline Velocity",
                       labels={"ticket_id": "System Log Reference Sequence", "monthly_recurring_revenue": "Contract Value Allocation ($)"})
    st.plotly_chart(fig_line, use_container_width=True)
    st.caption("**Financial Trend Explanation:** This chronological mapping charts active B2B contract distributions, tracking recurring portfolio value parameters to visualize cash flow consistency across accounts.")
    
    st.write("---")
    st.subheader("📋 Relational Infrastructure Incident Record Log")
    st.dataframe(filtered_df, use_container_width=True)
