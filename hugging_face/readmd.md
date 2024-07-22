## For getting only output token we need to used following commands

- return_full_text=False

```Python
pipe = pipeline('text-generation', model=model_name, tokenizer=model_name, device=0)
output = pipe(
    prompt,
    max_length=1000,
    num_return_sequences=1,
    top_k=50,
    top_p=0.95,
    temperature=0.5,
    do_sample=True,
    return_full_text=False
)
```

## Open source llm with streaming

https://colab.research.google.com/drive/1thc-2vC2Bspb6LbaW7sU9gAfMzB49SNT#scrollTo=HcAQkZUE7deN
https://github.com/langchain-ai/langchain/issues/2918

## To get llm model input structure

```Python
user_query = "what is data science ?"
chat = [
   {"role": "system", "content": "You are a conversational AI assistant that is provided a list of documents and a user query to answer based on information from the documents. The user also provides an answer mode which can be 'Grounded' or 'Mixed'. For answer mode Grounded only respond with exact facts from documents, for answer mode Mixed answer using facts from documents and your own knowledge. Cite all facts from the documents using <co: doc_id></co> tags."},
   {"role": "user", "content": user_query}
]
prompt = tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)
```

Output :

```Terminal
<|start_header_id|>system<|end_header_id|>

You are a conversational AI assistant<|eot_id|><|start_header_id|>user<|end_header_id|>

what is data science ?<|eot_id|><|start_header_id|>assistant<|end_header_id|>


```
