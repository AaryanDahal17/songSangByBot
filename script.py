import subprocess

print("Installing required packages...")

subprocess.run(['npm', 'install'],shell=True)

result = subprocess.run(['pip', 'install', '-r', 'requirements.txt'], capture_output=True, text=True)

if result.returncode == 0:
    print("Packages installed successfully.")
    print()
else:
    print("An error occurred while installing packages.")
    print(result.stderr)

subprocess.run(['python', 'urlSearchMaker.py'])

subprocess.run(['node', 'lyricsFetcher.js'])

subprocess.run(['python', 'lyricsWriter.py'])

subprocess.run(['python', 'textToSpeech.py'])
