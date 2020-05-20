# Parallel WaveGAN (+ MelGAN & Multi-band MelGAN) implementation with Pytorch

This is a fork of the original implementation to sync with Mozilla TTS.

| Pre-Trained Model |Dataset | Commit | Details |
|--------|--------|--------|---------|
| [PWGAN](https://www.dropbox.com/sh/fz8iixkhv68zsb4/AABlrNomybrGIinOrgLhZeosa?dl=0) | LJSpeech | fca88f9 | Trained with GT spectrograms|
| [MelGAN](https://www.dropbox.com/sh/d2fusbums88s7je/AAC3OaAOIVg1LDbp0nzl7iSNa?dl=0) | LJSpeech |[fe9c02e](https://github.com/erogol/ParallelWaveGAN/tree/fe9c02e) | Trained with GT spectrograms|

Basic workflow
- Create spectrograms using TTS based audio processing python python bin/preprocess_with_ap.py (this requires Mozilla TTS to be installed).
- Setup the config file wrt audio processing parameters used in your TTS model.
- Train the model.

Visit the original Repo for more information.
