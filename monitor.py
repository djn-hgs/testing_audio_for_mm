import pyaudio
import pygame

# Sort out a pygame window

pygame.init()

screen = pygame.display.set_mode((800, 300))
clock = pygame.time.Clock()
columns = 64

# Size of buffer in frames

CHUNK = 1024

# Choice of format

FORMAT = pyaudio.paInt8

# Stereo or mono

CHANNELS = 1

# Sample rate

RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("* monitoring")
monitoring = True

while monitoring:
    clock.tick(4)
    for event in pygame.event.get():

        # Check for QUIT event
        if event.type == pygame.QUIT:
            monitoring = False

    data = stream.read(CHUNK)

    width = screen.get_width()/ columns

    max_height = 256
    if max_height > 0:
        height_density = screen.get_height() / max_height
    else:
        height_density = 0

    sub_sample = int(len(data) / columns)

    screen.fill((0,0,0))

    for i in range(columns):
        sample_height = sum(data[i * sub_sample:(i + 1) * sub_sample]) / sub_sample
        pygame.draw.rect(screen, (255, 0, 0), (i * width, 0, width, sample_height * height_density))

    pygame.display.update()

stream.stop_stream()
stream.close()
p.terminate()

