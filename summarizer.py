import torch
from transformers import pipeline
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TextSummarizer:
    def __init__(self, model_name="facebook/bart-large-cnn"):
        logger.info(f"Initializing TextSummarizer with model: {model_name}")
        self.device = 0 if torch.cuda.is_available() else -1
        self.summarizer = pipeline("summarization", model=model_name, device=self.device)
        
    def summarize(self, text, max_length=130, min_length=30):
        if not text or len(text.strip()) == 0:
            raise ValueError("Input text cannot be empty.")
            
        logger.info(f"Summarizing text of length {len(text)}")
        try:
            summary = self.summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
            return summary[0]["summary_text"]
        except Exception as e:
            logger.error(f"Error during summarization: {e}")
            raise

if __name__ == "__main__":
    sample_text = """
    Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to the natural intelligence displayed by animals including humans. 
    Leading AI textbooks define the field as the study of "intelligent agents": any system that perceives its environment and takes actions that maximize its chance of achieving its goals.
    Some popular accounts use the term "artificial intelligence" to describe machines that mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem solving", however this definition is rejected by major AI researchers.
    """
    summarizer = TextSummarizer()
    result = summarizer.summarize(sample_text)
    print(f"Original Length: {len(sample_text)}")
    print(f"Summary: {result}")
