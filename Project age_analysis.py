import pandas as pd

# Load data from CSV file
def load_data(filepath):
    try:
        data = pd.read_csv(filepath)
        return data
    except FileNotFoundError:
        print("Error: The data file was not found.")
        return None

# Calculate statistics
def calculate_statistics(data):
    avg_age = data['Age'].mean()
    max_age = data['Age'].max()
    min_age = data['Age'].min()
    return avg_age, max_age, min_age

# Main function to run the analysis
def main():
    data = load_data('../data/ages.csv')
    if data is not None:
        avg_age, max_age, min_age = calculate_statistics(data)
        print(f"Average Age: {avg_age}")
        print(f"Maximum Age: {max_age}")
        print(f"Minimum Age: {min_age}")

if __name__ == "__main__":
    main()
