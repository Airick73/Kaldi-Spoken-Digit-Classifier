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
