import pandas as pd

def show_summary(file_path="data/applications.csv"):
    try:
        df = pd.read_csv(file_path)

        print("\n📊 Job Application Summary:\n")
        print(f"Total Applications: {len(df)}")
        print("\nStatus Breakdown:")
        print(df["Status"].value_counts())
        print("\nMost Used Platform:")
        print(df["Platform"].value_counts().head(3))
        print("\nTop Companies Applied To:")
        print(df["Company"].value_counts().head(3))

    except FileNotFoundError:
        print("❌ No application data found.")
    except pd.errors.EmptyDataError:
        print("⚠️ CSV file is empty.")
import matplotlib.pyplot as plt

def show_status_chart(file_path="data/applications.csv"):
    df = pd.read_csv(file_path)
    status_counts = df["Status"].value_counts()

    # Plot
    status_counts.plot(kind="bar", color="skyblue")
    plt.title("Job Application Status")
    plt.xlabel("Status")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.show()
def show_platform_chart(file_path="data/applications.csv"):
    df = pd.read_csv(file_path)
    platform_counts = df["Platform"].value_counts()

    platform_counts.plot(kind="pie", autopct="%1.1f%%", startangle=140)
    plt.title("Platforms Used for Applications")
    plt.ylabel("")  # Hide y-axis label
    plt.tight_layout()
    plt.show()
