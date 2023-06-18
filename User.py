from Check_the_path import PathPermissionChecker
from Burst import BurstGenerator
from ReadFile import ReadFile

ConfigFile=input(print("Please enter the path of your configration"))
OutputFile=input(print("Please enter the path of your output file"))
Checker=PathPermissionChecker(ConfigFile,OutputFile)
Checks=Checker.check_permissions()
#print(Checks)
while not Checks[0] or not Checks[1]:
        print("please re enter a valid path for both")
        ConfigFile=input(print("Please re-enter the path of your configration"))
        OutputFile=input(print("Please re-enter the path of your output file"))
        
Reader=ReadFile(ConfigFile)     
parameters = ReadFile.read_parameters(Reader)  
Burst_generator = BurstGenerator(parameters,OutputFile)
Burst_generator.BurstOfPackets()

#C:\nouran\Siemens\task1\config.txt
#C:\nouran\Siemens\task1\Output.txt