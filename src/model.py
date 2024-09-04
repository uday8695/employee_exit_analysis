# model.py

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import preprocess

def train_and_evaluate_model(file_path):
    X_train, X_test, y_train, y_test = preprocess.load_and_preprocess_data(file_path)

    # Initialize and train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Make predictions
    y_pred = model.predict(X_test)

    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    classification_rep = classification_report(y_test, y_pred)

    # Output the accuracy and classification report
    print(f'Accuracy: {accuracy:.4f}')
    print('Classification Report:')
    print(classification_rep)

# Example usage
if __name__ == "__main__":
    file_path = r'D:\23A55A4405\employee_exit_analysis\data\HR_comma_sep.csv'
    train_and_evaluate_model(file_path)
