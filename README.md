# 🧠 Student Mental Health Dashboard

This project is an interactive Streamlit dashboard built using a dataset about students' mental health. It helps visualize how factors like age, year of study, CGPA, and gender are associated with depression, anxiety, and panic attacks.

## 📊 Features

- Filter by Age, Year of Study, Gender
- Visualize Depression, Anxiety, Panic Attacks
- Bar charts and pie charts using Seaborn and Matplotlib
- Cleaned dataset using Jupyter Notebook

## 🧹 Data Cleaning

The raw dataset contained:
- Extra spaces in column names and not precised column names
- Year of study values with gender info (e.g., "Year 2 (Female)")


All cleaning steps are done in [`data_cleaning.ipynb`](data_cleaning.ipynb).

## 📂 Dataset

- Source: [Student Mental Health Dataset](https://raw.githubusercontent.com/Harsha125-art/public-datasets/main/student_mental_health.csv)
- 200+ entries with information like:
  - `Age`, `Gender`, `CGPA`
  - `Depression`, `Anxiety`, `Panic_attack`
  - `Seeking_Help`, `Course`, `Year_of_Study`

## 🛠 Technologies Used

- Python
- Streamlit
- Pandas
- Seaborn / Matplotlib
- Jupyter Notebook

## 🚀 How to Run

```bash
pip install streamlit pandas seaborn matplotlib
streamlit run dashboard.py
