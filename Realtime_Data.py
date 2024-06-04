"""
on basis of sample script
"""
import asyncio
from idun_guardian_sdk import GuardianClient, FileTypes
from testing_mp3 import handle_drowsy

my_api_token = "idun_QN0Cq1f2G3mpJjjblfC_hdW-AwftSG7jBaSpQU-XpHONk6IRXN4x13Yp"
RECORDING_TIMER = 60 * 15  # 15 min


def print_data(data):
    print(data.message)


if __name__ == "__main__":
    client = GuardianClient(api_token=my_api_token)
    client.address = asyncio.run(client.search_device())

    # subscribe_live_insights(raw_eeg=False, filtered_eeg=True, handler=print_data)
    client.subscribe_realtime_predictions(fft=True, jaw_clench=False, handler=handle_drowsy([{'Beta'}]))

    asyncio.run(client.start_recording(recording_timer=RECORDING_TIMER))
    rec_id = client.get_recording_id()

    print("RecordingId", rec_id)
    client.update_recording_tags(recording_id=rec_id, tags=["tag1", "tag2"])
    client.update_recording_display_name(recording_id=rec_id, display_name="todays_recordings")
