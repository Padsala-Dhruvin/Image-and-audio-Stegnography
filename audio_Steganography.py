import wave
def Do_lsb(msg_bits,frame_bytes):

	for i, bit in enumerate(msg_bits):
		frame_bytes[i] = (frame_bytes[i] & 254) | bit

	return(bytes(frame_bytes))


def Undo_lsb(frame_bytes):
	
	for i in range(len(frame_bytes)):
		frame_bytes[i] = (frame_bytes[i] & 1)
	
	return(frame_bytes)

def into_Bits_Array(string):

	string_bits = ""
	for i in string:
		string_bits = string_bits + bin(ord(i)).lstrip('0b').rjust(8,"0")
	text_msg_bits_array = list(map(int, "".join(string_bits))) 

	return(text_msg_bits_array)
	
def into_String(bytes):

	string_bits = ""
	for i in range(0,len(bytes),8):
		string_bits = string_bits + chr(int("".join(map(str,bytes[i:i+8])),2))
	text_string_bits = "".join(string_bits)
	
	return(text_string_bits)

def msg_Embed(audio_name,text_msg):
	audio = wave.open(audio_name, mode='rb')
	audio_Frames_Bytes = bytearray(list(audio.readframes(audio.getnframes())))
	
	text_msg = text_msg + int((len(audio_Frames_Bytes)/8)-(len(text_msg)*8)) *'@'
	
	text_msg_bits = into_Bits_Array(text_msg)
	
	Frames_with_Msg = Do_lsb(text_msg_bits,audio_Frames_Bytes)
	
	with wave.open("Stego"+audio_name, mode='wb') as sm:
		sm.setparams(audio.getparams())
		sm.writeframes(Frames_with_Msg)
	audio.close()
	
def msg_Extract(audio_name):
	audio = wave.open(audio_name, mode='rb')
	audio_Frames_Bytes = bytearray(list(audio.readframes(audio.getnframes())))
	msg_Bytes = Undo_lsb(audio_Frames_Bytes)
	msg_String = into_String(msg_Bytes)
	msg_Text = msg_String.split("@@@@")[0]
	return(msg_Text)
	audio.close()
	


Enter_filename = input("Enter audio_file Name:")
user_Choice = int(input("1.Embed or 2.Extract :"))
if user_Choice == 1 :
	Stego_Message = input("Enter Text to be embedded:")
	msg_Embed(Enter_filename,Stego_Message)
	print("Message successfully hidden")
elif user_Choice == 2 :
	Stego_Text = msg_Extract(Enter_filename)
	print("Extracted Message :" +Stego_Text)
	
	