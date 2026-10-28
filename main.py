from validator import validate_log_file ,get_text_file_validation_summary

def main():
    print("=== Log Validator Tool Started ===")

    log_filename = "sample.log"

    print(f"Reading and validating log file: {log_filename}...")

    summary_results = validate_log_file(log_filename)

    report_path = get_text_file_validation_summary(summary_results)

    print("--- Reading report content from disk: ---\n")

    with open(report_path, 'r') as f:
        content = f.read()
        print(content)
        print(f"Report successfully saved to: {report_path}\n")

if __name__ == "__main__":
    main()