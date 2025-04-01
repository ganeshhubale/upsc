# UPSC Exam Score Calculator

A simple command-line calculator for GS and CSAT exam scores.

## Features

- Calculate scores for GS and CSAT papers based on correct answers and attempted questions.
- Easy to use from the command line.

## Installation Guide

Follow these steps to install the `upsc` package locally:

### Prerequisites

- Ensure you have Python 3.6 or higher installed on your system. You can check your Python version by running:
  
  ```bash
  python3 --version
  ```

### Step 1: Clone the Repository

If you haven't already, clone the repository containing the package code. You can do this using git:

```bash
git clone https://github.com/ganeshhubale/exam_score_calculator.git
cd upsc
```

### Step 2: Install the Package

Open your terminal and navigate to the root directory of the package (the directory containing `setup.py`).

```bash
cd path/to/upsc
```

Install the package using pip:

```bash
pip install .
```

The `.` indicates that you want to install the package from the current directory.

### Step 3: Verify the Installation

After the installation is complete, you can verify that the package is installed by running:

```bash
pip list
```

Look for `upsc` in the list of installed packages.

### Step 4: Run the Package

Once the package is installed, you can run the calculator from the command line using the following command:

```bash
upsc
```

This will launch the UPSC Exam Score Calculator, and you can interact with it as intended.

## Usage

When you run the command, you will be prompted to enter the number of correct answers and attempted questions for both the GS and CSAT papers. The program will then calculate and display the total scores.

### Example Interaction

```
Welcome to the Exam Score Calculator
======================================
GS Paper Score Calculation
===========================
Enter the number of correct answers for GS: 80
Enter the number of attempted questions for GS: 100
Total GS Score: 153.34
===========================
CSAT Paper Score Calculation
===========================
Enter the number of correct answers for CSAT: 70
Enter the number of attempted questions for CSAT: 80
Total CSAT Score: 157.00
===========================
Thank you for using the Exam Score Calculator!
```

