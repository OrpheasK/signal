import numpy as np
import soundfile as sf

hrir, audio, convolved_left, convolved_right, binaural_audio = [], [], [], [], []

# Load the stereo HRIR audio file
hrirfiles = ['azi_99,0_ele_45,0.wav', #center
'azi_99,0_ele_45,0.wav', #30
'azi_99,0_ele_45,0.wav', #-30
'azi_99,0_ele_45,0.wav', #110
'azi_99,0_ele_45,0.wav', #-110
'azi_99,0_ele_45,0.wav'] #180

for file in hrirfiles:
    data, fs = sf.read('ezioexp/azieles/'+file)
    hrir.append(data)


# Load the audio file you want to spatialize
files = ['EzioFamilyTheme441_FL.wav',
'EzioFamilyTheme441_FR.wav',
'EzioFamilyTheme441_C.wav',
'EzioFamilyTheme441_SB.wav',
'EzioFamilyTheme441_SL.wav',
'EzioFamilyTheme441_SR.wav']

for file in files:
    data, fs = sf.read('ezioexp/'+file)
    audio.append(data)

print (audio[0])

# Ensure the HRIR and audio files have the same sample rate (fs)

# Perform convolution for both channels

for i in range(6):
    convolved_left.append(np.convolve(audio[i], hrir[i][:, 0], mode='same'))
    convolved_right.append(np.convolve(audio[i], hrir[i][:, 1], mode='same'))

    # Create the binaural audio by combining left and right channels
    binaural_audio.append(np.column_stack((convolved_left[i], convolved_right[i])))

    # Save the resulting binaural audio
    sf.write(f'ezioexp/output_binauralezio_good{i}.wav', binaural_audio[i], fs)