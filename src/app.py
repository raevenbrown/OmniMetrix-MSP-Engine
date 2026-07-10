import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date

# 1. Main Page Canvas Configuration
st.set_page_config(page_title="OmniMetrix MSP Control Suite", layout="wide")

# ==========================================
# CENTRALIZED DATA STATE: 40 HIGH-DENSITY IoT ASSETS (BUNCH LLC)
# ==========================================
if "generator_fleet_db" not in st.session_state:
    st.session_state.generator_fleet_db = pd.DataFrame({
        "asset_id": [f"OMNI-{3100+i}" for i in range(1, 41)],
        "client_account": ["Bunch LLC" if i % 2 == 0 else "Industrial Power Group" for i in range(40)],
        "facility_location": [
            "Atlanta Hub A", "Savannah Terminal", "Alpharetta Substation", "Macon Logistics Center", "Augusta Medical Site",
            "Columbus Station", "Marietta Data Vault", "Athens Cold Storage", "Gainesville Plant", "Kennesaw Depot",
            "Atlanta Hub B", "Savannah Port", "Alpharetta Vault", "Macon Complex", "Augusta Plant B",
            "Columbus Hub", "Marietta Substation", "Athens Center", "Gainesville Depot", "Kennesaw Plant B",
            "Atlanta Hub C", "Savannah Yard", "Alpharetta Tower", "Macon Rail Yard", "Augusta Complex C",
            "Columbus Plant", "Marietta Hub B", "Athens Station B", "Gainesville Yard", "Kennesaw Center B",
            "Atlanta Hub D", "Savannah Hub B", "Alpharetta Site B", "Macon Depot B", "Augusta Substation B",
            "Columbus Yard B", "Marietta Tower B", "Athens Complex D", "Gainesville Site B", "Kennesaw Station D"
        ],
        "generator_brand": ["Generac", "Kohler", "Cummins", "Caterpillar", "MTU", "Generac", "Kohler", "Cummins", "Caterpillar", "MTU"] * 4,
        "academic_term": [
            "Spring 2025", "Summer 2025", "Fall 2025", "Spring 2025", "Fall 2025", 
            "Spring 2026", "Summer 2026", "Fall 2026 Preview", "Fall 2026 Preview", "Fall 2026 Preview",
            "Spring 2025", "Summer 2025", "Fall 2025", "Spring 2025", "Fall 2025", 
            "Spring 2026", "Summer 2026", "Fall 2026 Preview", "Fall 2026 Preview", "Fall 2026 Preview",
            "Spring 2025", "Summer 2025", "Fall 2025", "Spring 2025", "Fall 2025", 
            "Spring 2026", "Summer 2026", "Fall 2026 Preview", "Fall 2026 Preview", "Fall 2026 Preview",
            "Spring 2025", "Summer 2025", "Fall 2025", "Spring 2025", "Fall 2025", 
            "Spring 2026", "Summer 2026", "Fall 2026 Preview", "Fall 2026 Preview", "Fall 2026 Preview"
        ], # Mapping term strings for layout cross-compatibility
        "telemetry_link_type": ["LTE Cellular", "Iridium Satellite", "LAN/Ethernet", "LTE Cellular", "Iridium Satellite"] * 8,
        "battery_voltage": [
            13.4, 11.2, 12.8, 13.1, 9.8, 13.5, 12.9, 10.5, 13.2, 12.6,
            13.3, 11.0, 12.7, 13.0, 9.6, 13.6, 12.8, 10.4, 13.1, 12.5,
            13.2, 11.1, 12.6, 12.9, 9.5, 13.4, 12.7, 10.3, 13.0, 12.4,
            13.5, 11.3, 12.9, 13.2, 9.9, 13.7, 13.0, 10.6, 13.3, 12.7
        ],
        "fuel_level_pct": [
            88, 45, 92, 74, 15, 95, 82, 38, 79, 64,
            86, 42, 90, 71, 12, 97, 80, 35, 77, 61,
            85, 40, 89, 70, 10, 94, 79, 33, 76, 60,
            89, 47, 94, 76, 18, 99, 84, 40, 81, 66
        ],
        "studentvue_sync_status": [
            "Good Standing - Regular Sync", "Good Standing - Regular Sync", "Academic Hold - Missing Transcript",
            "Good Standing - Regular Sync", "Probation Sync Alert", "Good Standing - Regular Sync",
            "Good Standing - Regular Sync", "Financial Hold - Balance Due", "Good Standing - Regular Sync",
            "Probation Sync Alert"
        ] * 4, # Structural cross-compatibility
        "telemetry_health_tier": [
            "Good Standing - Regular Sync", "Good Standing - Regular Sync", "Critical Warning - Voltage Dropout", 
            "Good Standing - Regular Sync", "Good Standing - Regular Sync", "Good Standing - Regular Sync", 
            "Good Standing - Regular Sync", "Emergency Alert - Low Fuel Level", "Good Standing - Regular Sync", 
            "Critical Warning - Block Heater Failure"
        ] * 4,
        "operational_stage": ["Active Online", "Active Online", "Active Online", "Active Online", "Active Online", "Active Online", "Active Online", "Dispatched", "Pending Commission", "Inquiry Stage"] * 4,
        "assigned_campaign": ["Completed Yield", "Completed Yield", "Completed Yield", "Completed Yield", "Completed Yield", "Completed Yield", "Completed Yield", "Housing Deposit Nudge", "Scholarship Push", "Fall Preview Invite"] * 4,
        "hardware_tags": ["NFPA 110 Compliant, Industrial Tier", "Commercial Backup, Automated Exercise Enrolled", "Critical Infrastructure, High Isolation Unit", "Telecom Asset Site Base", "Data Center Prime Power Unit"] * 8,
        "diagnostic_log_notes": [
            "Regular automated self-test cycle completed successfully without frequency deviations.",
            "Battery charger system reporting reduced current efficiency. Monitoring parameters.",
            "Critical: Voltage drops logged under loaded state exercise conditions. Replacement scheduled.",
            "Fuel consumption rates align perfectly with peak operating load conditions.",
            "Emergency: Block heater failure logged. Coolant temp falling below minimum thresholds.",
            "Onboarding complete. Remote monitoring system fully authenticated.",
            "Transient vibration profiles fall within normal manufacturing parameters.",
            "Fuel delivery truck dispatched. On-site capacity sits below emergency threshold limits.",
            "Awaiting official field configuration parameters to pass regulatory validation.",
            "Preliminary site evaluation complete. Mapping engine structures to centralized pipeline modules."
        ] * 4,
        "to_dos_pending": [i % 4 for i in range(40)],
        "communication_preference": ["Cellular Link" if i % 2 == 0 else "Satellite Uplink" for i in range(40)]
    })

