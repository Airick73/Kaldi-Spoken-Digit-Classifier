import os
import random
from pydub import AudioSegment
import sys

relative_path_to_recordings = os.path.join("free-spoken-digit-dataset", "recordings")
speaker_names = ["jackson", "nicolas", "theo", "lucas", "yweweler", "george"]
digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Number of recordings of the same digit spoken 
# (i.e. 0_george_22.wav, 0_geroge_1.wav, 0_george_4.wav, are all of the spoken digit zero)
indices = range(50) 

# Number of combinations to create per speaker 
num_combinations = 100

def concatenate_digits(single_spoken_digit_files, output_file):
    
    # Initialize empty audio segment 
    combined_audio = AudioSegment.empty()
    
    for file in single_spoken_digit_files:
        # Initialize audio segment from single spoken digit
        single_digit_audio = AudioSegment.from_wav(file)
        # Concatinate audio segment to combined auto segment
        combined_audio += single_digit_audio
    
    combined_audio.export(output_file, format="wav")

# Ensure output directory exists
output_dir = os.path.join(".", "random_combinations_2")
os.makedirs(output_dir, exist_ok=True)

for speaker_name in speaker_names:
    
    # Ensure output directory exists
    speaker_output_dir = os.path.join(output_dir, speaker_name)
    os.makedirs(speaker_output_dir, exist_ok=True)

    for i in range(num_combinations):
        # Generate a random three-digit combination
        random_spoken_digits = random.choices(digits, k=3)
        
        # Randomly select an index for each digit
        random_indicies = random.choices(indices, k=3)
        
        # Generate file paths for each digit
        digit_files = [
            os.path.join(relative_path_to_recordings, f"{digit}_{speaker_name}_{index}.wav") 
            for digit, index in zip(random_spoken_digits, random_indicies)
        ]
        
        # Create an output file name
        output_file = os.path.join(speaker_output_dir, f"{random_spoken_digits[0]}_{random_spoken_digits[1]}_{random_spoken_digits[2]}.wav")

        # Concatenate the digit files
        concatenate_digits(digit_files, output_file)

        print(f"Created {output_file}")
