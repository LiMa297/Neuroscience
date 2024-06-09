"""
on basis of sample script
"""
import asyncio
from idun_guardian_sdk import GuardianClient, FileTypes
from Play_MP3 import MP3Player

my_api_token = "idun_QN0Cq1f2G3mpJjjblfC_hdW-AwftSG7jBaSpQU-XpHONk6IRXN4x13Yp"
RECORDING_TIMER = 100000    # 60 * 15  # 15 min


def print_data(data):
    print(data.message)


def check_beta(data):
    # Ensure 'stateless_z_scores' is a non-empty list
    # print(data.message)
    # print('hugo')
    # print(data.message.get('stateless_z_scores'))
    # print('walter')
    if data.message.get('stateless_z_scores'):
        # Extract the first dictionary in the list
        z_scores = data.message['stateless_z_scores'][0]

        # Extract the beta value
        beta = z_scores.get('Beta')
        if beta is not None:
            if beta < 1.0 or beta > 2.4:
                print(f"Beta out of range: {beta}")
                MP3Player.play_music()
            else:
                print(f"Beta in range: {beta}")
        else:
            print("Beta value is not available in the data.")

    else:
        print("stateless_z_scores is empty or not available.")


if __name__ == "__main__":
    client = GuardianClient(api_token=my_api_token)
    client.address = asyncio.run(client.search_device())

    # subscribe_live_insights(raw_eeg=False, filtered_eeg=True, handler=print_data)
    client.subscribe_realtime_predictions(fft=True, jaw_clench=False, handler=check_beta)

    asyncio.run(client.start_recording(recording_timer=RECORDING_TIMER))
    rec_id = client.get_recording_id()

    print("RecordingId", rec_id)
    client.update_recording_tags(recording_id=rec_id, tags=["tag1", "tag2"])
    client.update_recording_display_name(recording_id=rec_id, display_name="todays_recordings")
