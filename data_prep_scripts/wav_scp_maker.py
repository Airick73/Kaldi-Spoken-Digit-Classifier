import os

def populate_wav_scp(random_combinations_dir, digits_audio_dir):
    # List of speaker directories
    train_speakers = ['george', 'yweweler', 'lucas', 'nicolas', 'theo']
    test_speakers = ['jackson']

    # Create directories for train and test
    os.makedirs("wav_files/train", exist_ok=True)
    os.makedirs("wav_files/test", exist_ok=True)
    
    # Open files for writing
    train_wav_scp = os.path.join("wav_files/train", "wav.scp")
    test_wav_scp = os.path.join("wav_files/test", "wav.scp")
    
    with open(train_wav_scp, 'w') as train_outfile, open(test_wav_scp, 'w') as test_outfile:
        # Traverse the directory
        for speaker in os.listdir(random_combinations_dir):
            speaker_dir = os.path.join(random_combinations_dir, speaker)
            if os.path.isdir(speaker_dir):
                for wav_file in os.listdir(speaker_dir):
                    # Extract the combination from the wav file name
                    combination = os.path.splitext(wav_file)[0]
                    
                    # Create the output line
                    line = f"{speaker}_{combination} {digits_audio_dir}/{speaker}/{wav_file}\n"
                    
                    if speaker in train_speakers:
                        # Write to the train output file
                        train_outfile.write(line)
                    elif speaker in test_speakers:
                        # Write to the test output file
                        test_outfile.write(line)

# Example usage
random_combinations_dir = "./random_combinations"  # Replace with your directory path to the random_combinations made by digit_combinator.py
digits_audio_dir = "./digits_audio"

populate_wav_scp(random_combinations_dir, digits_audio_dir)
