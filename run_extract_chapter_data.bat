@echo off
:: Activate the environment
CALL C:\ProgramData\Anaconda3\Scripts\activate tf_env
:: Run your Python script
python "C:\Users\digitalscorpyun\Projects & Coding\scripts\extract_chapter_data.py"
:: Keep the terminal open after execution
pause