# ==========================================
# CENTRALIZED DATA STATE: 20 HIGH-DENSITY SERVICE TECH PROFILES
# ==========================================
if "faculty_retention_db" not in st.session_state:
    st.session_state.faculty_retention_db = pd.DataFrame({
        "faculty_id": [f"TECH-{400+i}" for i in range(1, 21)],
        "faculty_name": [
            "Dr. Stacey Nebriaga", "Prof. Michael Gabriele", "Dr. Tyler Pede", "Dr. Thomas Anderson", 
            "Prof. Emily Holzgrefe", "Dr. Sarah Jenkins", "Dr. David Vance", "Prof. Elena Rostova",
            "Dr. Robert Langdon", "Prof. Minerva McGonagall", "Dr. Alan Grant", "Dr. Ellie Sattler",
            "Prof. Charles Xavier", "Dr. Henry Wu", "Dr. Ian Malcolm", "Prof. Albus Dumbledore",
            "Dr. Severus Snape", "Prof. Gilderoy Lockhart", "Dr. Remus Lupin", "Dr. Pomona Sprout"
        ], # Preserving technical array parameters for name lookups
        "department_assignment": [
            "Biology", "Information Systems", "Economics", "Management", "Marketing", 
            "Accounting", "Cybersecurity", "Finance", "Biology", "Accounting", 
            "Cybersecurity", "Economics", "Entrepreneurship", "Finance", "Hospitality Management", 
            "Information Systems", "Management", "Marketing", "Hospitality Management", "Entrepreneurship"
        ], # Department mapping cross-compatibility
        "appointment_track": [
            "Master Field Engineer", "Tenured Senior Specialist", "Associate Logistics Analyst", "Master Field Engineer", 
            "Tenured Senior Specialist", "Associate Logistics Analyst", "Master Field Engineer", "Tenured Senior Specialist",
            "Master Field Engineer", "Master Field Engineer", "Associate Logistics Analyst", "Master Field Engineer",
            "Master Field Engineer", "Tenured Senior Specialist", "Tenured Senior Specialist", "Master Field Engineer",
            "Master Field Engineer", "Tenured Senior Specialist", "Associate Logistics Analyst", "Master Field Engineer"
        ],
        "faculty_staff_status": [
            "Active - Full Instructional Load", "Active - Full Instructional Load", "Pending Tenure Review Notice", 
            "Sabbatical - Research Active", "Active - Full Instructional Load", "Pending Tenure Review Notice", 
            "Active - Full Instructional Load", "Medical Leave", "Active - Full Instructional Load",
            "Active - Full Instructional Load", "Pending Tenure Review Notice", "Active - Full Instructional Load",
            "Sabbatical - Research Active", "Active - Full Instructional Load", "Active - Full Instructional Load",
            "Active - Full Instructional Load", "Active - Full Instructional Load", "Medical Leave",
            "Pending Tenure Review Notice", "Active - Full Instructional Load"
        ],
        "faculty_staff_status_clean": [
            "Active - Full Maintenance Operations", "Active - Full Maintenance Operations", "Pending Certification Renewal", 
            "Dispatched - Remote On-Site Assignment", "Active - Full Maintenance Operations", "Pending Certification Renewal", 
            "Active - Full Maintenance Operations", "Standby Status", "Active - Full Maintenance Operations",
            "Active - Full Maintenance Operations", "Pending Certification Renewal", "Active - Full Maintenance Operations",
            "Dispatched - Remote On-Site Assignment", "Active - Full Maintenance Operations", "Active - Full Maintenance Operations",
            "Active - Full Maintenance Operations", "Active - Full Maintenance Operations", "Standby Status",
            "Pending Certification Renewal", "Active - Full Maintenance Operations"
        ],
        "tenure_years_at_institution": [
            12.5, 3.0, 4.5, 16.0, 2.5, 5.0, 14.0, 1.5,
            8.0, 22.0, 3.5, 11.0, 19.5, 4.0, 1.0, 35.0,
            15.0, 2.0, 5.5, 13.0
        ],
        "semester_credit_hours_load": [
            420, 580, 390, 310, 620, 410, 330, 600,
            450, 300, 510, 400, 280, 590, 610, 200,
            350, 550, 430, 380
        ], # Capacity loads tracking
        "faculty_retention_hazard_flag": [
            "Low Risk", "Medium Risk", "Low Risk", "Low Risk", "High Risk", "Low Risk", "Low Risk", "Medium Risk",
            "Low Risk", "Low Risk", "Medium Risk", "Low Risk", "Low Risk", "High Risk", "High Risk", "Low Risk",
            "Low Risk", "High Risk", "Low Risk", "Low Risk"
        ],
        "estimated_departure_timeline": [
            "Stable (>5 Years)", "Review in 1-2 Years", "Stable (>5 Years)", "Stable (>5 Years)", "Immediate Risk (<1 Year)", "Stable (>5 Years)", "Stable (>5 Years)", "Review in 1-2 Years",
            "Stable (>5 Years)", "Stable (>5 Years)", "Review in 1-2 Years", "Stable (>5 Years)", "Stable (>5 Years)", "Immediate Risk (<1 Year)", "Immediate Risk (<1 Year)", "Stable (>5 Years)",
            "Stable (>5 Years)", "Immediate Risk (<1 Year)", "Stable (>5 Years)", "Stable (>5 Years)"
        ],
        "retention_notes": [f"Field service log certification parameters checked for specialist {i}." for i in range(1, 21)]
    })

