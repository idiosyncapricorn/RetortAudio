import librosa
import soundfile as sf

def load_audio(file_path):
    """
    Load an audio file and return the audio data and sample rate.
    """
    try:
        audio_data, sr = librosa.load(file_path, sr=None, mono=False)
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{file_path}' was not found.")
    except Exception as e:
        raise RuntimeError(f"Error loading audio file '{file_path}': {e}")

    # Ensure audio data is valid
    if audio_data is None or len(audio_data) == 0:
        raise ValueError(f"The file '{file_path}' contains no audio data.")
    return audio_data, sr
