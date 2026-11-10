# Engineering_student_placement_analyser
Analysing how placement depends on certain factors and predicting it through logistic regression.
## Project Objective 
Analysing how placement depends on certain factors like CGPA , number of internships , history of backlogs and stream. The project uses logistic regression to estimate the probability that a person will be placed based on these factors.
## Team and Roles
| Member | Entry No. | Role |
|---|---|---|
| Tashvi Garg | 2026MCB1577 |  Documentation lead |
| Arjun Solanki | 2026EEB1325 |  Execution lead |
| Rishabh Rajput | 2026DAB1305 | PPT lead |
| Shreyansh | 2026AIB1080 | Video lead |
## Project Structure
```text
student_placement_analyser/
├── .gitattributes
├── .gitignore
├── backlog_placement.png
├── backlog_summary.csv
├── data_checking_and_comparisons.ipynb
├── Model Evaluator.ipynb
├── placement_model.ipynb
├── placement_model.joblib
├── placement_predictions.csv
├── placements.csv
├── README.md
├── requirements_member1.txt
├── requirements_member2.txt
├── requirements_member3.txt
├── stream_and_backlogs.ipynb
├── stream_placement.png
└── stream_summary.csv
```
## Setup Instructions
- **Python Version:** 3.14.6
- **Required Libraries:** All required libraries and their versions are listed in `requirements.txt`.

To install the required dependencies, run the following command in the project directory:

```bash
python -m pip install -r requirements.txt
```
## Steps to Run
1. Clone or download the project repository from GitHub.
2. Open the project folder in Visual Studio Code (VS Code).
3. Open the notebooks in the following order:
   - `data_checking_and_comparisons.ipynb`
   - `stream_and_backlogs.ipynb`
   - `placement_model.ipynb`
   - `Model Evaluator.ipynb`
4. Select the appropriate Python kernel (Python 3.14.6) in VS Code if prompted.
5. Open each notebook and click **Run All** to execute all its cells.
## Expected Output
- **Data Checking and Comparisons:** Displays missing-value and duplicate checks, overall placement percentage, and comparisons of placement percentages across CGPA values and internship counts using tables and graphs.
- **Stream and Backlogs Analysis:** Displays placement comparisons across different engineering streams and backlog categories using summary tables and graphs.
- **Placement Prediction Model:** Trains a Logistic Regression model using student-related factors and generates placement predictions.
- **Model Evaluation:** Displays the model's performance through accuracy, confusion matrix, classification report, and visualisations.
