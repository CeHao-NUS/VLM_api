import os
from utils.file_utils import *
from llm.completor_openai import OpenAICompletor

api_key = os.environ.get('OPENAI_API_KEY')

def main():
    
    initial_system = "You are a Python tutor. You are helping a student with their Python homework."
    task_prompt = "Write a python function that takes a list of integers and returns the sum of all the integers in the list."
    completor = OpenAICompletor(api_key)

    completor.add_system(initial_system)
    ans = completor.answer(task_prompt)

    print('ans\n', ans)
    
    # ans = completor.get_all_answers()
    # write_txt_file(file_name, ans)

if __name__ == "__main__":
    main()