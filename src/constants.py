import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
RESULTS_DIR = os.path.join(BASE_DIR, "results")
OUTPUTFILE = os.path.join(RESULTS_DIR, "beam_analysis_results.json")
REPORTFILE = os.path.join(RESULTS_DIR, "report.html")
WELCOMEFILE = os.path.join(BASE_DIR, "welcome.html")
WORKINGFILE = os.path.join(BASE_DIR, "working.html")
ERRORFILE = os.path.join(BASE_DIR, "error.html")
ICON = os.path.join(BASE_DIR,"icon.svg")
os.makedirs(RESULTS_DIR, exist_ok=True)
PROGRAM_NAME = "IntelliBeamAnaylzer"
GPT_LLM = "GPT"
CLAUDE_LLM = "CLAUDE"
MAX_CLAUDE_TOKENS = 200000
MAX_GPT_TOKENS = 128000
GPT_TEMPERATURE = 1.0
CLAUDE_TEMPERATURE = 1.0
DEFAULT_LLM = GPT_LLM
MIN_WIDTH = 800
MIN_HEIGHT = 600