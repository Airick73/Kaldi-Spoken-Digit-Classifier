import os

# Define a dictionary to map numbers to words
number_to_word = {
    '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
    '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
}

def number_to_words(transcription):
    words = transcription.split()
    return ' '.join(number_to_word.get(word, word) for word in words)

def generate_transcriptions(directory, train_speakers, test_speakers):
    
    # Ensure output directory exists
    train_output_dir = os.path.join(".", "train")
    os.makedirs(train_output_dir, exist_ok=True)
    
    # Ensure output directory exists
    test_output_dir = os.path.join(".", "test")
    os.makedirs(test_output_dir, exist_ok=True)
    
    # Define the output file paths
    train_output_file = os.path.join(train_output_dir, 'text')
    test_output_file = os.path.join(test_output_dir, 'text')

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
                        # Create the text transcription (replace underscores with spaces)
                        transcription = combination.replace('_', ' ')
                        # Convert numbers to words
                        transcription_in_words = number_to_words(transcription)
                        # Create the output line
                        line = f"{speaker}_{combination} {transcription_in_words}\n"
                        
                        # Write to the appropriate output file
                        if speaker in test_speakers:
                            test_outfile.write(line)
                        elif speaker in train_speakers:
                            train_outfile.write(line)

# Example usage
directory = r'path\to\random_combinations'  # Replace with your directory path to the random_combinations made by digit_combinator.py
train_speakers = ['george', 'lucas', 'nicolas', 'theo', 'yweweler']  # Replace with your train speaker names
test_speakers = ['jackson']  # Replace with your test speaker names

generate_transcriptions(directory, train_speakers, test_speakers)
