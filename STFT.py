import librosa
import librosa.display
import matplotlib.pyplot as plt

audio_path = "audio.wav"

# 加载音频文件 y是音频数据 sr是采样率
y, sr = librosa.load(audio_path, sr=None)

# 计算短时傅里叶变换
D = librosa.stft(y)

# 将幅度转换为分贝
DB = librosa.amplitude_to_db(abs(D))
DB = DB.min()
DB /= DB.max()


# 展示
plt.figure(figsize=(10, 5))
librosa.display.specshow(DB, sr=sr, x_axis="time", y_axis="linear", cmap="inferno")
plt.colorbar(format="%+2.0f dB")
plt.title("Spectrogram")

plt.xlabel("Time")
plt.ylabel("Frequency(Hz)")
plt.tight_layout()
plt.show()