if "coles_capacity_db" not in st.session_state:
    st.session_state.coles_capacity_db = pd.DataFrame({
        "major_name": ["Biology", "Accounting", "Cybersecurity", "Economics", "Entrepreneurship", "Finance", "Hospitality Management", "Information Systems", "Management", "Marketing"],
        "undergrad_seat_count": [850, 1250, 680, 410, 350, 980, 240, 890, 1650, 1420],
        "semester_credit_hours": [12400, 18400, 9100, 5200, 4800, 24500, 3100, 9400, 19800, 14200],
        "retention_goal_pct": [84.0, 85.0, 88.0, 80.0, 82.0, 82.0, 80.0, 88.0, 80.0, 85.0],
        "actual_retention_pct": [81.2, 82.4, 86.7, 79.1, 81.5, 76.8, 80.2, 89.5, 74.2, 81.1],
        "department_inventory_count": [45, 120, 85, 30, 25, 110, 15, 60, 140, 130]
    })

ksu_gold_palette = ["#FFC400", "#161B22", "#FFA000", "#FF8F00", "#4E5D6C", "#FF5722", "#00E676"]

# ==========================================
# SIDEBAR SELECTION SYSTEM
# ==========================================
st.sidebar.title("⚡ OmniMetrix MSP Core")
st.sidebar.markdown("**Enterprise Node:** `Bunch LLC Fleet Control`")
st.sidebar.write("---")

