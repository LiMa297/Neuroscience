from idun_guardian_sdk import GuardianClient
import time
import asyncio

# Define your API key
API_KEY = 'idun_QN0Cq1f2G3mpJjjblfC_hdW-AwftSG7jBaSpQU-XpHONk6IRXN4x13Yp'

# Initialize the Idun client
client = GuardianClient(api_token=API_KEY)


# Define the callback function to handle incoming insights
def handle_insight(insight):
    print("Received insight:", insight)

async def main():
    """
    This function is the main function for the script. It will start the recording and the LSL stream.
    """
    await asyncio.gather(
        client.start_recording(
            client.subscribe_live_insights(filtered_eeg=True, handler=handle_insight)
        )
        #stream_data(api_class=client.api_token)
        client.end_recording(main())
    )

# Subscribe to live insights

# Keep the script running to continue receiving insights

asyncio.run(main())