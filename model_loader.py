from transformers import AutoTokenizer, pipeline, AutoModelForSeq2SeqLM

def loadModel():
    tokenizer=AutoTokenizer.from_pretrained("MBZUAI/LaMini-Flan-T5-783M")
    model=AutoModelForSeq2SeqLM.from_pretrained("MBZUAI/LaMini-Flan-T5-783M")
    generator=pipeline("text2text-generation", model=model, tokenizer=tokenizer)
    return generator