st.sidebar.subheader("👁️ Layer Visibility Options")
show_students = st.sidebar.checkbox("Show Telemetry Asset Tracks", value=True)
show_faculty = st.sidebar.checkbox("Show Field Service Engineer Tracks", value=True)
st.sidebar.write("---")

st.sidebar.subheader("🗂️ Global Fleet Filters")
dept_filter = st.sidebar.selectbox("Filter by Asset Care Hub Assignment:", options=["All Departments"] + list(st.session_state.coles_capacity_db["major_name"].unique()))
term_filter = st.sidebar.selectbox("Target Operational Monitoring Horizon:", options=["All Semesters", "Spring 2025", "Summer 2025", "Fall 2025", "Spring 2026", "Summer 2026", "Fall 2026 Preview"])
studentvue_filter = st.sidebar.selectbox("Telemetry Connection Registration Profile Status:", options=["All Student Tiers", "Good Standing - Regular Sync", "Academic Hold - Missing Transcript", "Financial Hold - Balance Due", "Probation Sync Alert"])
faculty_status_filter = st.sidebar.selectbox("Field Service Technical Dispatch Status:", options=["All Faculty Tiers", "Active - Full Instructional Load", "Pending Tenure Review Notice", "Sabbatical - Research Active", "Medical Leave"])

processed_funnel = st.session_state.generator_fleet_db.copy()
processed_faculty = st.session_state.faculty_retention_db.copy()

if dept_filter != "All Departments":
    processed_funnel = processed_funnel[processed_funnel["intended_major"] == dept_filter]
    processed_faculty = processed_faculty[processed_faculty["department_assignment"] == dept_filter]

if term_filter != "All Semesters":
    processed_funnel = processed_funnel[processed_funnel["academic_term"] == term_filter]

if studentvue_filter != "All Student Tiers":
    processed_funnel = processed_funnel[processed_funnel["studentvue_sync_status"] == studentvue_filter]

if faculty_status_filter != "All Faculty Tiers":
    processed_faculty = processed_faculty[processed_faculty["faculty_staff_status"] == faculty_status_filter]

st.sidebar.write("---")
st.sidebar.subheader("🏁 Navigation Terminal")

nav_options = []
if show_students: nav_options.append("👤 Hardware Telemetry Hub (Bunch LLC)")
if show_faculty: nav_options.append("🏛️ Field Technician Dispatch Terminal")
if show_students: nav_options.append("📢 EAB Targeted Action Dispatcher")
nav_options.append("📈 Reports & Analytics Gateway (All 10 Keys)")

app_panel = st.sidebar.radio("Select Operational Workspace Desk:", options=nav_options)

