# Import the IDUN Guardian SDK
import idun_guardian_sdk as idun
from idun_guardian_sdk import GuardianClient
import numpy as np
from scipy.fft import fft
from scipy.signal import find_peaks
drowsy_bool = False

idun.GuardianClient(api_token="idun_QN0Cq1f2G3mpJjjblfC_hdW-AwftSG7jBaSpQU-XpHONk6IRXN4x13Yp")

# Parameters
sampling_rate = 100  # Sample rate in Hz
buffer_size = sampling_rate  # Buffer size to collect 1 second of data
frequency_range = (20, 30)  # Frequency range to detect peaks in Hz

# Buffer to collect data
data_buffer = []

idun.subscribe_live_insights(raw_eeg=False, filtered_eeg=True, imu=False)
idun.subscribe_realtime_predictions(fft=True, jaw_clench=False, bin_heog=False)


def on_data_received(data_point):
    global data_buffer

    # Add the new data point to the buffer
    data_buffer.append(data_point)

    # If the buffer is full, process the data
    if len(data_buffer) >= buffer_size:
        process_data(data_buffer)
        # Clear the buffer for the next set of data
        data_buffer = []


def process_data(data):
    # Perform FFT on the data
    N = len(data)
    yf = fft(data)
    xf = np.fft.fftfreq(N, 1 / sampling_rate)[:N // 2]

    # Find the indices corresponding to the frequency range of interest
    freq_indices = np.where((xf >= frequency_range[0]) & (xf <= frequency_range[1]))[0]

    # Check for peaks in the selected frequency range
    peaks, _ = find_peaks(np.abs(yf[:N // 2][freq_indices]))

    # Determine if there is a peak
    peak_detected = len(peaks) > 0

    print("Peak detected:", peak_detected)

    # Process the filtered data or take appropriate action
    if peak_detected:
        handle_peak_detection()


def handle_peak_detection():
    # Implement your logic when a peak is detected
    print("Peak detected in the 20-30Hz range!")
    drowsy_bool = True


# Simulate receiving data points
for i in range(1000):  # Simulate 10 seconds of data
    # Generate a random data point (replace with real data in practice)
    data_point = np.sin(2 * np.pi * 25 * i / sampling_rate)  # Example: 25Hz signal
    on_data_received(data_point)
