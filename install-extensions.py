import subprocess

with open('./extensions', 'r') as f:
    content = f.readlines()
    content = [x.strip() for x in content]
    for line in content:
        subprocess.call(['/usr/local/bin/code', '--install-extension', line])

