{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "a26d7808-dc81-46e8-9acc-8ca60988dc01",
   "metadata": {},
   "outputs": [],
   "source": [
    "# preprocess.py\n",
    "\n",
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "\n",
    "def load_and_preprocess_data(file_path):\n",
    "    df = pd.read_csv(r'D:\\23A55A4405\\employee_exit_analysis\\data\\HR_comma_sep.csv')\n",
    "\n",
    "    # Encode categorical variables\n",
    "    label_encoder = LabelEncoder()\n",
    "    df['salary'] = label_encoder.fit_transform(df['salary'])\n",
    "    df['Department'] = label_encoder.fit_transform(df['Department'])\n",
    "\n",
    "    # Define features and target variable\n",
    "    X = df.drop('left', axis=1)\n",
    "    y = df['left']\n",
    "\n",
    "    # Split the data into training and testing sets\n",
    "    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)\n",
    "\n",
    "    return X_train, X_test, y_train, y_test\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "af6d8a9e-f2f4-45c4-9902-64daea85d5d1",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5428c30f-720d-4eec-b6e9-bd99c51167b2",
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
