#!/usr/bin/env python3
import os
import subprocess
import numpy as np
from scipy import signal
from scipy.io import wavfile

SAMPLE_RATE = 44100
OUT_DIR = "docs/assets/audio"
os.makedirs(OUT_DIR, exist_ok=True)

def save_wav_to_mp3(audio_data, wav_path, mp3_path):
    # Normalize to 0.85 peak
    audio_data = audio_data.astype(np.float32)
    max_val = np.max(np.abs(audio_data))
    if max_val > 0:
        audio_data = (audio_data / max_val) * 0.85
    int_data = (audio_data * 32767).astype(np.int16)
    wavfile.write(wav_path, SAMPLE_RATE, int_data)
    subprocess.run(["ffmpeg", "-y", "-i", wav_path, "-codec:a", "libmp3lame", "-qscale:a", "2", mp3_path],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    if os.path.exists(wav_path):
        os.remove(wav_path)
    print(f"Generated: {mp3_path}")

# ==========================================
# 1. 森林深處清溪流淌與樹冠微風 (16秒無縫循環)
# ==========================================
def generate_forest_stream(duration=16.0):
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    n_samples = len(t)
    
    # 溪流水聲：多頻段粉紅噪聲 + 湧動調製
    white_l = np.random.randn(n_samples)
    white_r = np.random.randn(n_samples)
    
    # 模擬水流的 3 個主要共振帶 (350Hz 低吟、900Hz 潺潺、2400Hz 飛沫)
    def filter_band(data, low, high):
        b, a = signal.butter(2, [low / (SAMPLE_RATE/2), high / (SAMPLE_RATE/2)], btype='band')
        return signal.lfilter(b, a, data)
    
    # 水流主體
    stream_low = filter_band(white_l, 250, 600) * 0.5
    stream_mid = filter_band(white_l, 650, 1500) * 0.7
    stream_high = filter_band(white_l, 1600, 3800) * 0.4
    
    # 水流波動調製 (緩慢起伏)
    mod1 = 0.7 + 0.3 * np.sin(2 * np.pi * 0.35 * t)
    mod2 = 0.8 + 0.2 * np.sin(2 * np.pi * 0.82 * t + 1.2)
    stream_l = (stream_low + stream_mid * mod1 + stream_high * mod2)
    
    stream_low_r = filter_band(white_r, 250, 600) * 0.5
    stream_mid_r = filter_band(white_r, 650, 1500) * 0.7
    stream_high_r = filter_band(white_r, 1600, 3800) * 0.4
    mod3 = 0.7 + 0.3 * np.sin(2 * np.pi * 0.41 * t + 0.8)
    stream_r = (stream_low_r + stream_mid_r * mod3 + stream_high_r * mod1)
    
    # 加入天然小水滴泡泡聲 (Poisson 分佈)
    np.random.seed(42)
    num_bubbles = int(duration * 12)
    bubble_times = np.random.uniform(0.2, duration - 0.2, num_bubbles)
    for bt in bubble_times:
        start_idx = int(bt * SAMPLE_RATE)
        bubble_len = int(SAMPLE_RATE * np.random.uniform(0.025, 0.06))
        if start_idx + bubble_len >= n_samples:
            continue
        tb = np.linspace(0, bubble_len / SAMPLE_RATE, bubble_len)
        f_start = np.random.uniform(700, 1400)
        f_end = f_start * np.random.uniform(1.2, 1.8)
        # 泡泡上升正弦波
        freq = np.linspace(f_start, f_end, bubble_len)
        phase = np.cumsum(2 * np.pi * freq / SAMPLE_RATE)
        env = np.exp(-tb * 70) * (tb / (bubble_len / SAMPLE_RATE))
        bubble = np.sin(phase) * env * np.random.uniform(0.15, 0.35)
        pan = np.random.uniform(0.2, 0.8)
        stream_l[start_idx:start_idx+bubble_len] += bubble * (1 - pan)
        stream_r[start_idx:start_idx+bubble_len] += bubble * pan

    # 樹冠深林微風 (超低頻深邃呼嘯)
    b_wind, a_wind = signal.butter(1, 180 / (SAMPLE_RATE/2), btype='low')
    wind_l = signal.lfilter(b_wind, a_wind, np.random.randn(n_samples)) * (0.6 + 0.4 * np.sin(2 * np.pi * 0.12 * t))
    wind_r = signal.lfilter(b_wind, a_wind, np.random.randn(n_samples)) * (0.6 + 0.4 * np.sin(2 * np.pi * 0.09 * t + 1))
    
    out_l = stream_l * 0.75 + wind_l * 0.25
    out_r = stream_r * 0.75 + wind_r * 0.25
    
    # 做 1 秒無縫交叉淡入淡出 (Seamless loop crossfade)
    fade_len = int(SAMPLE_RATE * 1.0)
    fade_in = np.linspace(0, 1, fade_len)
    fade_out = np.linspace(1, 0, fade_len)
    
    out_l[:fade_len] = out_l[:fade_len] * fade_in + out_l[-fade_len:] * fade_out
    out_r[:fade_len] = out_r[:fade_len] * fade_in + out_r[-fade_len:] * fade_out
    out_l = out_l[:-fade_len]
    out_r = out_r[:-fade_len]
    
    stereo = np.column_stack([out_l, out_r])
    save_wav_to_mp3(stereo, "/tmp/stream.wav", os.path.join(OUT_DIR, "forest_stream_deep.mp3"))

# ==========================================
# 2. 林間清脆鳥鳴 (林鳥、柳鶯、山雀婉轉啼鳴)
# ==========================================
def generate_birdsong(duration=6.0):
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    n_samples = len(t)
    audio = np.zeros(n_samples)
    
    def add_chirp(start_time, f1, f2, dur, vibrato_depth=35, vibrato_rate=25):
        s_idx = int(start_time * SAMPLE_RATE)
        c_len = int(dur * SAMPLE_RATE)
        if s_idx + c_len >= n_samples: return
        tc = np.linspace(0, dur, c_len)
        freq = np.linspace(f1, f2, c_len) + vibrato_depth * np.sin(2 * np.pi * vibrato_rate * tc)
        phase = np.cumsum(2 * np.pi * freq / SAMPLE_RATE)
        env = np.clip(np.sin(np.pi * tc / dur), 0, 1) ** 1.8
        chirp = (np.sin(phase) + 0.15 * np.sin(2 * phase)) * env
        audio[s_idx:s_idx+c_len] += chirp
        
    # 第一段：山雀輕快三連音 (啾、啾、啾)
    add_chirp(0.4, 3800, 4800, 0.12)
    add_chirp(0.65, 4100, 5200, 0.14)
    add_chirp(0.92, 4600, 3600, 0.22)
    
    # 第二段：柳鶯婉轉長啼 (清靈滑音)
    add_chirp(2.2, 3200, 4600, 0.28, vibrato_depth=60, vibrato_rate=32)
    add_chirp(2.6, 4500, 3400, 0.35, vibrato_depth=80, vibrato_rate=30)
    add_chirp(3.1, 3800, 4900, 0.18)
    
    # 第三段：遠處回響一聲短啼
    add_chirp(4.4, 4200, 3500, 0.15)
    add_chirp(4.7, 3600, 4300, 0.20)
    
    # 輕微立體聲環境混響
    stereo = np.column_stack([audio * 0.9, audio * 0.7])
    save_wav_to_mp3(stereo, "/tmp/birds.wav", os.path.join(OUT_DIR, "birds_woodland.mp3"))

# ==========================================
# 3. 溪畔樹蛙鳴叫 (清晨溪石蛙鳴，真實喉音)
# ==========================================
def generate_frogs(duration=5.0):
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    n_samples = len(t)
    audio = np.zeros(n_samples)
    
    def add_croak(start_time, dur=0.25, base_freq=520, pulse_rate=34):
        s_idx = int(start_time * SAMPLE_RATE)
        c_len = int(dur * SAMPLE_RATE)
        if s_idx + c_len >= n_samples: return
        tc = np.linspace(0, dur, c_len)
        # 脈衝序列調製 (模擬蛙鳴特有的喉部聲囊顫動)
        pulse = 0.5 + 0.5 * signal.sawtooth(2 * np.pi * pulse_rate * tc)
        carrier = (np.sin(2 * np.pi * base_freq * tc) + 
                   0.6 * np.sin(2 * np.pi * (base_freq * 2) * tc) + 
                   0.3 * np.sin(2 * np.pi * (base_freq * 3) * tc))
        env = np.sin(np.pi * tc / dur) ** 2
        audio[s_idx:s_idx+c_len] += carrier * pulse * env
        
    # 兩隻蛙對鳴 (一遠一近)
    add_croak(0.5, dur=0.24, base_freq=480, pulse_rate=32)
    add_croak(0.85, dur=0.28, base_freq=510, pulse_rate=35)
    add_croak(1.3, dur=0.32, base_freq=490, pulse_rate=33)
    
    add_croak(2.8, dur=0.22, base_freq=620, pulse_rate=42)
    add_croak(3.15, dur=0.26, base_freq=640, pulse_rate=45)
    
    stereo = np.column_stack([audio * 0.85, audio * 0.65])
    save_wav_to_mp3(stereo, "/tmp/frogs.wav", os.path.join(OUT_DIR, "frogs_stream.mp3"))

# ==========================================
# 4. 動物特徵腳步聲與出場音效
# ==========================================
def generate_deer_steps():
    # 梅花鹿：清脆優雅蹄聲踏草輕踩 (嗒...嗒...嗒...)
    duration = 4.0
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    audio = np.zeros(len(t))
    step_times = [0.4, 1.2, 2.1, 3.0]
    for st in step_times:
        s_idx = int(st * SAMPLE_RATE)
        c_len = int(0.12 * SAMPLE_RATE)
        tc = np.linspace(0, 0.12, c_len)
        # 蹄擊 (高Q共振) + 草葉摩擦 (帶通噪聲)
        click = np.sin(2 * np.pi * 820 * tc) * np.exp(-tc * 65)
        rustle = signal.lfilter(*signal.butter(2, [1200/(SAMPLE_RATE/2), 3500/(SAMPLE_RATE/2)], 'band'), np.random.randn(c_len)) * np.exp(-tc * 35) * 0.4
        step = (click * 0.6 + rustle * 0.4)
        audio[s_idx:s_idx+c_len] += step
    stereo = np.column_stack([audio, audio * 0.85])
    save_wav_to_mp3(stereo, "/tmp/steps_deer.wav", os.path.join(OUT_DIR, "steps_deer.mp3"))

def generate_rabbit_steps():
    # 萌兔好奇：輕巧蹦跳輕踏聲 (噗、噗、噗)
    duration = 3.5
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    audio = np.zeros(len(t))
    hop_times = [0.3, 0.95, 1.7, 2.5]
    for ht in hop_times:
        s_idx = int(ht * SAMPLE_RATE)
        c_len = int(0.14 * SAMPLE_RATE)
        tc = np.linspace(0, 0.14, c_len)
        # 兔爪軟肉墊踏草 (低頻噗噗聲 + 微弱草葉聲)
        thud = np.sin(2 * np.pi * 170 * tc) * np.exp(-tc * 45)
        leaf = signal.lfilter(*signal.butter(2, [800/(SAMPLE_RATE/2), 2400/(SAMPLE_RATE/2)], 'band'), np.random.randn(c_len)) * np.exp(-tc * 40) * 0.35
        audio[s_idx:s_idx+c_len] += (thud * 0.7 + leaf * 0.3)
    stereo = np.column_stack([audio * 0.85, audio])
    save_wav_to_mp3(stereo, "/tmp/steps_rabbit.wav", os.path.join(OUT_DIR, "steps_rabbit.mp3"))

def generate_otter_sound():
    # 水獺：溪石水花輕濺、水面游動划水 (嘩啦、咕嚕)
    duration = 3.8
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    audio = np.zeros(len(t))
    # 兩次水花探頭
    for st in [0.4, 1.8]:
        s_idx = int(st * SAMPLE_RATE)
        c_len = int(0.6 * SAMPLE_RATE)
        tc = np.linspace(0, 0.6, c_len)
        splash_noise = signal.lfilter(*signal.butter(2, [600/(SAMPLE_RATE/2), 4200/(SAMPLE_RATE/2)], 'band'), np.random.randn(c_len))
        env = (tc / 0.1) * np.exp(-tc * 7)
        bubble = np.sin(2 * np.pi * np.linspace(1100, 600, c_len) * tc) * np.exp(-tc * 12) * 0.4
        audio[s_idx:s_idx+c_len] += (splash_noise * env * 0.7 + bubble * 0.3)
    stereo = np.column_stack([audio, audio * 0.9])
    save_wav_to_mp3(stereo, "/tmp/steps_otter.wav", os.path.join(OUT_DIR, "steps_otter.mp3"))

def generate_sparrows_sound():
    # 靈動麻雀：拍翅撲稜聲 (撲撲撲) ＋ 兩聲清脆啾啾啼鳴
    duration = 3.5
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    audio = np.zeros(len(t))
    # 降落拍翅 (15次微小撲稜聲)
    flap_start = 0.2
    for i in range(12):
        s_idx = int((flap_start + i * 0.045) * SAMPLE_RATE)
        c_len = int(0.04 * SAMPLE_RATE)
        tc = np.linspace(0, 0.04, c_len)
        flap = signal.lfilter(*signal.butter(2, [300/(SAMPLE_RATE/2), 1600/(SAMPLE_RATE/2)], 'band'), np.random.randn(c_len)) * np.sin(np.pi * tc / 0.04)
        audio[s_idx:s_idx+c_len] += flap * 0.5
    # 落地後雀躍啼鳴 (啾！啾！)
    def add_chirp(st, f1, f2):
        s_idx = int(st * SAMPLE_RATE)
        c_len = int(0.08 * SAMPLE_RATE)
        tc = np.linspace(0, 0.08, c_len)
        freq = np.linspace(f1, f2, c_len)
        audio[s_idx:s_idx+c_len] += np.sin(2 * np.pi * freq * tc) * np.sin(np.pi * tc / 0.08) * 0.6
    add_chirp(1.1, 4800, 3200)
    add_chirp(1.35, 3600, 5200)
    add_chirp(2.1, 4200, 4900)
    stereo = np.column_stack([audio * 0.95, audio * 0.8])
    save_wav_to_mp3(stereo, "/tmp/steps_sparrows.wav", os.path.join(OUT_DIR, "steps_sparrows.mp3"))

def generate_redpandas_steps():
    # 小熊貓：厚爪輕踩倒木抓抓聲、木頭摩擦聲
    duration = 3.5
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    audio = np.zeros(len(t))
    step_times = [0.4, 0.9, 1.5, 2.1, 2.7]
    for st in step_times:
        s_idx = int(st * SAMPLE_RATE)
        c_len = int(0.1 * SAMPLE_RATE)
        tc = np.linspace(0, 0.1, c_len)
        wood_tap = np.sin(2 * np.pi * 380 * tc) * np.exp(-tc * 50)
        scratch = signal.lfilter(*signal.butter(2, [1400/(SAMPLE_RATE/2), 4000/(SAMPLE_RATE/2)], 'band'), np.random.randn(c_len)) * np.exp(-tc * 60) * 0.4
        audio[s_idx:s_idx+c_len] += (wood_tap * 0.6 + scratch * 0.4)
    stereo = np.column_stack([audio * 0.85, audio])
    save_wav_to_mp3(stereo, "/tmp/steps_redpandas.wav", os.path.join(OUT_DIR, "steps_redpandas.mp3"))

def generate_leopard_cat_steps():
    # 台灣石虎：極輕柔的貓科軟肉墊潛步、微弱落葉摩擦聲 (靜謐優雅)
    duration = 4.0
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    audio = np.zeros(len(t))
    step_times = [0.5, 1.4, 2.3, 3.2]
    for i, st in enumerate(step_times):
        s_idx = int(st * SAMPLE_RATE)
        c_len = int(0.09 * SAMPLE_RATE)
        tc = np.linspace(0, 0.09, c_len)
        soft_pad = np.sin(2 * np.pi * 140 * tc) * np.exp(-tc * 55)
        leaf_rustle = signal.lfilter(*signal.butter(2, [1100/(SAMPLE_RATE/2), 3200/(SAMPLE_RATE/2)], 'band'), np.random.randn(c_len)) * np.exp(-tc * 45) * 0.25
        # 第2步踩到細小樹枝微脆折聲
        twig = 0
        if i == 1:
            twig = np.sin(2 * np.pi * 1800 * tc[:int(c_len*0.3)]) * np.exp(-tc[:int(c_len*0.3)] * 180) * 0.35
            audio[s_idx:s_idx+len(twig)] += twig
        audio[s_idx:s_idx+c_len] += (soft_pad * 0.6 + leaf_rustle * 0.4)
    stereo = np.column_stack([audio, audio * 0.9])
    save_wav_to_mp3(stereo, "/tmp/steps_leopard_cat.wav", os.path.join(OUT_DIR, "steps_leopard_cat.mp3"))

def generate_bear_steps():
    # 大黑熊：沈穩厚重大熊步伐踏地聲 (咚... 咚...)
    duration = 4.5
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    audio = np.zeros(len(t))
    step_times = [0.6, 1.8, 3.0]
    for st in step_times:
        s_idx = int(st * SAMPLE_RATE)
        c_len = int(0.35 * SAMPLE_RATE)
        tc = np.linspace(0, 0.35, c_len)
        sub_thud = np.sin(2 * np.pi * 65 * tc) * np.exp(-tc * 14)
        body_weight = signal.lfilter(*signal.butter(2, [90/(SAMPLE_RATE/2), 350/(SAMPLE_RATE/2)], 'band'), np.random.randn(c_len)) * np.exp(-tc * 16) * 0.7
        audio[s_idx:s_idx+c_len] += (sub_thud * 0.5 + body_weight * 0.5)
    stereo = np.column_stack([audio * 0.9, audio])
    save_wav_to_mp3(stereo, "/tmp/steps_bear.wav", os.path.join(OUT_DIR, "steps_bear.mp3"))

def generate_beaver_sound():
    # 河狸：溪畔細啃樹枝卡滋卡滋聲與溪石微踏
    duration = 4.0
    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    audio = np.zeros(len(t))
    # 細啃樹枝咀嚼
    chew_times = [0.3, 0.5, 0.75, 1.1, 1.35, 1.6, 2.2, 2.45, 2.8]
    for ct in chew_times:
        s_idx = int(ct * SAMPLE_RATE)
        c_len = int(0.045 * SAMPLE_RATE)
        tc = np.linspace(0, 0.045, c_len)
        nibble = np.sin(2 * np.pi * np.random.uniform(1600, 2800) * tc) * np.exp(-tc * 120) * 0.5
        audio[s_idx:s_idx+c_len] += nibble
    stereo = np.column_stack([audio, audio * 0.9])
    save_wav_to_mp3(stereo, "/tmp/steps_beaver.wav", os.path.join(OUT_DIR, "steps_beaver.mp3"))

if __name__ == "__main__":
    print("Generating pristine forest sound library...")
    generate_forest_stream()
    generate_birdsong()
    generate_frogs()
    generate_deer_steps()
    generate_rabbit_steps()
    generate_otter_sound()
    generate_sparrows_sound()
    generate_redpandas_steps()
    generate_leopard_cat_steps()
    generate_bear_steps()
    generate_beaver_sound()
    print("All forest audio generated successfully!")
