"""Public QLoRA training entry point.
The historical checkpoint, private data and exact hyperparameters are unavailable; pass them explicitly.
"""
import argparse, json
from pathlib import Path

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--model_name_or_path",required=True)
    ap.add_argument("--train_file",required=True)
    ap.add_argument("--output_dir",required=True)
    ap.add_argument("--num_train_epochs",type=float,default=3)
    ap.add_argument("--learning_rate",type=float,default=2e-4)
    ap.add_argument("--per_device_train_batch_size",type=int,default=1)
    ap.add_argument("--gradient_accumulation_steps",type=int,default=16)
    ap.add_argument("--max_seq_length",type=int,default=2048)
    ap.add_argument("--use_4bit",action="store_true")
    args=ap.parse_args()
    try:
        import torch
        from datasets import load_dataset
        from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, TrainingArguments, Trainer, DataCollatorForLanguageModeling
        from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
    except ImportError as e:
        raise SystemExit("Install transformers datasets peft accelerate bitsandbytes torch before a real run: "+str(e))
    ds=load_dataset("json",data_files=args.train_file,split="train")
    tok=AutoTokenizer.from_pretrained(args.model_name_or_path,trust_remote_code=True)
    if tok.pad_token is None: tok.pad_token=tok.eos_token
    def render(ex):
        text=tok.apply_chat_template(ex["messages"],tokenize=False,add_generation_prompt=False)
        return {"text":text}
    ds=ds.map(render)
    def encode(ex): return tok(ex["text"],truncation=True,max_length=args.max_seq_length)
    ds=ds.map(encode,remove_columns=ds.column_names)
    quant=None
    if args.use_4bit:
        quant=BitsAndBytesConfig(load_in_4bit=True,bnb_4bit_quant_type="nf4",bnb_4bit_compute_dtype=torch.float16)
    model=AutoModelForCausalLM.from_pretrained(args.model_name_or_path,trust_remote_code=True,quantization_config=quant,device_map="auto")
    if args.use_4bit: model=prepare_model_for_kbit_training(model)
    lora=LoraConfig(r=16,lora_alpha=32,lora_dropout=0.05,bias="none",task_type="CAUSAL_LM",target_modules=["q_proj","k_proj","v_proj","o_proj"])
    model=get_peft_model(model,lora); model.print_trainable_parameters()
    out=Path(args.output_dir); out.mkdir(parents=True,exist_ok=True)
    training=TrainingArguments(output_dir=str(out),num_train_epochs=args.num_train_epochs,learning_rate=args.learning_rate,per_device_train_batch_size=args.per_device_train_batch_size,gradient_accumulation_steps=args.gradient_accumulation_steps,logging_steps=1,save_strategy="epoch",report_to="none",fp16=torch.cuda.is_available())
    Trainer(model=model,args=training,train_dataset=ds,data_collator=DataCollatorForLanguageModeling(tok,mlm=False)).train()
    model.save_pretrained(out); tok.save_pretrained(out)
    print(json.dumps({"output_dir":str(out),"records":len(ds),"provenance":"public_reconstruction"},ensure_ascii=False))

if __name__=="__main__": main()
