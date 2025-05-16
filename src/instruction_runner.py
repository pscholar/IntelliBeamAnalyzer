import os
import tempfile
import subprocess
from abstractclasses.abstract_instruction_runner import AbstractInstructionRunner

class SimpleInstructionRunner(AbstractInstructionRunner):
    def __init__(self):
        # Use the directory of the calling script
        self.temp_dir = os.path.dirname(os.path.abspath(__file__))

    def save_and_run(self, code: str, output_file: str = None) -> str:
        print(f"Temp dir: {self.temp_dir}")
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
                    import sys
                    import os
                    import subprocess
                    #print(f"Temp file name: {temp_file.name}")
                    script_dir = os.path.dirname(os.path.abspath(__file__))
                    env = os.environ.copy()
                    env["PYTHONPATH"] = script_dir + os.pathsep + env.get("PYTHONPATH", "")
                    #print(f"Python Executable: {sys.executable}")
                    result = subprocess.run(
                        [sys.executable, temp_file.name],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.PIPE,
                        text=True,
                        cwd=script_dir,
                        env=env  
                    )
                    print(result)
                    os.remove(temp_file.name)
                    if os.path.exists(output_file):
                        with open(output_file, "r") as f:
                            output_content = f.read()
                        return output_content.strip()
                    return f"Error in execution or output file not created: {result.stderr.strip()}"       
        except Exception as e:
            return f"An error occurred: {str(e)}"
        #Beam Length:7m
        #Left support: pin
        #right support: roller
        #Material: steel
        #Cross-section: 200 x 300mm
        #Load of 10kN at 3m from left support

        # A 6m steel beam is supported by a pin support at the left and roller support at the right. It carries a point load of 10 kN at 3m from the left support. Cross-section is 200 x 300m.
