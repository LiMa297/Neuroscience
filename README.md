# Neuroscience

This is the README and you should read it, definitely!

### GroupName: Soundwave Society

As we are both quite new in the field of programming, it was challenging to get on with the new environment
of continuous input data and processing with those. We tried our best and though in retrospective, it could have been better
we are proud on how we got along no matter what. Many techniques were tried, as you can see in the 'Unused' folder,
but in the end one path finally led to rome, or in this case to a study-stress-and-tiredness-reliefe-tool.

## INSTRUCTIONS:
- in the Play_MP3.py, enter your music folder
- run the Realtime_Data.py file while wearing the IDUN Guardian Device
- focus on a task :)

## IDEAS:
- increase focus- -better learning experience-
- Stress relief w/ audio support/interruption ---> concentration via ear eeg (https://doi.org/10.1109/BCI48061.2020.9061652)
- Change mental state w/ predefined music playlists ---> music therapy (DOI 10.1007/s12193-011-0080-6 and https://doi.org/10.3390/s19184014)

## FURTHER DEVELOPMENT:
- recommendations based on liked songs during same mental state (https://doi.org/10.1007/s11042-015-3202-4)


## DETAILS:
- when mental state indicates, that learning is useless, music will play... (depending on mood) 
- bandwidth observations: drop in gamma ---> inattentive, beta goes up ---> stress, alpha goes down ---> not relaxed (https://doi.org/10.3389/fninf.2022.997282)
- implement function in mp3 player to get songs in playlist and play automatically... [DONE]

## WE NEED:
- Real time EEG data [DONE]
- Bandwidth filters (recognize drop and increase / decision tree) (alpha AND/OR beta) [DONE FOR BETA]
- music player [DONE, AT LEAST INVISIBLE FOR NOW...]
- at least one playlist (eventually different mood playlists) [KINDA DONE]
- implement decision of bandwidth filter to start playlist (eventually select playlist / study break OR motivation) [DONE]
- eventually timer to stop playlist (for study breaks) [DONE]

original code source: MP3_player.py https://data-flair.training/blogs/python-mp3-player/
we used this code as a basis and then built on it for our usecase


## Play_MP3.py
This file contains the setup for the mp3 player. It creates a Pop-up window, with control buttons like play, stop, next and so on.
In this stage of the project, a playlist is predefined and set in the function "load_music_folder".
As the scope for our project is to create an automatic detection for exhaustion, the program starts the music player automatically,
when the defined scope is reached and the music will play for a studying break of 15 minutes and stops afterwards.

## Realtime_Data.py
This file is based on the example script for getting all the real-time data. This should get the User-data and check if the beta 
value is in the specified bandwidth. A beta lower than 1.0 and higher than 2.4 should trigger the music player. All the other 
states and values should have no consequence.

## ENDNOTES:
- sadly the pop-up is not working for the music player, in some tests we did, the pop-up appeared and we had to manually click
    play to start the music, which was not what we wanted, so we decided in favour of automatically starting the music
    however this starts the music without the pop-up and you're forced to listen to the music that plays... without the option of skipping 
- somehow we're not sure how if the play_music works after the 15min break as we tested only on 15 seconds... for time reasons



