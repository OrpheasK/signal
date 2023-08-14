import scipy
import scipy.io.wavfile as wavfile
import scipy.fftpack as fftpk
import numpy as np
from matplotlib import pyplot as plt

#based on code https://github.com/Metallicode/RandomProjects_IOT/blob/master/06_fft_analysis/python_fft.py

s_rate, signal = wavfile.read("/Users/orpheas/audiofl/beau.wav") 

fft = abs(scipy.fft.fft(signal))
# fft = fft[:, :1]
freqs = fftpk.fftfreq(len(fft), (1.0/s_rate))

length = signal.shape[0] / s_rate
time = np.linspace(0., length, signal.shape[0])

fftmax = np.max(fft)

# for i, f in enumerate(fft):
#     if f < 0.01*fftmax:
#         fft[i] = 0

percentages = fft/(fft.sum(axis=0)/2) * 100 #sum divided by two, the transform also takes place for negative values which are not used

# fig, axs = plt.subplots(2)

# audio waveform plots
# axs[0].plot(time, signal[:, 0], label="Left channel")
# axs[0].plot(time, signal[:, 1], label="Right channel")

# axs[0].legend()

# axs[0].xlabel("Time [s]")
# axs[0].ylabel("Amplitude")

# plt.show()
onehz = 1/freqs[1] 
binfr = [396, 417, 528, 639, 741, 852, 963]
binfrnm = ['396 Hz', '417 Hz', '528 Hz', '639 Hz', '741 Hz', '852 Hz', '963 Hz']

counts = np.zeros(7)

# fft plots
# fft[190]=0
# plt.plot(freqs[range(len(fft)//16)], fft[range(len(fft)//16)])   
# plt.subplot(freqs, fft[:, :1])                                                          
# axs[1].xlabel('Frequency (Hz)')
# axs[1].ylabel('Amplitude')
# plt.show()
# print(fft.sum(axis=0))

fig, ax = plt.subplots()
# print(percentages[round(65/freqs[1])])

for i, centrfr in enumerate(binfr):
    counts[i] = sum(percentages[round((centrfr-onehz/2)/freqs[1]):round((centrfr+onehz/2)/freqs[1])])

print(counts)
print(counts/counts.sum()*100)


bar_colors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:blue', 'tab:green', 'tab:orange']
ax.bar(binfrnm, counts/counts.sum()*100, color=bar_colors)
ax.set_xlabel('Frequency')
ax.set_ylabel('Total percentage in song')
plt.figtext(0.8,0.5,'fwr')
plt.show()
# print(np.argmax(percentages))





# freqs spec:
# liberate 396 Hz
# cleanse 417
# miracles 528
# harmony 639
# resolve 741
# intuition 852
# unity 963