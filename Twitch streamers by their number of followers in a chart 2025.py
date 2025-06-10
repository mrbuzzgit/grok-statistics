import matplotlib.pyplot as plt

# Data
streamers = ["Ninja", "KaiCenat", "Ibai", "auronplay", "Rubius", "TheGrefg", "xQc", "Tfue", "shroud", "elmarianaa"]
followers = [19.2, 17.9, 17.2, 16.8, 15.8, 12.2, 12.1, 11.3, 11.1, 10.4]  # in millions

# Create bar chart
plt.figure(figsize=(10, 6))
bars = plt.bar(streamers, followers, color=['#FF5555', '#55FF55', '#5555FF', '#FFFF55', '#FF55FF',
                                          '#55FFFF', '#FFAA55', '#55AAFF', '#AA55FF', '#FF5555'])

# Customize chart
plt.title('Top 10 Twitch Streamers by Followers (June 2025)')
plt.xlabel('Twitch Streamers')
plt.ylabel('Followers (Millions)')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height, f'{height}',
             ha='center', va='bottom')

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Show plot
plt.show()