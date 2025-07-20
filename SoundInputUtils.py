import aubio
import pyaudio
import sys
import numpy as np

#initialize pyaudio
p = pyaudio.PyAudio()

class SoundInputUtils:
	def __init__(self):
		# open stream
		self.buffer_size = 1024
		self.pyaudio_format = pyaudio.paFloat32
		self.n_channels = 1
		self.samplerate = 16000
		self.stream = None
		self.volume = 0
		self.currentlyJumping = False

	def __del__(self):
		pass

#def main(args):

	
	


	#while True:
		
		#format volume so only displays at most six numbers behind 0
		#volume = "{:6f}".format(volume)
		#print("|" * int(volume))

		#print(str(volume))

#if __name__ == "__main__": main(sys.argv)

	def madeSound(self):
		if self.volume > 15 and self.currentlyJumping==False:
			self.currentlyJumping = True
			return True
		elif self.volume<15 and self.currentlyJumping==True:
			self.currentlyJumping=False

	def openStream(self):
		self.stream = p.open(format=self.pyaudio_format,
						channels = self.n_channels,
						rate = self.samplerate,
						input = True,
						frames_per_buffer=self.buffer_size)

	def listen(self):
		#Listen to the stream
		data = self.stream.read(self.buffer_size//2, exception_on_overflow=False)
		samples = np.fromstring(data, dtype=aubio.float_type)
		self.volume = np.sum(samples**2)/len(samples)
		self.volume = self.volume * 1000
		#print("|" * int(self.volume))

	def closeStream(self):
		self.stream.stop_stream()
		self.stream.close()
		self.volume = 0


