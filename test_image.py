import os
from utils.file_utils import *
from llm.completor_vision import OpenAICompletorVision

import time

api_key = os.environ.get('OPENAI_API_KEY')

def main():
    
    completor = OpenAICompletorVision(api_key, model="gpt-4o")

    initial_system = read_txt_file('prompts/raw_instruction.txt')
    work1_prompt = read_txt_file('prompts/work1.txt')

    completor.add_system(initial_system)
    
    image_path =  ['real_front view.jpg', 'real_top view.jpg']

    work1 = f"\
        The [Task Description] is : Pick the mug from the table. \n\
        {work1_prompt} \n\
        "
    work2_prompt = read_txt_file('prompts/work2.txt')
    work3_prompt = read_txt_file('prompts/work3.txt')

    t0 = time.time()
    ans = completor.answer_with_image(work1, image_path)
    t1= time.time()
    print('Time taken in work 1:', round(t1-t0, 2))

    ans = completor.answer(work2_prompt)
    t2 = time.time()
    print('Time taken in work 2:', round(t2-t1, 2))

    ans = completor.answer(work3_prompt)
    t3 = time.time()
    print('Time taken in work 3:', round(t3-t2, 2))

    ans = completor.get_all_answers()

    write_txt_file('test_answer.txt', ans)
    print('write to test_answer.txt')

if __name__ == "__main__":
    main()