import matplotlib.pyplot as plt

# Data for charm hadrons (name, quark composition, lifetime in fs)
charm_hadrons = [
    ("D+", "c d̄", 1040.0),
    ("D-", "c̄ d ", 1040.0),
    ("D0", "c ū", 410.1),
    ("Dbar0", "c̄ u", 410.1),
    ("D_s+", "c s̄", 500.0),
    ("D_s-", "c̄ s", 500.0),
    ("Λ_c+", "c u d", 200.0),
    ("Ξ_c+", "c s u", 442.0),
    ("Ξ_c0", "c s d", 112.0),
    ("Ω_c0", "c s s", 69.0),
    
]
# Extract names, quark composition, and lifetimes for pie chart labels and sizes
hadron_names = [hadron[0] for hadron in charm_hadrons]
quark_compositions = [hadron[1] for hadron in charm_hadrons]
hadron_lifetimes = [hadron[2] for hadron in charm_hadrons]
areas = [lifetime / max(hadron_lifetimes)  for lifetime in hadron_lifetimes]
# Create pie charts
fig, axs = plt.subplots(2, 5, figsize=(12, 6))
fig.suptitle("Charm Hadrons Quark Composition and Lifetime", fontsize=16)

for i, ax in enumerate(axs.flatten()):
    if i < len(hadron_names):
        quarks = quark_compositions[i].split()
        quark_numbers = len(quarks)
        if quark_numbers == 2:
            quark_percentages = [0.5,0.5]
            ax.pie(quark_percentages, labels=quarks,  startangle=90, radius=areas[i])
        if quark_numbers == 3:
            quark_percentages = [1/3,1/3,1/3]
            ax.pie(quark_percentages, labels=quarks, startangle=90, radius=areas[i])
        ax.set_title(hadron_names[i] + f" ({hadron_lifetimes[i]} fs)\n area = {round(areas[i],2)} ")

# Adjust spacing for subplots
plt.tight_layout()
plt.subplots_adjust(top=0.85)

# Save the plot to a file or display it
plt.savefig("charm_hadrons.png")
# The plot can be displayed by uncommenting the next line:
# plt.show()
