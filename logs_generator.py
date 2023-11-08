import random
import string
import argparse

def generate_vehicle_key():
    return f"{random.choice(string.ascii_uppercase)}" \
           f"{random.choice(string.ascii_uppercase)}" \
           f"{random.choice(string.ascii_uppercase)}" \
           f"{str(random.randint(0, 9999)).zfill(4)}" \
           f"{random.choice(string.ascii_uppercase)}" \
           f"{random.choice(string.ascii_uppercase)}"

def generate_logs(number_of_cars, number_of_logs, output_file, max_interval):
    tolls = {
        'W': [240, 250, 260, 270],
        'E': [270, 260, 250, 240]
    }
    status = ['ENTRY', 'ON ROAD', 'ON ROAD', 'EXIT']
    time_diffs = [240, 300, 420]
    last_entry_time = 0

    # Initialize car information
    cars_info = {generate_vehicle_key(): 0 for _ in range(number_of_cars)}
    logs = []

    while len(logs) < number_of_logs:
        car, last_time = random.choice(list(cars_info.items()))

        # Ensure the next car enters within max_interval seconds
        entry_time = max(last_time, last_entry_time + random.randint(1, max_interval))
        base_time = entry_time
        last_entry_time = entry_time

        direction = random.choice(['W', 'E'])
        toll_order = tolls[direction]

        for i, toll in enumerate(toll_order):
            if len(logs) >= number_of_logs:
                break  # Break the loop if we have generated the required number of logs

            if i > 0:
                base_time += random.randint(time_diffs[i - 1], time_diffs[i - 1] + 600)
            log_entry = f"{base_time}, {car}, {toll}{direction}, {status[i]}"
            logs.append(log_entry)
            if status[i] == 'EXIT':
                # Once a car exits, it cannot re-enter for 1000s
                cars_info[car] = base_time + 1000
                break

    # Save logs to the output file
    with open(output_file, 'w') as file:
        for log in logs:
            file.write(log + '\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate toll booth logs and save to a file.')
    parser.add_argument('number_of_cars', type=int, help='Number of cars to generate logs for.')
    parser.add_argument('number_of_logs', type=int, help='Number of logs to generate.')
    parser.add_argument('output_file', type=str, help='File path to save the logs.')
    parser.add_argument('--max_interval', type=int, default=700, help='Maximum interval in seconds between entries of cars.')

    args = parser.parse_args()

    generate_logs(args.number_of_cars, args.number_of_logs, args.output_file, args.max_interval)