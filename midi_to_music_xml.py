import muspy


def midi_to_music_obj(midi_data) -> muspy.Music:
    return muspy.from_pretty_midi(midi_data)


def music_obj_to_music_xml_file(music_obj: muspy.Music):
    muspy.write_musicxml('music.xml', music_obj)
