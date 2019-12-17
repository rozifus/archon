# clean duplicates

import os
import subprocess

formats = [
    'webm',
    'mp4',
    'mkv'
]

print()

for root, dirs, files in os.walk('.'):
    for f in files:
        try:
            full_path = os.path.join(root, f)
            ext = os.path.splitext(full_path)[1]
            ext = ext.strip('.')
            if not ext in formats:
                continue
            result = subprocess.run([
                'ffmpeg',
                '-v', 'error',
                '-i', full_path,
                '-f', 'null',
                '-'],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True
            )

            if result.stdout or result.stderr:
                print(full_path)
                print(result.stderr)

        except Exception as e:
            print(e)

