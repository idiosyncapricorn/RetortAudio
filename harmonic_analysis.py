import numpy as np
from scipy.signal import find_peaks

def analyze_harmonic_distortion(audio_data, sr):
    """
    Analyze harmonic distortion by identifying harmonic peaks in the spectrum.
    """
    try:
        if len(audio_data.shape) > 1:  # Stereo audio
            audio_data = np.mean(audio_data, axis=0)  # Convert to mono

        fft = np.fft.fft(audio_data)
        magnitudes = np.abs(fft).flatten()
        freqs = np.fft.fftfreq(len(audio_data), 1 / sr)

        peaks, _ = find_peaks(magnitudes, height=np.max(magnitudes) * 0.1)
        harmonic_frequencies = [freqs[p] for p in peaks if freqs[p] > 0]

        return {
            "Harmonic Peaks": harmonic_frequencies,
            "Recommendation": "Check for distortion in harmonic frequencies" if len(harmonic_frequencies) > 0 else "No significant distortion detected",
        }

    except Exception as e:
        return {
            "Error": f"Harmonic analysis failed: {e}"
        }
