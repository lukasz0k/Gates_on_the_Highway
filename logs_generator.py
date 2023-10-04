import random
import string
import argparse

# Function to generate logs
def generate_logs(num_vehicles, num_logs, file_path):
    # Constants
    road_points = [['240E','250E','260E','270E'],['270W','260W','250W','240W']]
    
    logs = []

    # Generate unique vehicle IDs
    vehicle_ids = []
    while len(vehicle_ids) < num_vehicles:
        # Ensure at least 10 characters with min 3 letters at the beginning
        prefix = random.choices(string.ascii_uppercase, k=max(3,5))
        suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=max(7, 10 - len(prefix))))
        vehicle_id = ''.join(prefix) + suffix
        if vehicle_id not in vehicle_ids:
            vehicle_ids.append(vehicle_id)

    # Initialize a dictionary to track the last EXIT time for each vehicle ID
    last_exit_times = {}

    # Generate logs for the specified number of logs
    while len(logs) < num_logs:
        vehicle_id = random.choice(vehicle_ids)
        entry_time = random.randint(1, 86400)
        
        # Check if there's a previous EXIT log for this vehicle ID
        if vehicle_id in last_exit_times:
            entry_time = last_exit_times[vehicle_id] + 1
        else:
            entry_time = entry_time

        on_road_time1 = entry_time + random.randint(500, 1200)
        on_road_time2 = on_road_time1 + random.randint(300, 800)
        exit_time = on_road_time2 + random.randint(700, 2200)

        direction = random.choice(road_points)

        entry_direction = direction[0]
        on_road_direction1 = direction[1]
        on_road_direction2 = direction[2]
        exit_direction = direction[3]

        logs.extend([(entry_time, vehicle_id, entry_direction, 'ENTRY'),
                     (on_road_time1, vehicle_id, on_road_direction1, 'ON ROAD'),
                     (on_road_time2, vehicle_id, on_road_direction2, 'ON ROAD'),
                     (exit_time, vehicle_id, exit_direction, 'EXIT')])

        # Update the last EXIT time for this vehicle ID
        last_exit_times[vehicle_id] = exit_time

    # Sort logs by time
    logs.sort(key=lambda x: x[0])

    # Save the generated logs to the specified file
    with open(file_path, 'w') as file:
        for log in logs:
            file.write(f"Time: {log[0]}, Vehicle ID: {log[1]}, Point: {log[2]}, Status: {log[3]}\n")

    print(f"Logs saved to '{file_path}'")

def main():
    parser = argparse.ArgumentParser(description="Generate highway logs.")
    parser.add_argument("num_vehicles", type=int, help="Number of vehicles")
    parser.add_argument("num_logs", type=int, help="Number of logs to generate")
    parser.add_argument("file_path", help="Path to the log file")
    args = parser.parse_args()

    # Check if the number of vehicles is greater than 0
    if args.num_vehicles <= 0:
        print("Number of vehicles must be greater than 0.")
        return

    # Generate logs using user-specified parameters
    generate_logs(args.num_vehicles, args.num_logs, args.file_path)

if __name__ == "__main__":
    main()