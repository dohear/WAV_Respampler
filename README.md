# .WAV Resampler

This is a simple .WAV file resampler for burning .wav files to a CD.
It takes an imput directory (containing all of the .wav files you want resampled),
tells you each individual songs sample rate in its naitive form,
then pipes resampled duplicates of every .WAV file into the same directory as the originals, 
resampled to 44.1 kHZ (The only sample rate witch with .WAV files can be burned on a CD)

# How to:

- Install the requirements found in __requirements.txt__

- Set up your file structure 
    - note: sourcefiles must be named sourcefiles, 
    otherwise you have to alter the code's source_dir 
    variable to match the path to your directory 
    containing the target .WAV files

```plaintext
arbitrary directory/
│
├── sourcefiles/
│   ├── target1.WAV           
│   ├── target2.WAV              
│   ├── ....             
│   └── targetn.WAV
└── samplerate.py
```

- run the code in terminal by typing
```
    python samplerate.py
```

- after the code has finished running your __sourcefiles__ directory
should contain all of the resampled .WAV files, indicated by the prefix
__'resampled_'__, along with the originals in their raw unmodified forms


