#!/usr/bin/env python
import sys
import warnings

from utilities import AiLatestDevelopment

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI LLMs'
    }
    feedback={"feedback":"Body Language Analysis Summary Hand on waist: 10.36036036036036 Hands clasped: 0.45045045045045046 Head looks down: 89.1891891891892 Emotion Detector Analysis Angry: 9.91% Disgust: 15.77 \%\ Fear: 24.32% Happy: 28.83% Neutral: 6.76% Sad: 13.06% Surprise: 1.35\%\ Eye Contact Analysis Not contact: 100.00% Hand Movement Analysis"}
    result=AiLatestDevelopment().crew().kickoff(feedback)
    print(result)
    return{"report":result}
result=run()