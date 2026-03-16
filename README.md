# Quantium starter repo
## Pink Morsel Sales Dashboard

An interactive sales dashboard built with Python to analyze the impact of a price increase on **Pink Morsel** sales.

This project was developed as part of the **Quantium Data Analytics Job Simulation** and demonstrates a full workflow including **data processing, visualization, testing, and automation**.

---

## Project Overview

Soul Foods wanted to answer the following business question:

> Were sales higher before or after the Pink Morsel price increase on **15 January 2021**?

To answer this question, the project performs the following steps:

1. Process raw transaction data from multiple CSV files
2. Clean and structure the dataset
3. Build an interactive dashboard to visualize sales trends
4. Allow filtering by region
5. Implement automated tests for the dashboard
6. Automate test execution using a shell script

The dashboard clearly shows that **sales increased after January 2021**.

---

## Dashboard Preview

The dashboard visualizes **Pink Morsel sales over time** and allows filtering by region.

---

## Technologies Used

- Python
- Pandas
- Dash
- Plotly
- Pytest
- CSS
- Shell scripting
- Virtual environments

---

## Project Structure

```
quantium-starter-repo
│
├── data/                 # Raw CSV files
├── process_data.py       # Data processing script
├── output_data.csv       # Processed dataset
├── app.py                # Dash dashboard application
├── run_tests.sh          # Script to run automated tests
├── tests/
│   └── test_app.py       # Dashboard test suite
└── README.md
```

---

## Data Processing

The script `process_data.py` performs the following steps:

- Combines multiple CSV files
- Filters only **Pink Morsel** products
- Converts price values to numeric format
- Calculates total sales

```
Sales = Quantity × Price
```

The final dataset contains the following columns:

```
Sales
Date
Region
```

---

## Dashboard Features

The dashboard includes:

- Sales trend visualization
- Region filtering using radio buttons
- Interactive line chart
- Clean and simple UI

Users can filter the data by selecting:

```
All
North
South
East
West
```

---

## Running the Dashboard

Activate the virtual environment:

```
source myenv/Scripts/activate
```

Run the Dash application:

```
python app.py
```

Open the dashboard in your browser:

```
http://127.0.0.1:8050
```

---

## Running Tests

Execute the test suite using:

```
pytest
```

The tests verify:

- The dashboard header exists
- The visualization is displayed
- The region picker is present

---

## Automated Test Script

The project includes a script to automate running the tests.

Run the script using:

```
bash run_tests.sh
```

The script:

1. Activates the virtual environment
2. Runs the test suite
3. Returns exit code `0` if tests pass

---

## Key Insight

The visualization shows that:

**Sales increased significantly after the Pink Morsel price increase on January 15, 2021.**

This suggests the price increase **did not negatively impact demand**.

---

## Skills Demonstrated

This project demonstrates skills in:

- Data cleaning and processing
- Data visualization
- Interactive dashboard development
- Automated testing
- Test automation
- Python project organization

---

## Author

Developed as part of the **Quantium Data Analytics Virtual Experience Program**.
