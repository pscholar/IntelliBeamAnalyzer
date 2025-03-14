
import os
from task_packager import TaskPackager
from response_retriever import BackTicksResponseRetriever 
from instruction_runner import SimpleInstructionRunner
import constants

def perform_analysis(task, model = None):
    if model is None:
      return None
    TP = TaskPackager()
    BTR = BackTicksResponseRetriever()
    SIP = SimpleInstructionRunner()
    sys_prompt, task = TP.package_task(user_input=task,task_type="analysis")
    response = model.send_to_model(system_prompt=sys_prompt,task=task)  
    if response is None:
       return None 
    code = BTR.parse_response(response=response)
    if code is None:
       return None    
    results = SIP.save_and_run(code=code,output_file=constants.OUTPUTFILE)
    sys_prompt, task = TP.package_task(user_input=results,task_type="report")
    response = model.send_to_model(system_prompt=sys_prompt,task=task)
    if response is None:
       return None 
    report = BTR.parse_response(response=response)
    if code is None:
       return None
    os.makedirs(os.path.dirname(constants.REPORTFILE), exist_ok=True)
    try:
      with open(constants.REPORTFILE, 'w') as file:
        file.write(report)
        return os.path.abspath(constants.REPORTFILE)
    except Exception as e:
        return None

    
       
