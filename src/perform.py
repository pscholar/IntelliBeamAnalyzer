
import os
from task_packager import TaskPackager
from model_interface import GPTModelInterface 
from model_interface import CLDModelInterface
from response_retriever import BackTicksResponseRetriever 
from instruction_runner import SimpleInstructionRunner
import constants

def perform_analysis(task, LLM = constants.DEFAULT_LLM):
    TP = TaskPackager()
    GPT = GPTModelInterface()
    CLD = CLDModelInterface()
    BTR = BackTicksResponseRetriever()
    SIP = SimpleInstructionRunner()
    sys_prompt, task = TP.package_task(user_input=task,task_type="analysis")
    if LLM == constants.GPT_LLM:
      response = GPT.send_to_model(system_prompt=sys_prompt,task=task)
    elif LLM == constants.CLAUDE_LLM:
       response = CLD.send_to_model(system_prompt=sys_prompt,task=task)   
    code = BTR.parse_response(response=response)    
    results = SIP.save_and_run(code=code,output_file=constants.OUTPUTFILE)
    sys_prompt, task = TP.package_task(user_input=results,task_type="report")
    if LLM == constants.GPT_LLM:
      response = GPT.send_to_model(system_prompt=sys_prompt,task=task)
    elif LLM == constants.CLAUDE_LLM:
      response = CLD.send_to_model(system_prompt=sys_prompt,task=task)
    report = BTR.parse_response(response=response)
    os.makedirs(os.path.dirname(constants.REPORTFILE), exist_ok=True)
    try:
      with open(constants.REPORTFILE, 'w') as file:
        file.write(report)
        return os.path.abspath(constants.REPORTFILE)
    except Exception as e:
        return None

    
       
