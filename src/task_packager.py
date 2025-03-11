from abstractclasses.abstract_task_packager import AbstractTaskPackager

class TaskPackager(AbstractTaskPackager):
    def __init__(self):
        self.system_prompts = {
            "task_generation": "You are a structural analysis engineer. Your job is to generate executable code that will analyze the structural properties of a beam based on the user input.",
            "result_interpretation": "You are a structural analysis engineer. Given the results from the structural analysis code, your job is to generate a detailed report explaining the findings."
        }

    def package_task(self, user_input: str, task_type: str = "task_generation") -> str:
        if task_type not in self.system_prompts:
            raise ValueError("Invalid task type. Should be 'task_generation' or 'result_interpretation'.")
        
        system_prompt = self.system_prompts[task_type]
        clean_user_input = " ".join(user_input.split())
        return f"{system_prompt} {clean_user_input}"
