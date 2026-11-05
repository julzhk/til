TIL Downloading open source LLMs: Ollama is a thing.
- 
Getting an LLM to work locally is surprisingly straightforward. 
This has advantages such as allowing experimenting with various models; customising the system prompt; the temperature (eg: randomness); provide background documents to augment the model's  
knowledge and so on. Not to mention the better privacy and security. When the big Gen-AI bubble pops, maybe Ollama (and associated models) will be the only thing left standing.

---
* On a mac: homebrew or [download the installer](https://ollama.com/download).
* Install a model. eg: gemma3:1b (one of the smaller models)
* Open the ollama app for a chat interface.
* want to use the terminal? invoke it with `ollama` which provides the following commands:

```console
Available Commands:
  serve       Start ollama
  create      Create a model
  show        Show information for a model
  run         Run a model
  stop        Stop a running model
  pull        Pull a model from a registry
  push        Push a model to a registry
  signin      Sign in to ollama.com
  signout     Sign out from ollama.com
  list        List models
  ps          List running models
  cp          Copy a model
  rm          Remove a model
  help        Help about any command

Flags:
  -h, --help      help for ollama
  -v, --version   Show version information
  ```

### System Messages

To set a default context (eg 'system message') for the model, use: `/set system`
eg: 

```Console
>>> /show system
No system message was specified for this model.

>>> /set system
you are a pirate

Arrr, shiver me timbers! I am indeed a pirate! I am Captain Byte, and I’m
here to answer your questions... or perhaps, to plunder your mind!

What treasures do ye seek?

>>> /clear
Cleared session context
>>> whats your name
Hello! You can call me Gemma. It’s nice to meet you. 😊
```
---
### Is there a Python API?

Yes indeed! And the Python API allows RAG and vector stores integration quite easily too : see the notebook demo given in the O'Reilly seminar [the seminar notes](https://github.
com/lisabecker/oreilly-webinars) from [the recent informative webinar](https://learning.oreilly.com/live-events/working-locally-with-open-source-llms/0642572007554/0642572264017/).

This snippet shows:
* configure langchain with a particular model
* load and split documents
* create a RetrievalQA chain
* make a query

```python
model = "gemma3:1b"     # 1B parameters
# model = "llama3.2"    # 3B parameters
# model = "mistral"     # 7B parameters

# Create a language model with an endpoint, and a RetrievalQA chain which takes the language model,and the vector store containing our documents.
llm = OllamaLLM(
    model=model,
    base_url="http://127.0.0.1:11434",
    temperature=0.9, top_p=0.95, top_k=46,
    )
loader = DirectoryLoader(
    "./documents",
    glob="**/*.txt",
    loader_cls=TextLoader,
    loader_kwargs={"encoding": "utf-8"}
)
docs = loader.load()
print(f"One single document:\n\n'{docs[1].page_content}'\n\nFrom the text file:\n'{docs[1].metadata['source']}'")
splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=128)
chunks = splitter.split_documents(docs)
print(f"One single document chunk:\n'{chunks[5].page_content}'\n\nFrom the file:\n'{chunks[5].metadata['source']}'")

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vector_store.as_retriever(search_kwargs={"k": 10}), # We set the number of chunks to return k
    chain_type="stuff",            # or "map_reduce", "refine", etc.
    return_source_documents=True,  # if you want the source chunks back
)
# With RAG
query = "Who is the captain of the pirate ship?"
result = qa_chain.invoke({"query": query})
print(f"Answer: {result['result']}\n")
print(f"Source: {result['source_documents']}")
```
---

### Now deploy it to fly.io?
https://fly.io/docs/python/do-more/add-ollama/
