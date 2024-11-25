import os
import wave
import librosa
import soundfile as sf


#path to the target files
source_dir = "sourcefiles"  



for file in os.listdir(source_dir): 

    file_path = os.path.join(source_dir, file)

    #finds the files naitive sample rate and prints it
    with wave.open(file_path, 'rb') as wav_file:
        sample_rate = wav_file.getframerate()  
        print(f"{file} sample rate: {sample_rate} Hz")
    
    #gets audio data for librosa
    audio_data, original_sample_rate = librosa.load(file_path, sr=None)


    #resamples target file to 44100 HZ
    resampled_data = librosa.resample(audio_data, orig_sr=original_sample_rate, target_sr=44100)

    #pipes resampled file into sourcefile directory
    resampled_file_path = os.path.join(source_dir, 'resampled_' + file)
    sf.write(resampled_file_path, resampled_data, 44100)

    #prints message indicating success to users
    print(f"'{file}' successfully resampled to 44100 Hz")

