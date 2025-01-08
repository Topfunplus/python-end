import librosa
import librosa.display
import matplotlib.pyplot as plt

# 音频文件的路径
audio_path = "audio.wav"

# 加载音频文件 y是音频数据 sr是采样率
y, sr = librosa.load(audio_path, sr=None)

# 计算短时傅里叶变换
D = librosa.stft(y)

# 将幅度转换为分贝
DB = librosa.amplitude_to_db(abs(D))
DB = DB.min()
DB /= DB.max()


# 设置 matplotlib 图形的大小
plt.figure(figsize=(10, 5))
# 显示频谱图
librosa.display.specshow(DB, sr=sr, x_axis="time", y_axis="linear", cmap="inferno")
# 添加颜色条
plt.colorbar(format="%+2.0f dB")

# 设置标题
plt.title("Spectrogram")

# 设置x轴和y轴的标签
plt.xlabel("Time")
plt.ylabel("Frequency(Hz)")

# 显示图形
plt.tight_layout()
plt.show()
