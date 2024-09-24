import random

# Function to simulate coin tosses and calculate probabilities
def coin_toss_simulator(tosses):
    outcomes = {"Heads": 0, "Tails": 0}

    # Simulate tossing the coin the specified number of times
    for _ in range(tosses):
        outcome = random.choice(["Heads", "Tails"])
        outcomes[outcome] += 1

    # Print the results
    print("Outcome\tFrequency\tProbability")
    for outcome, count in outcomes.items():
        probability = count / tosses
        print(f"{outcome}\t{count}\t\t{probability:.2f}")

# Main function to ask for user input and run the simulation
def main():
    tosses = int(input("Enter the number of coin tosses: "))
    coin_toss_simulator(tosses)

if __name__ == "__main__":
    main()