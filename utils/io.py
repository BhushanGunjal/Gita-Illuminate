import pandas as pd

def load_raw_data(file_path):
    """
    Loads the raw data from a CSV or Excel file.
    :param file_path: Path to the raw data file (CSV or Excel).
    :return: Loaded DataFrame.
    """
    # Handle different file types
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path)
    elif file_path.endswith(".xlsx") or file_path.endswith(".xls"):
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a CSV or Excel file.")

def save_processed_data(data, file_path):
    """
    Saves the processed dataset to a file.
    :param data: The DataFrame to save.
    :param file_path: Path to the output file.
    """
    # Save the processed data as a pickle file
    data.to_pickle(file_path)
