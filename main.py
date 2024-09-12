from audio_manager import AudioManager
import os
from utils.file_utils import *
from llm.completor_vision import OpenAICompletorVision
from llm.completor_openai import OpenAICompletor

import ast
import subprocess

api_key = os.environ.get('OPENAI_API_KEY')
image_path =  "C:\\Users\\admin\\Desktop\\diff policy\\demo\\img_Color.png"


def main():
    completor = OpenAICompletorVision(api_key, model="gpt-4o")
    # completor = OpenAICompletor(api_key, model="gpt-4o")
    audio_manager = AudioManager()


    # ================== Task 0: take the photo / call GSAM ==================
    # 1. take the photo

    # 2. call GSAM / make sure the target dir is correct.
    # subprocess.Popen(['python', 'main.py', "--config"])


    question_prompt = read_txt_file('prompts/demo/question_prompt.txt')

    # while True:
    print("="*40)
    print("Please tell me your question.")
    # input("Press Enter to start recording...")
    # text = audio_manager.listen()

    text = "I want to drink?"
    # text = "What are on the table?"

    # ================== Task 1: analyze the image ==================
    if text:

        question = f"""{question_prompt} 
                    \n The question is: [{text}]
                    """
        # print(f"Question: {text}")

        print("Thinking...")
        # answer = completor.answer(text)
        answer = completor.answer_with_image(question, image_path)


        print(f"Answer: {answer}")
        # audio_manager.speak_async(answer)
        # audio_manager.speak(answer)

    else: # If the audio is not recognized
        print("Please try again.")
    
    # ================== Task 2: analyze what to do ==================
    manipulation_prompt = read_txt_file('prompts/demo/manipulation_prompt.txt')
    answer = completor.answer(manipulation_prompt)

    
    action = ast.literal_eval(answer)

    if action is not None:
        print("Working on the task...")
        print(f"Answer: {answer}")

        # do the segmentation and manipulation

        # 1. call the results of GSAM 

        # 2. get the one with specific label

        # 3. load pre-defined grasp pose

        # 4. convert to the real pose
        
    else:
        print("Task done.")

if __name__ == "__main__":
    main()