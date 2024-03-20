import os
import pandas as pd

# Function to read data from folder
def read_data_from_folder(folder_path):
    files = os.listdir(folder_path)
    df_list = []
    for file in files:
        if file.endswith('.dat'): 
            file_path = os.path.join(folder_path, file)
            df = pd.read_csv(file_path, delimiter='\t')
            df_list.append(df)
    return pd.concat(df_list, ignore_index=True)

# Function to calculate gross salary
def calculate_gross_salary(df):
    df['Gross Salary'] = df['basic_salary'] + df['allowances']
    return df

# Function to write data to CSV with footer
def write_to_csv(df, output_path):
    df = df.drop_duplicates()
    df.to_csv(output_path, index=False)
    second_highest_salary = df["Gross Salary"].nlargest(2).iloc[-1]
    average_salary = df["Gross Salary"].mean()

    with open(output_path, 'a') as f:
        f.write('\n') 
        f.write(f'Second Highest Salary={second_highest_salary}, ') 
        f.write(f'Average Salary={average_salary}') 

    
# Main function
def main(input_folder, output_folder):
    df = read_data_from_folder(input_folder)
    
    df = calculate_gross_salary(df)
    
    output_file = os.path.join(output_folder, 'RESULT.csv')
    write_to_csv(df, output_file)

if __name__ == "__main__":
    input_folder = r"File_Handler\Input_Data"  
    output_folder = r"File_Handler\Output_Data" 
    main(input_folder, output_folder)
