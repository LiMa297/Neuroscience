from idun_guardian_sdk import GuardianClient
import time
import asyncio
from Play_MP3 import handle_drowsy

# Define your API key
API_KEY = 'idun_QN0Cq1f2G3mpJjjblfC_hdW-AwftSG7jBaSpQU-XpHONk6IRXN4x13Yp'

# Initialize the Idun client
client = GuardianClient(api_token=API_KEY)
client.address = asyncio.run(client.search_device())


client.subscribe_realtime_predictions(fft=True, jaw_clench=False, handler=handle_drowsy)
asyncio.run(client.start_recording(recording_timer=10000))
rec_id = client.get_recording_id()

print("RecordingId", rec_id)
client.update_recording_tags(recording_id=rec_id, tags=["tag1", "tag2"])
client.update_recording_display_name(recording_id=rec_id, display_name="todays_recordings")
# Subscribe to live insights

# Keep the script running to continue receiving insights

asyncio.run(main())             # VERSTANDI DAS FALSCH ODER KÖNNT MA DO VELLECHT NO AN FILTER IFÜAGA OBA, DASS NUR
                                # BETA DATA KON FÜRS ERSTE? DENN KÖNNT MA DIREKT UF DR FILTER FÜRA MP3