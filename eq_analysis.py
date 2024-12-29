import numpy as np
from librosa.feature import spectral_centroid

def analyze_eq(audio_data, sr):
    """
    Analyze tonal balance and provide recommendations for EQ adjustments.
    """
    try:
        if len(audio_data.shape) > 1:  # Stereo audio
            audio_data = np.mean(audio_data, axis=0)  # Convert to mono

        # Spectral centroid
        centroid = spectral_centroid(y=audio_data, sr=sr).mean()

        return {
            "Spectral Centroid": f"{centroid:.2f} Hz",
            "Recommendation": "Balance frequency bands based on usage context",
        }

    except Exception as e:
        return {
            "Error": f"EQ analysis failed: {e}"
        }
