import pandas as pd
import matplotlib.pyplot as plt

# Load Locust CSV
df = pd.read_csv("fn_run_stats_history.csv")

# Convert timestamp to relative time (seconds since start)
df["Time_sec"] = df["Timestamp"] - df["Timestamp"].iloc[0]

# Plot
plt.figure(figsize=(8, 5))
plt.plot(
    df["Time_sec"],
    df["Total Average Response Time"],
    linewidth=2
)

# Labels and title (IMPORTANT)
plt.xlabel("Time (seconds)")
plt.ylabel("Average Response Time (ms)")
plt.title("Average Response Time vs Time")

# Grid for readability
plt.grid(True)

# Show plot
plt.show()
