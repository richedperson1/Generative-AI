
# Oh, or you could use transformers.TextIteratorSteamer which also provides an iterator: https://huggingface.co/docs/transformers/main/en/internal/generation_utils#transformers.TextIteratorStreamer

from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer
from threading import Thread

tok = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained("gpt2")
inputs = tok(["An increasing sequence: one,"], return_tensors="pt")
streamer = TextIteratorStreamer(tok)

# Run the generation in a separate thread, so that we can fetch the generated text in a non-blocking way.
generation_kwargs = dict(inputs, streamer=streamer, max_new_tokens=20)
thread = Thread(target=model.generate, kwargs=generation_kwargs)
thread.start()
generated_text = ""
for new_text in streamer:
    generated_text += new_text
    
    