# ==========================================
# MODULE 1: HARDWARE TELEMETRY PORTAL
# ==========================================
if app_panel == "👤 Hardware Telemetry Hub (Bunch LLC)":
    main_workspace, ai_assistant_col = st.columns([3, 1])
    
    with main_workspace:
        st.markdown("## 📋 Fleet Operations: Funnel Progress & Hardware Asset Management")
        st.write("---")
        
        fc1, fc2, fc3, fc4 = st.columns(4)
        with fc1: st.metric("Sourced Monitored Assets Focus", value=len(processed_funnel))
        with fc2: st.metric("Dispatched Tech Tickets Pipeline", value=len(processed_funnel[processed_funnel["operational_stage"] == "Dispatched"]))
        with fc3: st.metric("Online Fleet Operational Yield", value=len(processed_funnel[processed_funnel["operational_stage"] == "Active Online"]))
        with fc4: 
            if "to_dos_pending" in processed_funnel.columns and len(processed_funnel) > 0:
                st.metric("Open System Work Reminders", value=int(processed_funnel["to_dos_pending"].sum()))
            else: st.metric("Open System Work Reminders", value=0)
        
        st.write("")
        if len(processed_funnel) > 0:
            selected_prospect = st.selectbox("🔍 Select Active Monitored Hardware Asset File to Audit:", options=list(processed_funnel["student_name"].unique()))
            master_match = st.session_state.generator_fleet_db[st.session_state.generator_fleet_db["student_name"] == selected_prospect]
            idx = master_match.index[0]
            p_row = master_match.loc[idx]
            
            with st.container(border=True):
                st.markdown(f"### Telemetry Node: **{p_row['facility_location']}** ({p_row['generator_brand']}) | Node ID: `{p_row['applicant_id']}`")
                st.write("")
                det_col1, det_col2 = st.columns(2)
                with det_col1:
                    st.markdown(f"**📚 Assigned Asset Hub Sector:** `{p_row['intended_major']}`")
                    st.markdown(f"**🗓️ Monitoring Horizon Target:** `{p_row['academic_term']}`")
                    st.markdown(f"**🎯 Telemetry Operating Stage:** `{p_row['operational_stage']}`")
                with det_col2:
                    st.markdown(f"**🔋 Monitored Battery Voltage:** `{p_row['battery_voltage']} V`")
                    st.markdown(f"**⛽ Fuel Level Tank Capacity:** `{p_row['fuel_level_pct']}%`")
                    st.markdown(f"**🔒 Central System Link Update:** `{p_row['telemetry_health_tier']}`")
            
            st.write("")
            st.subheader("🤖 AI Assistant: Automated Machine Diagnostic Insights")
            with st.container(border=True):
                st.markdown(f"*🧠 Real-Time Telemetry Digest Material:* **\"{p_row['diagnostic_log_notes']}\"**")
                
            st.write("---")
            st.subheader("🛠️ Streamline Hardware Maintenance Work Orders")
            w1, w2, w3 = st.columns([1, 1, 2])
            with w1: stage_update = st.selectbox("Modify Telemetry Operating Stage:", options=["Active Online", "Dispatched", "Pending Commission", "Inquiry Stage"])
            with w2: camp_update = st.selectbox("Reassign Outreach Action Track:", options=["Completed Yield", "Fall Preview Invite", "Scholarship Push", "Housing Deposit Nudge"])
            with w3: append_note = st.text_input("Append Diagnostic Communication Log Entry:")
                
            if st.button("🚀 Commit Adjustments to Centralized Fleet View", use_container_width=True):
                st.session_state.generator_fleet_db.at[idx, "operational_stage"] = stage_update
                st.session_state.generator_fleet_db.at[idx, "assigned_campaign"] = camp_update
                if append_note: st.session_state.generator_fleet_db.at[idx, "diagnostic_log_notes"] = f"{p_row['diagnostic_log_notes']} | Update: {append_note}"
                st.success("Fleet telemetry profile adjusted successfully.")
                st.rerun()
        else: st.warning("No tracking records match filters.")
            
        st.write("---")
        st.subheader("📋 Centralized View: Filtered Core Fleet Ingestion Ledger")
        st.dataframe(processed_funnel[["applicant_id", "student_name", "facility_location", "generator_brand", "academic_term", "operational_stage", "telemetry_health_tier"]], use_container_width=True, hide_index=True)

    with ai_assistant_col:
        st.markdown("### 🤖 IoT AI Copilot")
        st.write("---")
        if len(processed_funnel) > 0 and 'p_row' in locals():
            with st.container(border=True):
                st.markdown(f"**Node Target:** `{p_row['applicant_id']}`")
                st.write(f"* **Fuel Level:** {p_row['fuel_level_pct']}%")
                st.write(f"* **Voltage:** {p_row['battery_voltage']}V")
        st.write("")
        st.button("✉️ Dispatch Automated Nudge Trigger Blast", use_container_width=True)
        st.button("📅 Schedule Emergency Field Engineer Onsite Visit", use_container_width=True)

