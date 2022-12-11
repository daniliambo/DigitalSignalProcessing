import numpy as np

np.random.seed(seed=1)
sample_rate = 44100
frequency = 82.41
sec = 2
gen_len = sample_rate * sec
noise = (2 * np.random.uniform(-1, 1, int(sample_rate / frequency)))  # [-1, 1]
print(noise)


def karplus_strong(noise, N):
    # Noise - input
    # N - number of samples to generate
    # return y - generated signal based on Noise
    # YOUR CODE HERE
    print(1)
    samples = np.zeros(int(gen_len))
    for i in range(len(noise)):
        samples[i] = noise[i]
    print('len(samples):', len(samples))
    print(len(noise))
    for i in range(len(noise), len(samples)):
        # В начале i меньше длины шума, поэтому мы берем значения из шума.
        # Но потом, когда i больше длины шума, мы уже берем посчитанные нами новые значения.
        samples[i] = (samples[i - len(noise)] + samples[i - len(noise) - 1]) / 2
    return samples


print(karplus_strong(noise, gen_len))
