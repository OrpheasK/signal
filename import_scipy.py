import scipy
import scipy.io.wavfile as wavfile
import scipy.fftpack as fftpk
import numpy as np
from matplotlib import pyplot as plt

#based on code https://github.com/Metallicode/RandomProjects_IOT/blob/master/06_fft_analysis/python_fft.py

s_rate, signal = wavfile.read("/Users/orpheas/audiofl/anoteshift.wav") 

fft = abs(scipy.fft.fft(signal))
# fft = fft[:, :1]
freqs = fftpk.fftfreq(len(fft), (1.0/s_rate))

length = signal.shape[0] / s_rate
time = np.linspace(0., length, signal.shape[0])

fftmax = np.max(fft)

percentages = fft/(fft.sum(axis=0)/2) * 100 #sum divided by two, the transform also takes place for negative values which are not used

onehz = 1/freqs[1] 
binfr = [396, 417, 528, 639, 741, 852, 963]
binfrnm = ['396 Hz', '417 Hz', '528 Hz', '639 Hz', '741 Hz', '852 Hz', '963 Hz']

counts = np.zeros(7)

fig, ax = plt.subplots()
# print(percentages[round(65/freqs[1])])

for i, centrfr in enumerate(binfr):
    counts[i] = sum(percentages[round((centrfr-onehz/2)/freqs[1]):round((centrfr+onehz/2)/freqs[1])])

print(counts) #percentage of each frequency's presence in the audio file
print(counts/counts.sum()*100) #total percentage of selected frequencies across the full frequency bandwidth
presnc = round(counts.sum(), 2)

bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:blue', 'tab:green', 'tab:orange']
ax.bar(binfrnm, counts/counts.sum()*100, color=bar_colors)
ax.set_xlabel('Frequency')
ax.set_ylabel('Percentage')
plt.figtext(0.53,0.85,'Presence of frequencies: {}%'.format(presnc))
plt.show()
# print(np.argmax(percentages))

