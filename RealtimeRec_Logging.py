"""
Sample script for using the Guardian Earbud Client
- Start recording data from the Guardian Earbuds
"""
import asyncio
import logging
from idun_guardian_sdk import GuardianClient
from lsl_utils import stream_data

# Configuration constants
EXPERIMENT: str = "lsl_stream"
RECORDING_TIMER: int = 1000000
LED_SLEEP: bool = True
SENDING_TIMEOUT: float = 2  # Adjust this value if necessary
BI_DIRECTIONAL_TIMEOUT: float = 4  # Adjust this value if necessary
FILTER_DATA: bool = False

bci = GuardianClient(api_token='idun_QN0Cq1f2G3mpJjjblfC_hdW-AwftSG7jBaSpQU-XpHONk6IRXN4x13Yp')

# Configure the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Function to search for the device address
async def set_device_address():
    bci.address = await bci.search_device()
    if not bci.address:
        logger.info("No Guardian device found. Please ensure the device is on and within range.")


# Main function to start recording and stream data
async def main():
    """
    This function starts the recording and the LSL stream.
    """

    try:
        await set_device_address()
        logger.info("Starting recording")
        await asyncio.gather(
            bci.start_recording(
                recording_timer=RECORDING_TIMER,
                led_sleep=LED_SLEEP,
            ),
            stream_data(api_class=bci.api_token, filter_data=FILTER_DATA),
        )
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        # Handle specific exceptions if needed
    finally:
        logger.info("Recording finished")

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
