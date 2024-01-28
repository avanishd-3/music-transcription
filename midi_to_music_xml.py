import muspy
from pathlib import Path
import os


def midi_to_music_obj(midi_data) -> muspy.Music:
    """
    Convert MIDI data to a muspy Music object.

    Args:
        midi_data: The MIDI data to be converted.

    Returns:
        muspy.Music: The converted muspy Music object.
    """
    return muspy.from_pretty_midi(midi_data)


def music_obj_to_music_xml_file(music_obj: muspy.Music):
    path_to_download_folder = Path(os.path.join(Path.home(), "Downloads"))
    muspy.write_musicxml(path_to_download_folder / 'music.xml', music_obj)
    """
    Convert a music object to a MusicXML file.

    Args:
        music_obj (muspy.Music): The music object to be converted to MusicXML.

    Returns:
        None
    """
    muspy.write_musicxml(path_to_download_folder / 'music.xml', music_obj)


def midi_to_music_xml(midi_data):
    """
    Convert MIDI data to MusicXML format.
    
    Args:
        midi_data: The MIDI data to be converted.
    
    Returns:
        The music object in MusicXML format.
    """
    music_obj = midi_to_music_obj(midi_data)
