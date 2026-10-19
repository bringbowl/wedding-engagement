#!/usr/bin/env python3
import os
import subprocess
import numpy as np
from scipy.io import wavfile

SAMPLE_RATE = 44100
TARGET_DURATION = 60.0  # 60 秒高音質真實大自然音效循環
TARGET_SAMPLES = int(SAMPLE_RATE * TARGET_DURATION)
CROSSFADE_SEC = 2.0
CROSSFADE_SAMPLES = int(SAMPLE_RATE * CROSSFADE_SEC)

OUT_DIR = "docs/assets/audio"
os.makedirs(OUT_DIR, exist_ok=True)
OUT_MP3 = os.path.join(OUT_DIR, "forest_nature_ambient.mp3")

# 1. 讀取並標準化音軌為 float 格式
sr1, stream_raw = wavfile.read('/tmp/stream1.wav')
sr2, birds_raw = wavfile.read('/tmp/birds.wav')
sr3, frogs_raw = wavfile.read('/tmp/frogs.wav')

stream_data = stream_raw.astype(np.float32) / 32768.0
birds_data = birds_raw.astype(np.float32) / 32768.0
frogs_data = frogs_raw.astype(np.float32) / 32768.0

# 2. 將 17.8 秒的真實溪流流水聲做無縫拼貼循環至 60 秒
stream_loop = np.zeros((TARGET_SAMPLES + CROSSFADE_SAMPLES, 2), dtype=np.float32)
stream_len = len(stream_data)
s_pos = 0
step_len = stream_len - CROSSFADE_SAMPLES
fade_in = np.linspace(0, 1, CROSSFADE_SAMPLES)[:, None]
fade_out = np.linspace(1, 0, CROSSFADE_SAMPLES)[:, None]

while s_pos < len(stream_loop):
    end_pos = min(s_pos + stream_len, len(stream_loop))
    take_len = end_pos - s_pos
    if s_pos == 0:
        stream_loop[:take_len] = stream_data[:take_len]
    else:
        # 重疊淡入淡出
        cf_len = min(CROSSFADE_SAMPLES, take_len)
        stream_loop[s_pos:s_pos+cf_len] = (stream_loop[s_pos:s_pos+cf_len] * fade_out[:cf_len] +
                                            stream_data[:cf_len] * fade_in[:cf_len])
        if take_len > cf_len:
            stream_loop[s_pos+cf_len:end_pos] = stream_data[cf_len:take_len]
    s_pos += step_len

# 3. 擷取 60 秒真實林鳥啼鳴 (birds)
birds_track = birds_data[:TARGET_SAMPLES + CROSSFADE_SAMPLES]
if len(birds_track) < TARGET_SAMPLES + CROSSFADE_SAMPLES:
    birds_track = np.pad(birds_track, ((0, TARGET_SAMPLES + CROSSFADE_SAMPLES - len(birds_track)), (0, 0)))

# 4. 擷取真實溪畔樹蛙鳴叫 (frogs)，調製出自然的出現節奏 (不喧賓奪主，間歇性低鳴)
frogs_track = np.zeros_like(birds_track)
# 在 10~25 秒、40~55 秒讓蛙鳴自然浮現
t_axis = np.linspace(0, (len(frogs_track))/SAMPLE_RATE, len(frogs_track))
frog_env = (np.clip(np.sin(2 * np.pi * t_axis / 28.0), 0, 1) ** 2)[:, None]
frogs_sub = frogs_data[:len(frogs_track)]
frogs_track = frogs_sub * frog_env * 0.45

# 5. 平衡混音比例 (溪流 65% + 鳥鳴 85% + 蛙鳴 35%)
mixed = stream_loop[:len(birds_track)] * 0.65 + birds_track * 0.85 + frogs_track * 0.35

# 6. 做整段 60 秒的首尾無縫循環處理 (Seamless 60s Loop)
main_track = mixed[:TARGET_SAMPLES].copy()
tail = mixed[TARGET_SAMPLES:TARGET_SAMPLES + CROSSFADE_SAMPLES]

main_track[:CROSSFADE_SAMPLES] = (main_track[:CROSSFADE_SAMPLES] * fade_in +
                                  tail * fade_out)

# 7. 峰值防破音保護與標準化 (-1.0 dB)
peak = np.max(np.abs(main_track))
if peak > 0:
    main_track = (main_track / peak) * 0.89

# 8. 儲存為高品質立體聲 MP3
wav_temp = "/tmp/real_forest_ambient.wav"
wavfile.write(wav_temp, SAMPLE_RATE, (main_track * 32767).astype(np.int16))
subprocess.run(["ffmpeg", "-y", "-i", wav_temp, "-codec:a", "libmp3lame", "-b:a", "192k", OUT_MP3],
               check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
if os.path.exists(wav_temp):
    os.remove(wav_temp)

print(f"Generated: {OUT_MP3} (Size: {os.path.getsize(OUT_MP3)} bytes, Duration: 60s)")
