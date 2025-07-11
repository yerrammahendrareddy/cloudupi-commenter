import subprocess

def get_changed_tf_files(base, head):
    result = subprocess.run(["git", "diff", "--name-only", base, head], capture_output=True, text=True)
    changed_files = result.stdout.splitlines()
    return [f for f in changed_files if f.endswith(".tf")]
