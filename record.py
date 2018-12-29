import subprocess
import re

def record(station, port, freq, mode, time):
    """Record takes station, port, freq, mode, and time and returns the RSSI data
    of the recording being saved. The recording is saved to saved under the directory that the
    script is run on."""
    command = ["python", "Kiwi/kiwirecorder.py", "-k", str(30), "-s", str(station), "-p", str(port), "-f", str(freq), "-m", mode,
               "--tlimit="+str(time)]
    data = subprocess.Popen(command, stdout=subprocess.PIPE)
    output = data.communicate()[0]
    d =  re.sub("\r  ", ",", re.sub("Block: [0-9a-f]*, RSSI:", "", output)).split(",")[1:-1]
    return [float(i) for i in d]

data = record("hat2018.twrmon.net", 8075, 800, "am", 10);