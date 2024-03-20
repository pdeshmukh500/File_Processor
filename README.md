# CSV Data Processing Script
This Python script is designed to read data from multiple .dat files located in a specified folder, process the data, and generate a CSV file 
with additional calculations and a footer containing summary statistics.

## Usage
1. Ensure you have Python installed on your system.
2. Install the required dependencies using the following command:
     'pip install pandas'
3. Place your .dat files in the input folder.
4. Run the script by executing the following command:
    'python script.py'
5. Once the script finishes execution, you will find the output CSV file with the processed data in the output folder.

## Script Details
- `script.py`: This is the main Python script that performs the data processing.
- `input_folder`: This folder contains the input .dat files.
- `output_folder`: This folder stores the output CSV file with processed data.
- `read_data_from_folder()`: Function to read data from .dat files in the input folder.
- `calculate_gross_salary()`: Function to calculate gross salary based on basic salary and allowances.
- `write_to_csv()`: Function to write processed data to a CSV file with footer containing summary statistics.

## Dependencies
- Python 3.x
- pandas

## Author
  Priyanka Deshmukh

