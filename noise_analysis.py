import numpy as np
from scipy.signal import find_peaks

def analyze_noise(audio_data, sr, threshold=0.02):
    """
    Analyze noise levels and classify issues.
    """
    try:
        if len(audio_data.shape) > 1:  # Stereo audio
            audio_data = np.mean(audio_data, axis=0)  # Convert to mono

        rms = np.sqrt(np.mean(audio_data ** 2))
        is_noisy = rms > threshold

        # Compute FFT and ensure magnitudes are 1D
        fft = np.fft.fft(audio_data)
        magnitudes = np.abs(fft).flatten()

        # Generate frequency array
        freqs = np.fft.fftfreq(len(audio_data), 1 / sr)

        # Find peaks
        peaks, _ = find_peaks(magnitudes, height=np.max(magnitudes) * 0.2)
        tonal_noise = [freqs[p] for p in peaks if 20 <= freqs[p] <= 100]

        return {
            "RMS Level": f"{rms:.4f}",
            "Noisy": is_noisy,
            "Tonal Noise Frequencies": tonal_noise,
            "Recommendation": "Use noise reduction tools" if is_noisy else "No action needed",
        }

    except Exception as e:
        return {
            "Error": f"Noise analysis failed: {e}"
        }
