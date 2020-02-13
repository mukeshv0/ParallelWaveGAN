# Parallel WaveGAN fork for Mozilla TTS
This is a fork of the [original](https://github.com/kan-bayashi/ParallelWaveGAN) implementation to sync with [Mozilla TTS](https://github.com/mozilla/TTS).

| Models |Dataset | Commit            | Audio Sample  | Details |
| [PWGAN](https://drive.google.com/drive/folders/1kqIgxSrVoCA-KdpiOYqsVz5kbZyHVtK4?usp=sharing) | LJSpeech | [fca88f9](https://github.com/erogol/ParallelWaveGAN/tree/fca88f9) | soon... | Trained with GT spectrograms|
| [MelGAN](https://drive.google.com/drive/folders/1TSPRdm8N50QhKDmYaje7RlJrGH635SoX?usp=sharing) | LJSpeech |[22018e6]((https://github.com/erogol/ParallelWaveGAN/tree/22018e6) | ... | Trained with GT spectrograms|

# Basic workflow
1. Create spectrograms using TTS based audio processing 
```python python bin/preprocess_tts.py```
2. Setup the config file wrt audio processing parameters used in your TTS model. Sample config can be found under ```parallel_wavegan/tts_config_v2.yaml```.
3. Train the model.
```python python parallel_wavegan/bin/train.py --config tts_config_v2.yaml --outdir /path/to/your/output/```

