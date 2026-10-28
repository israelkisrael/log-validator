


def validate_log_line(log_entry: str) -> bool:

    """ Returns True if the log entry does not contain any error keywords, otherwise returns False. """
    error_keywords = ["error", "fail", "failed", "exception", "critical", "timeout"]

    lower_line = log_entry.lower() 

    for keyword in error_keywords:
        if keyword in lower_line:
            return False
        pass

    return True


def validate_log_file(log_file_path: str)  -> dict:
    """ Validate the file results and return a dictionary with the validation results. """

    validate_results = {
        "errors_found": 0,
        "valid_lines": 0,
        "line_count": 0
    }

    try:
        with open(log_file_path, 'r') as log_file:
            for line in log_file:
                validate_results["line_count"] += 1
                if validate_log_line(line):
                    validate_results["valid_lines"] += 1
                else: 
                    validate_results["errors_found"] += 1
    except FileNotFoundError:
        print(f"Error: The file '{log_file_path}'was not found.")
    except Exception as e:
        print(f"An error occurred while validating the log file: {e}")

    return validate_results 

def get_text_file_validation_summary(log_file_summary_dict: dict)  -> str:
    """ Returns a text file validation summary based on the validation reports. """

    file_path = "validation_summary_file.txt"
    with open(file_path , 'w') as summary_file:
        summary_file.write(f"==========Log File Validation Summary==========\n")
        summary_file.write(f"Total Lines Processed: {log_file_summary_dict['line_count']}\n")
        summary_file.write(f"Valid Lines: {log_file_summary_dict['valid_lines']}\n")
        summary_file.write(f"Error Lines: {log_file_summary_dict['errors_found']}\n")

    return file_path