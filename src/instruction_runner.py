import os
import tempfile
import subprocess
from abstractclasses.abstract_instruction_runner import AbstractInstructionRunner

class InstructionRunner(AbstractInstructionRunner):
    def __init__(self):
        self.temp_dir = tempfile.gettempdir()

    def save_and_run(self, code: str, output_file: str = None) -> str:
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".py", 
                                             dir=self.temp_dir) as temp_file:
                temp_file.write(code.encode())
                temp_file.close()
                if output_file is None:
                    result = subprocess.run(
                        ['python', temp_file.name],
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
                    )
                    os.remove(temp_file.name)
                    if result.returncode == 0:
                        return result.stdout.strip() or "Execution completed with no output."
                    else:
                        return f"Error in execution: {result.stderr.strip()}"               
                else:
                    result = subprocess.run(
                        ['python', temp_file.name],
                        stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True
                    )
                    os.remove(temp_file.name)
                    if os.path.exists(output_file):
                        with open(output_file, "r") as f:
                            output_content = f.read()
                        return output_content.strip()
                    return f"Error in execution or output file not created: {result.stderr.strip()}"       
        except Exception as e:
            return f"An error occurred: {str(e)}"
