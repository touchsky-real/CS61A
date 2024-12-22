from wave import open
from struct import Struct
from math import floor

frame_rate = 11025  # 每秒采样次数

def encode(x):
    """将 -1 到 1 之间的浮点数编码为两个字节（16 位有符号整数）。"""
    i = int(16384 * x)
    return Struct('h').pack(i)

def play(sampler, name='song.wav', seconds=2):
    """将采样器函数的输出写入 WAV 文件。"""
    out = open(name, 'wb')
    out.setnchannels(1)  # 单声道
    out.setsampwidth(2)  # 每帧 2 字节（16 位）
    out.setframerate(frame_rate)  # 设置采样率

    t = 0
    while t < seconds * frame_rate:
        sample = sampler(t)
        out.writeframes(encode(sample))
        t += 1

    out.close()

def tri(frequency, amplitude=0.05):
    """生成一个连续的三角波。"""
    period = frame_rate // frequency

    def sampler(t):
        saw_wave = t / period - floor(t/period + 0.5)
        tri_wave = 2 * abs(2 * saw_wave - 1) - 1
        return amplitude * tri_wave

    return sampler

def both(f, g):
    """返回一个函数，合成两个采样器 f 和 g 的结果。"""
    return lambda t: f(t) + g(t)

def note(f, start, end, fade=0.01):
    """生成一个音符，控制音符的开始、结束和渐变。"""
    def sampler(t):
        seconds = t / frame_rate
        if seconds < start:
            return 0
        elif seconds > end:
            return 0
        elif seconds < start + fade:
            return (seconds - start) / fade * f(t)
        elif seconds > end - fade:
            return (end - seconds) / fade * f(t)
        else:
            return f(t)
    return sampler

def mario_at(octave):
    """根据 octave 创建 Mario 风格的音符序列。"""
    c = tri(octave * 261.63)  # 高音 C
    e = tri(octave * 329.63)  # 高音 E
    g = tri(octave * 392.00)  # 高音 G
    low_g = tri(octave * 392.00 / 2)  # 低音 G

    return mario(c, e, g, low_g)

def mario(c, e, g, low_g):
    """生成 Mario 风格的音符序列。"""
    song = note(e, 0, 1/8)  # 创建第一个音符：E，持续 1/8 秒
    z = 1/8  # 用于控制音符间隔

    song = both(song, note(e, z, z + 1/8))  # E 音符，1/8 秒后
    z += 1/8
    song = both(song, note(e, z, z + 1/8))  # 再添加 E 音符，持续 1/8 秒
    z += 1/4
    song = both(song, note(c, z, z + 1/8))  # C 音符，持续 1/8 秒
    z += 1/8
    song = both(song, note(e, z, z + 1/8))  # E 音符，持续 1/8 秒
    z += 1/4
    song = both(song, note(g, z, z + 1/4))  # G 音符，持续 1/4 秒
    z += 1/2
    song = both(song, note(low_g, z, z + 1/4))  # 低音 G 音符，持续 1/4 秒
    z += 1/2

    return song  # 返回完整的歌曲

# 播放 Mario 风格的音乐
play(mario_at(1))  # octave = 1 为标准音阶
