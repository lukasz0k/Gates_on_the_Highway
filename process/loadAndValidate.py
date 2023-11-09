import os

class LoadInputsData:
    def loadLogs(self, file_path):
        # Verify the file extension is .txt
        if not file_path.lower().endswith('.txt'):
            raise ValueError("File is not a .txt format")
        
        # Check if the file is empty
        if os.stat(file_path).st_size == 0:
            raise ValueError("File is empty")

        # Try to open and read the file
        try:
            with open(file_path, 'r') as file:
                for line_number, line in enumerate(file, start=1):
                    if not line.strip():  # Skip empty lines
                        continue
                    columns = line.split()  # Assuming whitespace delimiter

                    if len(columns) < 4:  # Check if there are at least 4 columns
                        raise ValueError(f"Line {line_number}: Not enough columns")
                    
                for line_number, line in enumerate(file, start=1):
                    columns = line.split()  # Assuming whitespace delimiter
                    
                    # Verify the first column is a float
                    try:
                        float(columns[0])
                    except ValueError:
                        raise ValueError(f"Line {line_number}: First column is not a float")

                    # Verify the rest of the columns are text
                    for col in columns[1:]:
                        if not col.isalpha():
                            raise ValueError(f"Line {line_number}: Column is not text")

                    # Verify the third column is one of the specified values
                    if columns[2] not in ["240W", "250W", "260W", "270W", "270E", "260E", "250E", "240E"]:
                        raise ValueError(f"Line {line_number}: Third column has invalid value")

                    # Verify the fourth column is one of the specified values
                    if columns[3] not in ["ENTRY", "ON ROAD", "EXIT"]:
                        raise ValueError(f"Line {line_number}: Fourth column has invalid value")

        except FileNotFoundError:
            raise FileNotFoundError("File does not exist")
        
        except Exception as e:
            # Handle any other exception that might occur
            raise e

        return True  # Or the data, depending on requirements
    
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