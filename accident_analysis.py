import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_traffic_accidents():
    # Update this filename if yours matches a newer version exactly
    csv_file = "US_Accidents_March23.csv" 
    
    if not os.path.exists(csv_file):
        # Look for any CSV file in the directory if the exact name doesn't match
        csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]
        if csv_files:
            csv_file = csv_files[0]
        else:
            print("Error: Could not find your dataset CSV file in this folder.")
            return

    print(f"Reading {csv_file}... (Sampling the first 100,000 rows for performance)")
    # We read a sample of rows so your system memory (RAM) doesn't overload
    df = pd.read_csv(csv_file, nrows=100000)
    print("--- Dataset Sample Loaded Successfully ---")

    # 1. PARSE TIME OF DAY PATTERNS
    # Convert timestamp string columns to actual datetime objects
    df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')
    df['Hour'] = df['Start_Time'].dt.hour
    df['Weekday'] = df['Start_Time'].dt.day_name()

    sns.set_theme(style="whitegrid")

    # -------------------------------------------------------------
    # VISUALIZATION 1: Hourly Distribution (Time of Day Analysis)
    # -------------------------------------------------------------
    plt.figure(figsize=(9, 5))
    sns.histplot(data=df.dropna(subset=['Hour']), x='Hour', bins=24, kde=True, color='crimson')
    plt.title('Traffic Accident Distribution by Time of Day', fontsize=14, fontweight='bold')
    plt.xlabel('Hour of the Day (0 - 23)', fontsize=12)
    plt.ylabel('Accident Count', fontsize=12)
    plt.xticks(range(0, 24))
    plt.tight_layout()
    plt.savefig('accident_time_distribution.png', dpi=300)
    plt.show()

    # -------------------------------------------------------------
    # VISUALIZATION 2: Top Weather Contributing Factors
    # -------------------------------------------------------------
    plt.figure(figsize=(10, 5))
    top_weather = df['Weather_Condition'].value_counts().head(10)
    sns.barplot(
        x=top_weather.values, 
        y=top_weather.index, 
        hue=top_weather.index,
        palette='coolwarm',
        legend=False
    )
    plt.title('Top 10 Weather Conditions During Accidents', fontsize=14, fontweight='bold')
    plt.xlabel('Accident Count', fontsize=12)
    plt.ylabel('Weather Condition', fontsize=12)
    plt.tight_layout()
    plt.savefig('accident_weather_factors.png', dpi=300)
    plt.show()

    # -------------------------------------------------------------
    # VISUALIZATION 3: Geographic Hotspots (Top 10 States)
    # -------------------------------------------------------------
    plt.figure(figsize=(9, 5))
    top_states = df['State'].value_counts().head(10)
    sns.barplot(x=top_states.index, y=top_states.values, hue=top_states.index, palette='magma', legend=False)
    plt.title('Top 10 US States with Highest Accident Counts', fontsize=14, fontweight='bold')
    plt.xlabel('State Abbreviation', fontsize=12)
    plt.ylabel('Accident Count', fontsize=12)
    plt.tight_layout()
    plt.savefig('accident_state_hotspots.png', dpi=300)
    plt.show()

    print("\nAnalysis finished! Check your folder for the generated plot images.")

if __name__ == "__main__":
    analyze_traffic_accidents()
