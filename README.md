# aiml_api
This project leverages LLMs, specifically Llama 3.1 and the lightweight phi-3-instruct model, to detect malicious OS events, ensuring seamless integration with existing systems for enhanced cybersecurity.

https://aimlapi-nmsdr87bsd5ovtofnlmjxd.streamlit.app/

## Get Started
Clone the github repository in your virtual environment and activate it.

In your terminal run:

```
pip install streamlit
```
```
streamlit run qerberos
```
This will launch the streamlit app.

To ensure all model requirements are met you will also need to install the following in your environment. You can do it in this project's virtual environemnt thorugh the terminal:
```
!pip install --no-deps "xformers==0.0.27" trl peft accelerate bitsandbytes
!pip install "unsloth[cu121-torch230] @ git+https://github.com/unslothai/unsloth.git"
!pip install datasets
!pip install wandb
```

The dataset folder holds the training set files in csv format.

# How to 

The Windows log detecgtor which is a classifier is Finetuned_Phi_3_medium_4k_instruct_Unsloth.ipynb.  The ipython notebook needs to be run on colab.




