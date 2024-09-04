{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "e3b2c4a8-a833-498d-81b4-5e07b43bf1a9",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'preprocess'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[5], line 5\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01msklearn\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mensemble\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m RandomForestClassifier\n\u001b[0;32m      4\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01msklearn\u001b[39;00m\u001b[38;5;21;01m.\u001b[39;00m\u001b[38;5;21;01mmetrics\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m classification_report, accuracy_score\n\u001b[1;32m----> 5\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mpreprocess\u001b[39;00m\n\u001b[0;32m      7\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mtrain_and_evaluate_model\u001b[39m(file_path):\n\u001b[0;32m      8\u001b[0m     X_train, X_test, y_train, y_test \u001b[38;5;241m=\u001b[39m preprocess\u001b[38;5;241m.\u001b[39mload_and_preprocess_data(file_path)\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'preprocess'"
     ]
    }
   ],
   "source": [
    "# model.py\n",
    "\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.metrics import classification_report, accuracy_score\n",
    "import preprocess\n",
    "\n",
    "def train_and_evaluate_model(file_path):\n",
    "    X_train, X_test, y_train, y_test = preprocess.load_and_preprocess_data(file_path)\n",
    "\n",
    "    # Initialize and train the model\n",
    "    model = RandomForestClassifier(n_estimators=100, random_state=42)\n",
    "    model.fit(X_train, y_train)\n",
    "\n",
    "    # Make predictions\n",
    "    y_pred = model.predict(X_test)\n",
    "\n",
    "    # Evaluate the model\n",
    "    accuracy = accuracy_score(y_test, y_pred)\n",
    "    classification_rep = classification_report(y_test, y_pred)\n",
    "\n",
    "    # Output the accuracy and classification report\n",
    "    print(f'Accuracy: {accuracy:.4f}')\n",
    "    print('Classification Report:')\n",
    "    print(classification_rep)\n",
    "\n",
    "# Example usage\n",
    "if __name__ == \"__main__\":\n",
    "    file_path =r'D:\\23A55A4405\\employee_exit_analysis\\data\\HR_comma_sep.csv'\n",
    "    train_and_evaluate_model(file_path)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9a8c8929-5896-409a-a8a9-86aa5c9e8242",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
