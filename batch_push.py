import subprocess
import time
import os

def run_cmd(cmd):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

# Get all modified/untracked files
status = run_cmd('git status --porcelain')
lines = status.split('\n')
files = [line[3:] for line in lines if line]

batch_size = 30
print(f'Total files to process: {len(files)}')

for i in range(0, len(files), batch_size):
    batch = files[i:i+batch_size]
    print(f'\nProcessing batch {i//batch_size + 1}: {len(batch)} files')
    
    # Add files individually to avoid argument length limits
    for f in batch:
        run_cmd(f'git add "{f}"')
    
    # Commit
    run_cmd(f'git commit -m "Add PDFs batch {i//batch_size + 1}"')
    
    # Push
    push_res = subprocess.run('git push -u origin master', shell=True, capture_output=True, text=True)
    if push_res.returncode != 0:
        print(f'Push failed for batch {i//batch_size + 1}: {push_res.stderr}')
    else:
        print(f'Batch {i//batch_size + 1} pushed successfully.')
    
    time.sleep(2)
print("ALL DONE!")
