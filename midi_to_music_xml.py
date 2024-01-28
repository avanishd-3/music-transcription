import muspy
from pathlib import Path
import os


def midi_to_music_obj(midi_data) -> muspy.Music:
    return muspy.from_pretty_midi(midi_data)


def music_obj_to_music_xml_file(music_obj: muspy.Music):
    path_to_download_folder = Path(os.path.join(Path.home(), "Downloads"))
    muspy.write_musicxml(path_to_download_folder / 'music.xml', music_obj)


def midi_to_music_xml(midi_data):
    music_obj = midi_to_music_obj(midi_data)
