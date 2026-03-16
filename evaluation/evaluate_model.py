import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score

def evaluate_model(predictions, actual):
    cm = confusion_matrix(actual, predictions)
    accuracy = accuracy_score(actual, predictions)
    print(pd.DataFrame(cm))
    return accuracy

def main():
    # Example usage
    predictions = [0, 1, 0, 1]
    actual = [0, 1, 1, 0]
    accuracy = evaluate_model(predictions, actual)
    print(f"Accuracy: {accuracy}")

if __name__ == "__main__":
    main()
