import sys
import whisper

# This class handles the communication with the ai model and formats the data before returning it.

# To be able to freely change the underlying AI system we need to the design the class to be able to do so.

# Approach Nr.1: Abstract base class with implementations for each supported model. Cons: Only implemented models are supported
# Approach Nr.2: build a ModelAdapter with generalized commands. Pro: No implementation for each model needed just an iterpretation of the commands.
#                Might be possible to use commands that are the same in a group of ai systems e.g systems that use openAi's tiktoken.


class AutoTranscriber():
  
  def transcribe(file):
    #File not found error due to ffmpeg not being installed
    # -> TODO done: install ffmpeg on windows. Set environment variable
    model = whisper.load_model("turbo")
    print(file)
    result = model.transcribe(file)
    content = result["segments"]
    data = []
    for entry in content:
      data.append([{"speaker": ""}, entry["text"], entry["start"], entry["end"]])
    print(data)
    return data
  
  
  def formatData():
    pass