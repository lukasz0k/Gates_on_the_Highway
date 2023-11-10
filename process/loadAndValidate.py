import os

class LoadInputsData:
    def loadLogs(self, file_path):
        # Check if file exists
        if not os.path.exists(file_path):
            return "File not found"

        # Check if the file extension is .txt
        if not file_path.lower().endswith('.txt'):
            return "File is not a .txt format"

        # Check if the file is empty
        if os.stat(file_path).st_size == 0:
            return "File is empty, no logs loaded"

        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()

                if not lines:
                    return "File is empty, no logs loaded"

                for line_number, line in enumerate(lines, start=1):
                    columns = line.strip().split()

                    if len(columns) < 4:
                        return f"Invalid data in file, file need to have 4 columns"

                    # Check first column is a float
                    try:
                        float(columns[0])
                    except ValueError:
                        return f"Invalid data format, first column must be a number"

                    # Check remaining columns are text
                    for i, col in enumerate(columns[1:], start=2):
                        if not col.isalpha():
                            return f"Invalid data format, column {i} must be a text"

                    # Specific value checks for columns 3 and 4
                    if columns[2] not in ["240W", "250W", "260W", "270W", "270E", "260E", "250E", "240E"]:
                        return "Third column has invalid value"
                    if columns[3] not in ["ENTRY", "ON ROAD", "EXIT"]:
                        return "Fourth column has invalid value"

        except FileNotFoundError:
            return "File not found"
        except Exception as e:
            # Generic catch-all for any other exception
            return f"An error occurred: {e}"

        return "File loaded"  # Return this message if all checks pass
    
    def loadThreads(self, file_path):
        # Check if the file extension is .txt or .csv
        if not (file_path.lower().endswith('.txt') or file_path.lower().endswith('.csv')):
            raise ValueError("File is not a .txt or .csv format")

        # Check if the file is empty
        if os.stat(file_path).st_size == 0:
            raise ValueError("File is empty")

        threads = {}
        try:
            with open(file_path, 'r') as file:
                for line_number, line in enumerate(file, start=1):
                    if not line.strip():  # Skip empty lines
                        continue

                    if file_path.lower().endswith('.csv'):
                        # Split the line into columns for CSV
                        columns = line.strip().split(',')
                        if len(columns) != 2:
                            raise ValueError(f"Line {line_number}: Incorrect number of columns")
                        vehicle, owner = columns
                    else:
                        # Split the line by ':' for TXT
                        parts = line.strip().split(':')
                        if len(parts) != 2:
                            raise ValueError(f"Line {line_number}: Incorrect format, expected vehicle:owner")
                        vehicle, owner = parts

                    # Check that both vehicle and owner are strings
                    if not isinstance(vehicle, str) or not isinstance(owner, str):
                        raise ValueError(f"Line {line_number}: Vehicle and Owner values must be strings")

                    # Check if vehicle is already used as a key, ensuring uniqueness
                    if vehicle in threads:
                        raise ValueError(f"Line {line_number}: Duplicate vehicle entry found")
                    
                    threads[vehicle] = owner

        except FileNotFoundError:
            raise FileNotFoundError("File does not exist")
        except Exception as e:
            # Handle any other exception that might occur
            raise e

        return threads  # Return the dictionary of threads