from basic_pitch.inference import predict
from basic_pitch import ICASSP_2022_MODEL_PATH


def mp3_to_midi(mp3_file: str):
    """
    Convert MIDI data to MusicXML format.
    
    Args:
        midi_data: The MIDI data to be converted.
    
    Returns:
        The music object in MusicXML format.
    """
    model_output, midi_data, note_events = predict(mp3_file)

    return midi_data
