# House-price-prediction
This project involves predicting the price of a house based on various features using a machine learning  model - Linear Regression.
## Project Workflow
The objectives of this project is to predict house price using features such as area, number of bedrooms, bathrooms,furnishing status, and more. The steps involved are:
**Loading and exploring** the dataset.
**Data preprocessing** - including encoding categorical variables.
**Splitting** the dataset into traing and testing sets.
**Training** a Linear Regression model on the training data.
**Evaluating** the model using R2 Score.
**Visualizing** the comparison between actual and predicted values.
**saving the results** for manual analysis.

## 📊 Dataset

- The dataset contains 13 features including:
  - `price`, `area`, `bedrooms`, `bathrooms`, `stories`, `parking`, etc.
  - Categorical features like `mainroad`, `guestroom`, `basement`, `furnishingstatus` are converted using one-hot encoding.

- Total entries: 545

## 🧠 Machine Learning Model

- **Model Used**: Linear Regression (from `sklearn`)
- **Performance Metric**: R² Score
- **Result**: R² score ≈ 0.65

## 📈 Visualization

- A scatter plot is used to compare **actual vs predicted** house prices.
- Red 'x' points show actual prices, blue 'o' points show predicted prices.

## 🛠️ Libraries Used

- pandas
- numpy
- sklearn
- matplotlib
- seaborn

## 🔍 Future Improvements

- Try other models like Random Forest, Decision Tree, or Gradient Boosting.
- Improve preprocessing (outlier removal, feature scaling).
- Perform hyperparameter tuning.

## 📁 Files

- `Housing.csv`: Input dataset
- `main.py`: Code file
- `predicted_vs_actual.csv`: (Optional) comparison output
- `README.md`: Project documentation

---

Feel free to use this README. If you want, I can format it into a `.md` file so you can upload it directly. Would you like that?
