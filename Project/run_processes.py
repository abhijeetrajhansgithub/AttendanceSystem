import subprocess

# Command to run the second script
script2_command = fr"""python "B:\Computer Science and Engineering\PycharmIDE\ManipalAttendanceProjectV1\Project\Server\database.py" """

# Command to run the first script
script1_command = fr"""python "B:\Computer Science and Engineering\PycharmIDE\ManipalAttendanceProjectV1\Project\Server\app.py" """


# Run the scripts simultaneously using subprocess
process1 = subprocess.Popen(script1_command, shell=True)
process2 = subprocess.Popen(script2_command, shell=True)

# Wait for both processes to complete
process1.wait()
process2.wait()

print("Both scripts have completed.")
