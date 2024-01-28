import youtube_to_mp3
import mp3_to_midi
import midi_to_music_xml


def main(url: str):
    """ Output a music xml file given a Youtube url"""

    # url = input("Enter Youtube url: ").strip()

    youtube_to_mp3.youtube_link_to_mp3(link=url)

    midi = mp3_to_midi.mp3_to_midi(mp3_file='audio.mp3')

    music_obj = midi_to_music_xml.midi_to_music_obj(midi)

    midi_to_music_xml.music_obj_to_music_xml_file(music_obj)


