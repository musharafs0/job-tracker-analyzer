import streamlit as st
import pandas as pd
from datetime import datetime
import os

FILE_PATH = "data/applications.csv"

st.title("📋 Job Tracker & Application Analyzer")

# Load or create CSV
if not os.path.exists(FILE_PATH):
    df = pd.DataFrame(columns=["Date", "Company", "Role", "Platform", "Status"])
    df.to_csv(FILE_PATH, index=False)
else:
    df = pd.read_csv(FILE_PATH)

# Menu options
menu = ["Add Application", "View All", "Filter by Status", "Summary", "Charts"]
choice = st.sidebar.selectbox("Menu", menu)

# 1. Add Application
if choice == "Add Application":
    st.subheader("Add a New Job Application")

    company = st.text_input("Company Name")
    role = st.text_input("Job Role")
    platform = st.selectbox("Platform", ["LinkedIn", "Naukri", "Indeed", "Other"])
    status = st.selectbox("Status", ["Applied", "Interview", "Rejected", "Offer"])
    submit = st.button("Add")

    if submit and company and role:
        new_entry = {
            "Date": datetime.today().strftime('%Y-%m-%d'),
            "Company": company,
            "Role": role,
            "Platform": platform,
            "Status": status
        }
        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        df.to_csv(FILE_PATH, index=False)
        st.success("✅ Application added successfully!")

# 2. View All
elif choice == "View All":
    st.subheader("📄 All Applications")
    st.dataframe(df)

# 3. Filter by Status
elif choice == "Filter by Status":
    st.subheader("🔍 Filter by Status")
    selected_status = st.selectbox("Select status", df["Status"].unique())
    filtered = df[df["Status"] == selected_status]
    st.dataframe(filtered)

# 4. Summary
elif choice == "Summary":
    st.subheader("📊 Application Summary")
    st.write("Total Applications:", len(df))
    st.write("Status Breakdown:", df["Status"].value_counts())
    st.write("Top Platforms:", df["Platform"].value_counts().head(3))
    st.write("Top Companies:", df["Company"].value_counts().head(3))

# 5. Charts
elif choice == "Charts":
    st.subheader("📈 Visualizations")
    st.bar_chart(df["Status"].value_counts())
    st.write("")
    st.subheader("Platform Usage")
    st.pyplot(df["Platform"].value_counts().plot.pie(autopct="%1.1f%%").get_figure())
