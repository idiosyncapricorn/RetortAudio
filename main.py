from audio_io import load_audio
from noise_analysis import analyze_noise
from eq_analysis import analyze_eq
from normalization_analysis import analyze_normalization
from stereo_analysis import analyze_stereo
from harmonic_analysis import analyze_harmonic_distortion
from transient_analysis import analyze_transients


def generate_report(input_file):
    """
    Generate and format a user-friendly audio analysis report.
    """
    # Load the audio file
    audio_data, sr = load_audio(input_file)

    # Perform analyses
    noise_result = analyze_noise(audio_data, sr)
    eq_result = analyze_eq(audio_data, sr)
    normalization_result = analyze_normalization(audio_data)
    stereo_result = analyze_stereo(audio_data)
    harmonic_result = analyze_harmonic_distortion(audio_data, sr)
    transient_result = analyze_transients(audio_data, sr)

    # Format the report
    print("\n--- Audio Analysis Report ---\n")
    
    print("1. Noise Analysis")
    print(f"- RMS Level: {noise_result.get('RMS Level', 'N/A')}")
    print(f"- Is it noisy? {'Yes' if noise_result.get('Noisy', False) else 'No'}")
    print(f"- Problem Frequencies: {', '.join(map(str, noise_result.get('Tonal Noise Frequencies', [])))}")
    print(f"- Recommendation: {noise_result.get('Recommendation', 'N/A')}\n")

    print("2. EQ (Tone Balance) Analysis")
    print(f"- Spectral Centroid (Brightness): {eq_result.get('Spectral Centroid', 'N/A')}")
    print(f"- Recommendation: {eq_result.get('Recommendation', 'N/A')}\n")

    print("3. Volume and Loudness Analysis")
    print(f"- Max Amplitude: {normalization_result.get('Max Amplitude', 'N/A')}")
    print(f"- Dynamic Range: {normalization_result.get('Dynamic Range (dB)', 'N/A')} dB")
    print(f"- Clipping Detected: {'Yes' if normalization_result.get('Clipping Detected', False) else 'No'}")
    print(f"- Recommendation: {normalization_result.get('Recommendation', 'N/A')}\n")

    print("4. Stereo Analysis")
    print(f"- Stereo Detected: {'Yes' if stereo_result.get('Stereo Detected', False) else 'No'}")
    print(f"- Stereo Width: {stereo_result.get('Width', 'N/A')}")
    print(f"- Recommendation: {stereo_result.get('Recommendation', 'N/A')}\n")

    print("5. Harmonic Distortion Analysis")
    harmonic_peaks = harmonic_result.get('Harmonic Peaks', [])
    harmonic_peaks_list = list(map(str, harmonic_peaks))  # Convert to list
    print(f"- Harmonic Peaks: {', '.join(harmonic_peaks_list[:5])} ...")  # Show first 5 peaks
    print(f"- Recommendation: {harmonic_result.get('Recommendation', 'N/A')}\n")


    print("6. Transient Analysis")
    print(f"- Number of Transients: {transient_result.get('Transient Count', 'N/A')}")
    print(f"- Transient Times (s): {', '.join(map(lambda x: f'{x:.2f}', transient_result.get('Transient Times (s)', []))[:5])} ...")
    print(f"- Recommendation: {transient_result.get('Recommendation', 'N/A')}\n")

    print("--- End of Report ---")

def main():
    # Prompt user to choose a file
    file_path = input("Please enter the path to the audio file: ")
    try:
        generate_report(file_path)
    except Exception as e:
        print(f"Error processing file: {e}")

if __name__ == "__main__":
    main()