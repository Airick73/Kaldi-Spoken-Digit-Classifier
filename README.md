# Kaldi Spoken Digit Classifier 
This digit classifier is based on the [Kaldi tutorial for dummies](https://kaldi-asr.org/doc/kaldi_for_dummies.html) but in which I have prepared the dataset from the [free spoken digit dataset](https://github.com/Jakobovski/free-spoken-digit-dataset).

## Setup
1. **Clone the Kaldi repository**: `git clone https://github.com/kaldi-asr/kaldi.git`
2. **Navigate to the examples directory**: `cd kaldi/egs`
3. **Clone this project**: `git clone https://github.com/Airick73/Kaldi-Spoken-Digit-Classifier.git`
4. **Execute the setup script**: `./run.sh`

## Data preperation and required file creation
If you clone this repo into your Kaldi egs (example scripts) directory you will already have the following required files which correlate to the data in digits_audio:

- digits/digit_audio/train/{speaker_name}/{.wav files}
- digits/digit_audio/test/{speaker_name}/{.wav files}
- digits/data/train/utt2spk
- digits/data/train/wav.scp
- digits/data/train/text
- digits/data/train/spk2gender
- digits/data/test/utt2spk
- digits/data/test/wav.scp
- digits/data/test/text
- digits/data/test/spk2gender
- digits/data/local/corpus.txt
- digits/data/local/dict/lexicon.txt
- digits/data/local/dict/nonsilence_phones.txt
- digits/data/local/dict/optional_silence.txt
- digits/data/local/dict/silence_phones.txt

You do not need to do any work to setup these files and can use them as is. However if you wanted to automate the generation of some of the larger files such as:

- digits/digit_audio/train/{speaker_name}/{.wav files}
- digits/digit_audio/test/{speaker_name}/{.wav files}
- digits/data/train/utt2spk
- digits/data/train/wav.scp
- digits/data/train/text
- digits/data/test/utt2spk
- digits/data/test/wav.scp
- digits/data/test/text
- digits/data/local/corpus.txt

The scripts I created for automating the generation of those files are located in the `data_prep_scripts` directory. 

## How I created the digit_audio data from [FSDD](https://github.com/Jakobovski/free-spoken-digit-dataset)
Using the `digit_combinator.py` python script located in `digits/data_prep_scripts` I took the individual spoken digits and concated them together to form a random selection of three spoken digits. For example taking 0_george_1.wav, 2_george_5.wav, and 5_george_2.wav I created george_1_5_2.wav which is george saying "one five two". Note that in FSDD the first number of the .wav indicates the index and the last number indicates the spoken digit. They have the speaker say the same digit multiple times. 

## Contributing 

Contributions are welcome! Please submit pull requests for bug fixes, features, or documentation improvements.

## Lisence 

MIT License

Copyright (c) [2024] [Eric Kemmer]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.