# student_placement_analyser
Analysing how placement depends on certain factors and predicting it through logistic regression.
## Project Objective 
Analysing how placement depends on certain factors like CGPA , number of internships , history of backlogs and stream. The project uses logistic regression to estimate the probability that a person will be placed based on these factors.
## Dataset
- **Dataset:** Engineering Placements Prediction
- **Source:** [Kaggle – Engineering Placements Prediction](https://www.kaggle.com/datasets/tejashvi14/engineering-placements-prediction)
- **File used:** `placements.csv`
## Team and Roles
| Member | Entry No. | Role |
|---|---|---|
| Tashvi Garg | 2026MCB1577 |  Documentation lead |
| Arjun Solanki | 2026EEB1325 |  Execution lead |
| Rishabh Rajput | 2026DAB1305 | PPT lead |
| Shreyansh | 2026AIB1080 | Video lead |
## Team Contributions

### Member 1 — Data Analysis and Documentation

- Checked the dataset for missing values and duplicate records. No missing values were found, while 1,829 duplicate rows were identified out of 2,966 total records.
- Calculated the overall placement percentage: 659 out of 1,137 unique student records were placed, resulting in an overall placement percentage of 57.96%.
- Compared placement percentages across different CGPA values. Students with CGPA 8 and 9 had the highest placement percentage of 100%, while students with CGPA 5 had the lowest at 6.58%.
- Compared placement percentages across internship counts. Students with two internships had the highest placement percentage (75.81%), followed by one internship (54.45%) and zero internships (52.13%).
- Created summary tables and visualizations using pandas and matplotlib to present the findings.
- Led the README documentation, including project introduction, team details, dataset source, setup instructions and execution steps.

### Member 2 — Stream and Backlog Analysis
- Compared placement percentages across six engineering streams and between students with and without backlog history.
- Calculated the total number of students, placed students and placement percentage for each category.
- Found that Electronics and Communication and Information Technology had the highest placement percentage (59.2%), while Civil had the lowest (46.1%).
- Observed that students without backlog history had a placement percentage of 55.8%, compared to 53.0% for students with backlog history.
- Repeated both comparisons using unique rows only, since 1,829 out of 2,966 records were repeated. The overall patterns remained unchanged.
- Created summary tables (`stream_summary.csv`, `backlog_summary.csv`) and bar graphs (`stream_placement.png`, `backlog_placement.png`).
- Documented the analysis in `stream_and_backlogs.ipynb`.
- Prepared the five-slide project presentation as the PPT lead.

### Member 3 — Placement Prediction Model
- Used seven student attributes: age, gender, engineering stream, internships, CGPA, hostel status and backlog history to predict placement.
- Split the data into training (2,390 records) and testing (576 records), keeping matching student details together.
- Applied categorical encoding and numerical scaling, learning the preprocessing rules only from the training data.
- Trained a Logistic Regression model using the training data.
- Generated placement predictions for the test data (0 = Not Placed, 1 = Placed).
- Saved actual and predicted placement values in `placement_predictions.csv` for evaluation.
- Saved the trained model and preprocessing tools for reuse.

### Member 4 — Model Evaluation
- Developed evaluation code to compare actual and predicted placement values using CSV files.
- Calculated accuracy, precision, recall and F1-score using Scikit-learn.
- Compared the model's evaluation metrics with a baseline based on the most frequent actual placement value.
- Generated a confusion matrix showing True Positives (TP), False Positives (FP), True Negatives (TN) and False Negatives (FN).
  
## Project Structure
```text
student_placement_analyser/
│
├── .gitattributes
├── .gitignore
├── README.md
├── requirements.txt
│
├── placements.csv
│
├── data_checking_and_comparisons.ipynb
├── stream_and_backlogs.ipynb
├── placement_model.ipynb
├── Model Evaluator.ipynb
│
├── placement_model.joblib
├── placement_predictions.csv
│
├── stream_summary.csv
├── backlog_summary.csv
│
├── stream_placement.png
└── backlog_placement.png
```

### File Descriptions

- **placements.csv:** Dataset used for placement analysis.
- **data_checking_and_comparisons.ipynb:** Data checking and CGPA/internship analysis.
- **stream_and_backlogs.ipynb:** Placement analysis across engineering streams and backlog history.
- **placement_model.ipynb:** Logistic Regression model for placement prediction.
- **Model Evaluator.ipynb:** Evaluation of model predictions.
- **placement_model.joblib:** Saved trained model.
- **placement_predictions.csv:** Actual and predicted placement results.
- **stream_summary.csv / backlog_summary.csv:** Summary tables.
- **stream_placement.png / backlog_placement.png:** Placement analysis graphs.
- **requirements.txt:** Required Python libraries and versions.

## Setup  prerequisites
- **Python Version:** 3.14.6
- **Required Libraries:** All required libraries and their versions are listed in `requirements.txt`.
## Steps to Run
1. Download or clone the repository.
2. Open the project folder in VS Code.
3. Install the Python and Jupyter extensions in VS Code.
4. Open a terminal in the project folder and run:
   python -m pip install -r requirements.txt
5. Open a notebook and select the Python environment where you installed those libraries.
6. Click Run All in each notebook, in this order:
   - `data_checking_and_comparisons.ipynb`
   - `stream_and_backlogs.ipynb`
   - `placement_model.ipynb`
   - `Model Evaluator.ipynb`
## Expected Output
- **Data Checking and Comparisons:** Displays missing-value and duplicate checks, overall placement percentage, and comparisons of placement percentages across CGPA values and internship counts using tables and graphs.
- **Stream and Backlogs Analysis:** Displays placement comparisons across different engineering streams and backlog categories using summary tables and graphs.
- **Placement Prediction Model:** Trains a Logistic Regression model using student-related factors and generates placement predictions.
- **Model Evaluation:** Displays the model's performance through accuracy, confusion matrix, classification report, and visualisations.
## AI Use Disclosure
- **Member 1:** ChatGPT was used in organising readme structure ,  code and debugging
- **Member 2:** Claude was used to assist with drafting presentation slides and resolving minor coding errors. All results were checked and verified.
- **Member 3:** ChatGPT was used for coding assistance, explanations and debugging.
- **Member 4:** AI assistance was limited to understanding coding syntax.
