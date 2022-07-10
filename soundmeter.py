#https://stackoverflow.com/questions/70502339/how-would-i-find-the-current-decibel-level-and-set-it-as-a-variable/70514219#70514219
import pyaudio
import time
from math import log10
import audioop  
import numpy
import librosa


p = pyaudio.PyAudio()
WIDTH = 2
RATE = int(p.get_default_input_device_info()['defaultSampleRate'])
DEVICE = p.get_default_input_device_info()['index']
rms = 0
counter = 0
decoded = []
mfcc = []

print("=== Soundmeter Started ===")
print(p.get_default_input_device_info())

def callback(in_data, frame_count, time_info, status):
    global rms
    global decoded
    #decoded = numpy.frombuffer(in_data, dtype=numpy.float)
    decoded = numpy.frombuffer(in_data, dtype=numpy.short).astype(float)
    rms = audioop.rms(in_data, WIDTH) / 32767
    return in_data, pyaudio.paContinue

stream = p.open(format=p.get_format_from_width(WIDTH),
                input_device_index=DEVICE,
                channels=1,
                rate=RATE,
                input=True,
                output=False,
                stream_callback=callback)

stream.start_stream()
 
while stream.is_active(): 


    zero_crosses = (numpy.where(numpy.sign(decoded[:-1]) != numpy.sign(decoded[1:]))[0] + 1).size
    mfcc = librosa.feature.mfcc(y=numpy.array(decoded), sr=RATE)
    
    print(len(decoded))
    print(len(mfcc))
    
    if rms==0:
        print(f"RMS: {0} DB: {0}  ZCR: {zero_crosses} Datapoint: {counter}") 
    else:
        db = 20 * log10(rms)
        print(f"RMS: {rms} DB: {db} ZCR: {zero_crosses} Datapoint: {counter}") 


    time.sleep(1)
    counter+=1
        

stream.stop_stream()
stream.close()

p.terminate()