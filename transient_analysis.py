import librosa
import numpy as np

def analyze_transients(audio_data, sr, threshold=0.3):
    """
    Analyze transients in the audio signal and report their locations.
    """
    try:
        onset_env = librosa.onset.onset_strength(y=audio_data, sr=sr)
        transients = np.where(onset_env > threshold * np.max(onset_env))[0]
        transient_times = librosa.frames_to_time(transients, sr=sr)

        return {
            "Transient Count": len(transient_times),
            "Transient Times (s)": transient_times.tolist(),
            "Recommendation": "Consider reducing transients with compression" if len(transient_times) > 0 else "No action required",
        }

    except Exception as e:
        return {
            "Error": f"Transient analysis failed: {e}"
        }
