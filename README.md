Parallel WaveGAN fork for Mozilla TTS

This is a fork of the original implementation to sync with Mozilla TTS.

| Models |Dataset | Commit | Audio Sample | Details | | PWGAN | LJSpeech | fca88f9 | soon... | Trained with GT spectrograms| 
| MelGAN | LJSpeech |[22018e6]((https://github.com/erogol/ParallelWaveGAN/tree/22018e6) | ... | Trained with GT spectrograms|

Basic workflow
- Create spectrograms using TTS based audio processing python python bin/preprocess_with_ap.py (this requires Mozilla TTS to be installed).
- Setup the config file wrt audio processing parameters used in your TTS model. 
- Train the model. 

Visit the original Repo for more information.
