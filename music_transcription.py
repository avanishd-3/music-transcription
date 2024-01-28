import youtube_to_mp3
import mp3_to_midi
import midi_to_music_xml


def main():
    """ Output a music xml file given a Youtube url"""

    url = input("Enter Youtube url: ").strip()

    youtube_to_mp3.youtube_link_to_mp3(link=url)

    midi = mp3_to_midi.mp3_to_midi(mp3_file='audio.mp3')

    midi_to_music_xml.midi_to_music_xml(midi)


if __name__ == "__main__":
    main()