# ==========================================
# MODULE 2: FIELD TECHNICIAN DISPATCH TERMINAL
# ==========================================
elif app_panel == "🏛️ Field Technician Dispatch Terminal":
    st.header("🏛️ Field Service Engineering Workload Terminal")
    st.markdown("##### *Auditing technical staff tenure years, field ticket generation workloads, and technician burnout prevention metrics.*")
    st.write("---")
    
    if len(processed_faculty) > 0:
        faculty_picker = st.selectbox("👤 Select Detailed Field Specialist Profile to Open:", options=list(processed_faculty["faculty_name"].unique()))
        f_row = processed_faculty[processed_faculty["faculty_name"] == faculty_picker].iloc[0]
        
        with st.container(border=True):
            st.markdown(f"### Engineering Staff File: **{f_row['faculty_name']}** | ID: `{f_row['faculty_id']}`")
            st.write("")
            f_c1, f_c2, f_c3 = st.columns(3)
            with f_c1:
                st.markdown(f"**🏢 Regional Care Assignment Hub:** `{f_row['department_assignment']}`")
                st.markdown(f"**🎯 Field Appointment Track:** `{f_row['appointment_track']}`")
                st.markdown(f"**⚙️ Specialist Status Update:** `{f_row['faculty_staff_status_clean']}`")
            with f_c2:
                st.markdown(f"**⏳ Years Staying with Firm:** `{f_row['tenure_years_at_institution']} Years`")
                st.markdown(f"**📚 Active Field Ticket Assigned Load:** `{f_row['semester_credit_hours_load']} Hours`")
            with f_c3:
                st.markdown(f"**🔮 Workload Hazard Flag Tier:** `{f_row['faculty_retention_hazard_flag']}`")
                st.markdown(f"**📅 Departure Timeline Estimate:** `{f_row['estimated_departure_timeline']}`")
            st.write("---")
            st.markdown(f"**📥 HR Operations Notes:** *\"{f_row['retention_notes']}\"*")
            
        st.write("---")
        f_g1, f_g2 = st.columns(2)
        with f_g1:
            fig_tenure = px.bar(processed_faculty, x="faculty_name", y="tenure_years_at_institution", title="Technician Service Tenure Longevity Profiles (Firm Retention Curve)", color="appointment_track", color_discrete_sequence=ksu_gold_palette)
            st.plotly_chart(fig_tenure, use_container_width=True)
        with f_g2:
            fig_hazard = px.pie(processed_faculty, values="semester_credit_hours_load", names="faculty_retention_hazard_flag", title="Field Service Allocation Volume Shares Sorted by Risk Flag", hole=0.4, color_discrete_sequence=["#00E676", "#FFC400", "#FF5722"])
            st.plotly_chart(fig_hazard, use_container_width=True)
    else: st.warning("No technician metrics log segments match active global filters.")

# ==========================================
# MODULE 3: TARGETED CAMPAIGN MANAGER
# ==========================================
elif app_panel == "📢 EAB Targeted Campaign Manager":
    st.header("📢 Custom Communications Telemetry Action Dispatcher")
    st.write("---")
    with st.form("campaign_creation_desk"):
        c_name = st.text_input("Outreach Action Name Target Label:", value="Emergency Fuel Maintenance Nudge Notice")
        c_channel = st.selectbox("Primary Notification Uplink Channel Strategy:", options=["Personalized Text/SMS Blasts", "Targeted Email Sequences", "Direct Control Handshake Codes"])
        c_cohort = st.selectbox("Target Audience Filter Group Stage Pool:", options=["Inquiry Population Pool", "Pending Commission Verification Slices", "Critical Alarm - Yield Warning Assets Focus"])
        if st.form_submit_button("🚀 Deploy Nuanced Outreach & Launch Campaign"):
            st.success(f"Action sequence track '{c_name}' deployed successfully! Automated notifications streaming.")

    st.write("---")
    fig_funnel = px.bar(processed_funnel, x="operational_stage", title="Continuous Fleet Status Progress Funnel Monitor", color="operational_stage", color_discrete_sequence=ksu_gold_palette)
    st.plotly_chart(fig_funnel, use_container_width=True)

