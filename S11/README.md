# Pilot response agent based on `deepseek-r1-distill-qwen-7b`

This application trys to implement an agent that acts as a pilot communicating with Air Traffic Control (ATC).

The standard communication workflow in this context involves the controller speaking first, followed by the pilot repeating the message. This readback procedure ensures that the message was clearly understood and helps prevent any miscommunication.

Here are some examples: 

- RYR684V wind 240 8kt cleared to land runway 24L -> expeted output -> cleared to land runway 24R RYA684V
- VLG54WT taxi to HP01 runway 24L via M, P, L, k  -> Taxi to HP01 runway 24L via M, P, L, k, VLG54WT

In the first example, we can see that the pilot repeats almost exactly what the controller said. However, non-essential information such as the wind is intentionally omitted in the response. This is done to minimize the time spent on the frequency, allowing other pilots to communicate more efficiently.


## Interface 

![Descripción de la imagen](app.png)

## APP

Using llmstudio and its SDK (Software Development Kit), I connected my Python script with a DeepSeek model (deepseek-r1-distill-qwen-7b). The input is an ATC (Air Traffic Controller) instruction, and the output is the expected pilot readback.

To customize the model’s behavior, I defined a set of instructions (the context), which I concatenate with the input before sending it to the model:

```python 
full_prompt = context + "\n\n" + prompt
```

Since the output was not what I expected (it included the reasoning), I added a layer to clean the response and extract only the relevant pilot phrase: 


```python 
    response_text = result.content.strip()
    if "<think>" in response_text:
        clean_response = response_text.split("<think>")[-1].strip().split("\n")[-1]
    else:
        clean_response = response_text.split("\n")[-1]
```
