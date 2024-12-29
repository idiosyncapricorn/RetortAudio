import numpy as np

def analyze_normalization(audio_data):
    """
    Analyze audio normalization, dynamic range, and peak levels.
    """
    try:
        max_amp = np.max(np.abs(audio_data))
        min_nonzero = np.min(np.abs(audio_data[np.nonzero(audio_data)])) if np.any(audio_data) else 1e-10

        dynamic_range = 20 * np.log10(max_amp / min_nonzero)
        clipping_detected = max_amp > 1.0
        low_level_detected = max_amp < 0.5

        return {
            "Max Amplitude": f"{max_amp:.2f}",
            "Dynamic Range (dB)": f"{dynamic_range:.2f}",
            "Clipping Detected": clipping_detected,
            "Low Levels Detected": low_level_detected,
            "Recommendation": (
                "Reduce levels to avoid distortion" if clipping_detected else
                "Normalize to optimize loudness" if low_level_detected else
                "No action required"
            ),
        }

    except Exception as e:
        return {
            "Error": f"Normalization analysis failed: {e}"
        }
