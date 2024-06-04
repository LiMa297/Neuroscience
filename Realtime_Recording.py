"""
Sample script for using the Guardian Earbud Client
- Start recording data from the Guardian Earbuds
"""
import asyncio
from idun_guardian_sdk import GuardianClient
from lsl_utils import stream_data

EXPERIMENT: str = "lsl_stream"
RECORDING_TIMER: int = 1000000
LED_SLEEP: bool = True
SENDING_TIMEOUT: float = 2  # If no receipt is received for 2 seconds, the data is buffered
                           # If you experience excessive disruptions, try increasing this value
BI_DIRECTIONAL_TIMEOUT: float = 4  # If no bi-directional data is received for 4 seconds, the connection is re-established
                                    # If you experience excessive disruptions, try increasing this value
FILTER_DATA = False

# start a recording session
bci = GuardianClient(api_token="idun_QN0Cq1f2G3mpJjjblfC_hdW-AwftSG7jBaSpQU-XpHONk6IRXN4x13Yp")
bci.address = asyncio.run(bci.search_device())


async def main():
    """
    This function is the main function for the script. It will start the recording and the LSL stream.
    """
    await asyncio.gather(
        bci.start_recording(
            recording_timer=RECORDING_TIMER,
            led_sleep=LED_SLEEP,
        ),
        stream_data(api_class=bci.api_token, filter_data=FILTER_DATA),
    )


asyncio.run(main())