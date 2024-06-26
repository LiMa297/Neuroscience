import asyncio
from pylsl import StreamInfo, StreamOutlet

from idun_guardian_sdk import GuardianClient

RECORDING_TIMER: int = 60 * 60 * 2  # 2 hours
my_api_token = "idun_QN0Cq1f2G3mpJjjblfC_hdW-AwftSG7jBaSpQU-XpHONk6IRXN4x13Yp"


def handle_insight(insight):
    print("Received insight:", insight)


if __name__ == "__main__":
    client = GuardianClient(api_token=my_api_token)
    client.address = asyncio.run(client.search_device())

    info = StreamInfo("IDUN", "EEG", 1, 250, "float32", client.address)
    lsl_outlet = StreamOutlet(info, 20, 360)

    client.subscribe_live_insights(
        raw_eeg=True,
        handler=lambda data: lsl_outlet.push_chunk(
            data["raw_eeg"]["ch1"], data["raw_eeg"]["timestamp"][-1]
        ),
    )

    asyncio.run(client.start_recording(recording_timer=RECORDING_TIMER))


    # Subscribe to live insights
    client.subscribe_live_insights(callback=handle_insight)