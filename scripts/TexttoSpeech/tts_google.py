import gtts
from playsound import playsound

# make request to google to get synthesis
tts = gtts.gTTS("Selam Dünya", lang="tr")
# save the audio file
tts.save("selam.mp3")
# play the audio file
playsound("selam.mp3")

# all available languages along with their IETF tag
print(gtts.lang.tts_langs())
