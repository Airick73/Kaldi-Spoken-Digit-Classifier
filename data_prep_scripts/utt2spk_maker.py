import os

def generate_utt2spk(directory, train_speakers, test_speakers):
    # Create directories for train and test utt2spk files
    os.makedirs("utt2spk/train", exist_ok=True)
    os.makedirs("utt2spk/test", exist_ok=True)

    # Define the output file paths
    train_output_file = os.path.join("utt2spk/train", 'utt2spk')
    test_output_file = os.path.join("utt2spk/test", 'utt2spk')

    # Open the output files for writing
    with open(train_output_file, 'w') as train_outfile, open(test_output_file, 'w') as test_outfile:
        
        # Traverse the directory
        for speaker in os.listdir(directory):
            speaker_dir = os.path.join(directory, speaker)
            if os.path.isdir(speaker_dir):
                for wav_file in os.listdir(speaker_dir):
                    if wav_file.endswith('.wav'):
                        # Extract the combination from the wav file name
                        combination = os.path.splitext(wav_file)[0]
                        # Create the output line
                        line = f"{speaker}_{combination} {speaker}\n"
                        
                        # Write to the appropriate output file
                        if speaker in test_speakers:
                            test_outfile.write(line)
                        elif speaker in train_speakers:
                            train_outfile.write(line)

# Example usage
directory = "./random_combinations"  # Replace with your directory path to the random_combinations made by digit_combinator.py
train_speakers = ['george', 'lucas', 'nicolas', 'theo', 'yweweler']  # Replace with your train speaker names
test_speakers = ['jackson']  # Replace with your test speaker names

generate_utt2spk(directory, train_speakers, test_speakers)
