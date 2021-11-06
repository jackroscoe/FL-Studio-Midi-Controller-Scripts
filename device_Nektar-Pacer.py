# name=Nektar Pacer
# url=https://forum.image-line.com/viewtopic.php?p=1483607#p1483607

# This import section is loading the back-end code required to execute the script. You may not need all modules that are available for all scripts.

import transport
import mixer
import ui
import midi

#The next two variables are constants defined up here so you don't need to go hunting in the script to find them later. Good habit. 
#You can name these as you like, so long as you use them in the script below as written ...

Faders_UpNote = 48 # All faders up midi note number
Faders_DownNote = 50  # All faders midi down note number

Transport_PlayNote = 94 # Play button
Transport_StopNote = 93 # Stop button
Transport_LoopRecordingNote = 86 # Enable/Disable Loop Recording
Transport_RecordNote = 95 # Record

class TSimple():

	def OnMidiMsg(self, event):

		event.handled = True
		if event.midiId == midi.MIDI_NOTEON:
			if (event.pmeFlags & midi.PME_System != 0):
				print(event.data1, event.data2)
				if event.data1 == Faders_UpNote:  #All faders UP
					ui.showWindow(midi.widMixer)
					for n in range(1, 50): #Sets the Mixer Channel range to be changed. (first channel, last channel). 0 is the Master.
						mixer.setTrackVolume(n, 0.65) #Sets each channel to 65%
				elif event.data1 == Faders_DownNote: #All faders down dim
					ui.showWindow(midi.widMixer)
					for n in range(1, 50): #Sets the Mixer Channel range to be changed. (first channel, last channel). 0 is the Master.
						mixer.setTrackVolume(n, 0.25) #Sets each channel to 25%
				elif event.data1 == Transport_PlayNote:
					if not transport.isPlaying():
						transport.start()
						event.handled = True
				elif event.data1 == Transport_StopNote:
					if transport.isPlaying():
						transport.stop()
						event.handled = True
				elif event.data1 == Transport_RecordNote:
					transport.record()
			else:
				event.handled = False
		else:
			event.handled = False

Simple = TSimple()

def OnMidiMsg(event):
	Simple.OnMidiMsg(event)

