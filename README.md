# Kaldi Spoken Digit Classifier 
This digit classifier is based on the [Kaldi tutorial for dummies](https://kaldi-asr.org/doc/kaldi_for_dummies.html) but in which I have prepared the dataset from the [free spoken digit dataset](https://github.com/Jakobovski/free-spoken-digit-dataset).

## Setup
### Clone the Kaldi repo
`git clone https://github.com/kaldi-asr/kaldi.git`
### Change directory to the egs (example scripts directory)
`cd kaldi/egs`
### Clone this repo 
`git clone https://github.com/Airick73/Kaldi-Spoken-Digit-Classifier.git`
### Run the run.sh bash script 
`./run.sh`

## How I created the data from [FSDD](https://github.com/Jakobovski/free-spoken-digit-dataset)
Using the following python script I took the individual spoken digits and concated them together to form a random selection of three spoken digits. For example taking 0_george_1.wav, 2_george_5.wav, and 5_george_2.wav I created george_1_5_2.wav which is george saying "one five two". Note that in FSDD the first number of the .wav indicates the index and the last number indicates the spoken digit. They have the speaker say the same digit multiple times. 

```{python}
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

```
