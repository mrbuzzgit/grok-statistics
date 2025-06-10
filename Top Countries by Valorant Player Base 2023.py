import matplotlib.pyplot as plt

# Data
countries = ['United States', 'Brazil', 'Turkey', 'Philippines', 'Indonesia']
players = [5.88, 1.68, 1.53, 1.43, 1.00]  # Estimated MAUs in millions

# Create bar chart
plt.figure(figsize=(10, 6))
plt.bar(countries, players, color='orange')

# Add labels and title
plt.xlabel('Country')
plt.ylabel('Estimated Monthly Active Players (Millions)')
plt.title('Top 5 Countries by Valorant Players (2023 Estimates)')
plt.ylim(0, 7)  # Set y-axis limit for better visualization

# Add value labels on top of bars
for i, v in enumerate(players):
    plt.text(i, v + 0.1, f'{v}M', ha='center', fontweight='bold')

# Display the chart
plt.tight_layout()
plt.show()