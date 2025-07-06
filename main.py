import pandas as pd
from datetime import datetime
import os
from analysis.analyzer import show_summary,show_status_chart, show_platform_chart


def add_application():
    # Create the new job entry
    new_entry = {
        "Date": datetime.today().strftime('%Y-%m-%d'),
        "Company": input("Enter Company Name: "),
        "Role": input("Enter Job Role: "),
        "Platform": input("Enter Platform (LinkedIn/Naukri/Other): "),
        "Status": input("Enter Status (Applied/Interview/Rejected/Offer): ")
    }

    # Convert to DataFrame
    new_df = pd.DataFrame([new_entry])

    # Define CSV file path
    file_path = "data/applications.csv"

    # Check if file exists and append or create
    if os.path.exists(file_path):
        new_df.to_csv(file_path, mode='a', header=False, index=False)
    else:
        new_df.to_csv(file_path, mode='w', header=True, index=False)

    print("✅ Application added successfully!")



def view_applications():
    import pandas as pd

    file_path = "data/applications.csv"

    try:
        df = pd.read_csv(file_path)

        print("\n📄 All Applications:\n")
        print(df.to_string(index=False))  # Display full table without index

    except FileNotFoundError:
        print("❌ No data found. Add some job applications first.")

def filter_by_status():
    import pandas as pd
    file_path = "data/applications.csv"

    try:
        df = pd.read_csv(file_path)
        status = input("Enter status to filter by (Applied/Interview/Rejected/Offer): ").capitalize()
        filtered = df[df['Status'] == status]

        if not filtered.empty:
            print(f"\n📄 Applications with status '{status}':\n")
            print(filtered.to_string(index=False))
        else:
            print(f"❗ No applications found with status '{status}'.")

    except FileNotFoundError:
        print("❌ No data found.")
if __name__ == "__main__":
    print("📌 Job Tracker")
    print("1. Add Application")
    print("2. View All Applications")
    print("3. Filter by Status")
    print("4. Show Summary")
    print("5. Status Chart")
    print("6. Platform Pie Chart")

    choice = input("Choose an option (1/2/3/4/5/6): ")

    if choice == "1":
        add_application()
    elif choice == "2":
        view_applications()
    elif choice == "3":
        filter_by_status()
    elif choice=="4":
        show_summary()
    elif choice=="5":
        show_status_chart()
    elif choice=="6":
        show_platform_chart()
    else:
        print("❗ Invalid choice.")

