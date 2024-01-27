from basic_pitch.inference import predict
from basic_pitch import ICASSP_2022_MODEL_PATH


def mp3_to_midi(mp3_file: str):
    """ Convert mp3 file to MIDI file"""

    model_output, midi_data, note_events = predict(mp3_file)

    print(note_events)


mp3_to_midi('audio.mp3')