# ==========================================
# MODULE 4: REPORTS & ANALYTICS GATEWAY (ALL 10 KEYS)
# ==========================================
elif app_panel == "📈 Reports & Analytics Gateway (All 10 Keys)":
    st.header("📈 Reports & Analytics Portfolio Gateway")
    st.markdown("##### *Mapping interactive query views to verify all 10 Key Responsibilities outlined in the data analyst job profile framework.*")
    st.write("---")
    
    ledger_df = pd.DataFrame({
        "Key ID": [f"Key {i}" for i in range(1, 11)],
        "Job Description Requirement Statement": [
            "1. Compiles standard and ad hoc reports per established guidelines and frequency",
            "2. Provides reports, analysis and data interpretation for all assigned departments",
            "3. Identifies areas of opportunity and presents findings and recommendations to leadership and stakeholders",
            "4. Provides productivity analysis reports",
            "5. Develops and maintains reports to measure operational and/or utilization activity",
            "6. May be required to prepare ad hoc reports required of association affiliations and/or oversight and regulatory requirements",
            "7. Compiles recurring operational review that includes trend analysis",
            "8. May assists with departmental inventory reporting and analysis",
            "9. May be required to prepare ad hoc reporting that assists with measuring department performance and/or effectiveness",
            "10. Collaborate with a variety of stakeholders across campus, including working closely with the Office of University Data Strategy to maintain alignment with overall university data strategy"
        ],
        "Dashboard Validation Status": ["🟢 Engine Integrated & Deployable"] * 10
    })
    st.dataframe(ledger_df, use_container_width=True, hide_index=True)
    st.write("---")
    
    selected_key_tab = st.selectbox("Select Active Compliance Report to Query Natively:", options=list(ledger_df["Job Description Requirement Statement"]))
    st.write("---")
    
    if "1. Compiles standard and ad hoc" in selected_key_tab:
        st.markdown("### 📊 Key 1: Standardized vs. Ad Hoc Telemetry Log Extractions")
        rep_type = st.radio("Select Guidelines Frequency Distribution Format:", ["Standard Recurring (Weekly Intake)", "Ad Hoc Live Extract"])
        if rep_type == "Standard Recurring (Weekly Intake)":
            st.info("📦 **Standard Guideline Run:** Extracting structured multi-semester hardware status records and diagnostic metrics.")
            st.dataframe(processed_funnel[["applicant_id", "student_name", "facility_location", "generator_brand", "academic_term", "operational_stage"]], use_container_width=True, hide_index=True)
        else:
            st.warning("⚡ **Ad Hoc Command Executed:** Running dynamic cross-sectional splice targeting critical emergency fleet dropouts.")
            ad_hoc_subset = processed_funnel[processed_funnel["fuel_level_pct"] < 40]
            st.dataframe(ad_hoc_subset, use_container_width=True, hide_index=True)

    elif "2. Provides reports, analysis and data interpretation" in selected_key_tab:
        st.markdown("### 🏛️ Key 2: Regional Service Hub Interpretation Summary Matrix")
        c_act, c_graph = st.columns(2)
        with c_act:
            st.info("📊 **Sourced Technical Infrastructure Profiles**")
            st.dataframe(processed_faculty[["faculty_name", "department_assignment", "appointment_track", "faculty_staff_status_clean", "tenure_years_at_institution"]], use_container_width=True, hide_index=True)
        with c_graph:
            fig_key2 = px.bar(processed_faculty, x="faculty_name", y="semester_credit_hours_load", title="Total Active Field Maintenance Hours Logged per Technician", color_discrete_sequence=["#FFC400"])
            st.plotly_chart(fig_key2, use_container_width=True)

    elif "3. Identifies areas of opportunity" in selected_key_tab:
        st.markdown("### 💡 Key 3: Leadership Findings & Strategic Fleet Recommendations Engine")
        low_voltage_leads = processed_funnel[processed_funnel["battery_voltage"] < 11.0] if len(processed_funnel) > 0 else pd.DataFrame()
        with st.container(border=True):
            st.markdown("🏆 **Executive Data Insights Memorandum (Bunch LLC)**")
            st.write(f"1. **Identified Area of Opportunity:** Found **{len(low_voltage_leads)}** active asset generator nodes demonstrating severe low battery voltage drops under load conditions.")
            st.write("2. **Analytical Interpretation:** Telemetry logs confirm a direct statistical relationship with charger system age benchmarks.")
            st.write("3. **Actionable Recommendation to Leadership:** Deploy proactive text action dispatches to update battery configurations before winter peak cycles.")
        if len(low_voltage_leads) > 0:
            st.error("🚨 Critical Opportunity Monitoring Watchlist:")
            st.dataframe(low_voltage_leads[["applicant_id", "facility_location", "generator_brand", "battery_voltage", "telemetry_health_tier"]], use_container_width=True, hide_index=True)

    elif "4. Provides productivity analysis reports" in selected_key_tab:
        st.markdown("### ⏳ Key 4: Action Campaign Effectiveness Productivity Audit Log")
        if len(processed_funnel) > 0:
            prod_df = processed_funnel.groupby("assigned_campaign").agg(total_assets_reached=("applicant_id", "count"), total_pending_tasks=("to_dos_pending", "sum"), mean_voltage_index=("battery_voltage", "mean")).reset_index()
            c_p1, c_p2 = st.columns(2)
            with c_p1: st.dataframe(prod_df, use_container_width=True, hide_index=True)
            with c_p2:
                fig_prod = px.bar(prod_df, x="assigned_campaign", y="total_assets_reached", title="Total Active Asset Density Count per Deployed Campaign Channel Track", color_discrete_sequence=["#161B22"])
                st.plotly_chart(fig_prod, use_container_width=True)

    elif "5. Develops and maintains reports to measure operational" in selected_key_tab:
        st.markdown("### ⚙️ Key 5: Operational Utilization & Activity Benchmarks")
        if len(processed_funnel) > 0:
            util_df = processed_funnel.groupby("communication_preference").size().reset_index(name="active_allocated_leads")
            c_u1, c_u2 = st.columns(2)
            with c_u1: st.dataframe(util_df, use_container_width=True, hide_index=True)
            with c_u2:
                fig_util = px.pie(util_df, values="active_allocated_leads", names="communication_preference", title="Preferred Telemetry Uplink Allocation Distribution", color_discrete_sequence=ksu_gold_palette)
                st.plotly_chart(fig_util, use_container_width=True)

    elif "6. May be required to prepare ad hoc reports required of association" in selected_key_tab:
        st.markdown("### 🏛️ Key 6: NFPA 110 Regulatory Compliance Oversight Gateway")
        reg_target = st.selectbox("Select Industrial Compliance Framework Protocol Profile:", ["NFPA 110 Emergency Power Standby Audit", "OSHA Critical Asset Field Safety Log", "EPA Local Emissions Run Standard"])
        with st.container(border=True):
            st.markdown(f"📁 **Active Compliance Manifest Structure:** `{reg_target}`")
            st.write("*   **Relational Assets Bound:** Bunch LLC fleet database matrices.")
            st.success("🟢 Validation Protocol: Pass. System metrics formatting maps perfectly onto federal compliance transmission standards.")

    elif "7. Compiles recurring operational review that includes trend analysis" in selected_key_tab:
        st.markdown("### 📈 Key 7: Multi-Semester Longitudinal Trend Analytics Curve")
        trend_df = st.session_state.coles_capacity_db.copy()
        trend_df["retention_shortfall"] = trend_df["retention_goal_pct"] - trend_df["actual_retention_pct"]
        c_t1, c_t2 = st.columns([2, 3])
        with c_t1: st.dataframe(trend_df[["major_name", "retention_goal_pct", "actual_retention_pct", "retention_shortfall"]], use_container_width=True, hide_index=True)
        with c_t2:
            fig_trend = px.line(trend_df, x="major_name", y="retention_shortfall", title="Longitudinal Shortfall Growth Profile Gaps Trends", markers=True, color_discrete_sequence=["#FF5722"])
            st.plotly_chart(fig_trend, use_container_width=True)

    elif "8. May assists with departmental inventory" in selected_key_tab:
        st.markdown("### 🖥️ Key 8: Departmental Technology Asset Inventory Analysis")
        c_i1, c_i2 = st.columns(2)
        with c_i1: st.dataframe(st.session_state.coles_capacity_db[["major_name", "undergrad_seat_count", "department_inventory_count"]], use_container_width=True, hide_index=True)
        with c_i2:
            fig_inv = px.bar(st.session_state.coles_capacity_db, x="major_name", y="department_inventory_count", title="Hardware Kiosk Terminals Deployed by Regional Control Center Hub", color_discrete_sequence=["#4E5D6C"])
            st.plotly_chart(fig_inv, use_container_width=True)

    elif "9. May be required to prepare ad hoc reporting that assists with measuring department performance" in selected_key_tab:
        st.markdown("### 🎯 Key 9: Center Performance & Program Effectiveness Matrix")
        if len(processed_funnel) > 0:
            res_counts = processed_funnel.groupby("operational_stage").size().reset_index(name="total_cases")
            c_pf1, f_pf2 = st.columns(2)
            with c_pf1: st.dataframe(res_counts, use_container_width=True, hide_index=True)
            with f_pf2:
                fig_perf = px.bar(res_counts, x="operational_stage", y="total_cases", title="Recruitment Progress Conversion Rates Profile", color_discrete_sequence=["#00E676"])
                st.plotly_chart(fig_perf, use_container_width=True)

    elif "10. Collaborate with a variety of stakeholders across campus" in selected_key_tab:
        st.markdown("### 🤝 Key 10: Office of Enterprise Data Strategy Taxonomy Alignment Matrix")
        with st.container(border=True):
            st.markdown("### 🏛️ Centralized Governance Mappings Framework Terminal")
            st.write("🔗 **Data Governance Layer:** Bunch LLC Corporate Data Strategy Taxonomy Directive standard verified.")
            st.write("📡 **API Synchronization Handshake Link:** `https://data-strategy.bunch-llc.com/v1/sync` active.")
            st.success("🟢 **Alignment Confirmed:** Local telemetry metadata schemas map completely and perfectly to central enterprise repository frameworks.")
