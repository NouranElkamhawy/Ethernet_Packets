class ReadFile:

    def __init__(self, file_name):
        self.file_name = file_name

    def read_parameters(self):
        params = []
        with open(self.file_name, 'r') as f:
    # Read all lines into a list
          lines = f.read()  ###Read packets configurations from a text file, ex: “config.txt” attached
# Generate random bytes
# Parse parameters from lines
# Extract value after "STREAM_DURATION_MS"
        StreamDuration = int(lines[lines.find('STREAM_DURATION_MS'):].split()[2])  ###Packets will be generated for a specific streaming duration
        params.append(StreamDuration)
        # Extract value after "IFGs"
        IFGs = int(lines[lines.find('IFGs'):].split()[2]) ###min. number of bytes is 12 
        params.append(IFGs)
        # Extract value after "SOURCE_ADDRESS"
        Source_Address_Bin =bin(int(lines[lines.find('SOURCE_ADDRESS'):].split()[2],16))[2:]
        params.append(Source_Address_Bin)
        # Extract value after "DESTINATION_ADDRESS"
        Destination_Address_Bin=bin(int(lines[lines.find('DESTINATION_ADDRESS'):].split()[2],16))[2:]
        params.append(Destination_Address_Bin)
        # Extract value after "ETHER_TYPE"
        Ether_Type_Bin =bin(int(lines[lines.find('ETHER_TYPE'):].split()[2],16))[2:]# Convert hex_value to an integer in base 16, then convert the integer to binary and remove the "0b" prefix
        params.append(Ether_Type_Bin)
        # Extract value after "PAYLOAD_TYPE"
        Payload_Type =lines[lines.find('PAYLOAD_TYPE'):].split()[2]
        params.append(Payload_Type)
        # Extract value after "MAX_PACKET_SIZE"
        Max_Packet_Size = int(lines[lines.find('MAX_PACKET_SIZE'):].split()[2])
        params.append(Max_Packet_Size)
        # Extract value after "BURST_SIZE"
        Burst_Size = int(lines[lines.find('BURST_SIZE'):].split()[2])
        params.append(Burst_Size)
        # Extract value after "BURST_PERIODICITY_US"
        Burst_Periodicity_Us = int(lines[lines.find('BURST_PERIODICITY_US'):].split()[2])
        params.append(Burst_Periodicity_Us)
        return params
    def get_parameter(self, name):
        return self.parameters.get(name)
# Usage:
file_reader = ReadFile("C:\\nouran\\Siemens\\task 1\\config.txt")
parameters = ReadFile.read_parameters(file_reader)
#print(parameters)