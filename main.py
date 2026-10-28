import argparse

from validator import validate_log_file ,get_text_file_validation_summary

def main():

    parser  = argparse.ArgumentParser(description="A professional modular CLI tool for log file validation.")
    parser.add_argument(
        "log_file",
        nargs="?",
        default="sample.log",
        help="Path to the log file you want to validate."
    )
    args = parser.parse_args()
    
    print("=== Log Validator Tool Started ===")

    print(f"Reading and validating log file: {args.log_file}...")

    try:
        summary_results = validate_log_file(args.log_file)

    except FileNotFoundError:
        print(f"\n[Error]: The file '{args.log_file}' was not found.")
        print("-> Please make sure the file exists in the folder,")
        print("-> Or provide the correct file name as an argument like this:")
        print(f"   python main.py <your_file_name.log>")
        print("-> Run with --help for more details.\n")
        return

    except IsADirectoryError:
        print(f"\n[Error]: The file '{args.log_file}' is a directory.")
        return

    except PermissionError:
        print(f"\n[Error]: Permission denied!")
        print(f"-> You don't have read permissions for '{args.log_file}'.\n")
        return
    
    except Exception as e:
        print(f"\n[Error]: An unexpected error occurred: {e}\n")
        return
    
    report_path = get_text_file_validation_summary(summary_results)

    print("--- Reading report content from disk: ---\n")

    with open(report_path, 'r') as f:
        content = f.read()
        print(content)
        print(f"Report successfully saved to: {report_path}\n")

if __name__ == "__main__":
    main()