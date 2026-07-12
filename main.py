import time
import random

# This example simulates a "Micro-AI" application running on a resource-constrained
# consumer device, such as a fitness tracker. It demonstrates how sensor data
# is processed locally using a lightweight model without sending data to the cloud.

def micro_ai_activity_classifier(activity_metric: float) -> str:
    """
    A simple, lightweight "Micro-AI" model for activity classification.
    This function represents the AI logic running entirely on the device
    without any cloud interaction.
    """
    # These thresholds act as our simple "trained model" parameters.
    # In a real Micro-AI system, these might come from a highly optimized,
    # pre-trained, and quantized machine learning model (e.g., TensorFlow Lite).
    SEDENTARY_THRESHOLD = 0.5
    WALKING_THRESHOLD = 1.5

    if activity_metric < SEDENTARY_THRESHOLD:
        return "Sedentary"
    elif activity_metric < WALKING_THRESHOLD:
        return "Walking"
    else:
        return "Running"

def simulate_sensor_data():
    """Simulates sensor data from a wearable device (e.g., accelerometer fusion)."""
    # Generate a random activity metric between 0.1 and 2.5
    # This metric could represent average acceleration magnitude or similar.
    return round(random.uniform(0.1, 2.5), 2)

def main():
    print("--- Micro-AI Activity Tracker Simulation ---")
    print("Demonstrates on-device AI processing without cloud dependency.")
    print("-" * 50)

    for i in range(5):
        # 1. Simulate data collection on the device (e.g., from an accelerometer)
        sensor_data = simulate_sensor_data()
        print(f"\n[{i+1}] Device collects sensor data: Activity Metric = {sensor_data}")

        # 2. Process data locally using the Micro-AI model
        # This is the core "Micro-AI" step: inference happens directly on the device.
        start_time = time.perf_counter()
        activity_label = micro_ai_activity_classifier(sensor_data)
        end_time = time.perf_counter()
        processing_time = (end_time - start_time) * 1000 # in milliseconds

        print(f"   [Micro-AI] Local inference completed in {processing_time:.2f} ms.")
        print(f"   [Micro-AI] Detected Activity: {activity_label}")

        # 3. Simulate device action/display based on local AI result
        print(f"   Device displays: 'Current Activity: {activity_label}'")

        # Simulate a short delay before the next sensor reading
        time.sleep(1)

    print("\n--- Simulation Complete ---")
    print("All processing was performed locally on the simulated device.")
    print("No data was sent to the cloud, ensuring privacy and low latency.")

if __name__ == "__main__":
    main()
