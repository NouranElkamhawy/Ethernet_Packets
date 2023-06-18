from ReadFile import ReadFile
import binascii
import secrets
import crcmod.predefined
import time
class EthernetPacketGenerator:
    def __init__(self, parameters):
         self.parameters = parameters
    def Time_parameters(self):
         BurstGen=[]
         STREAM_Duration_MS = self.parameters[0]
         BurstGen.append(STREAM_Duration_MS)
         IFGs = self.parameters[1]
         BurstGen.append(IFGs)
         BURST_Size = self.parameters[7]
         BurstGen.append(BURST_Size)
         BURST_Periodicity_US = self.parameters[8]
         BurstGen.append(BURST_Periodicity_US)
         
         
         return BurstGen
    def generate_ethernet_packet(self):
        # Operate functions and generate Ethernet packet based on parameters
        # ...

        # Example: Generating a sample Ethernet packet
        
        IFGs = self.parameters[1]
        Source_Address_Bin = self.parameters[2]
        Destination_Address_Bin = self.parameters[3]
        Ether_Type_Bin = self.parameters[4]
        Payload_Type = self.parameters[5]
        Max_Packet_Size = self.parameters[6]
        Source_Address_Bin = Source_Address_Bin.zfill(48)# Convert hexadecimal to binary with padded zeros
        Destination_Address_Bin = Destination_Address_Bin.zfill(48)
        Ether_Type_Bin = Ether_Type_Bin.zfill(16) #if it is 0x0800 it indicates that the payload of the Ethernet frame is an IPv4 packet. Similarly, a value of 0x86DD indicates an IPv6 packet.
        once=0
        if once==0 and Max_Packet_Size>1526:
            print("this packet is not an ethernet packet")
            once=1
                  
        #print(IFGs)
        #print(Source_Address_Bin)
        #print(Destination_Address_Bin)
        #print(Max_Packet_Size)
        #print(Ether_Type_Bin)
        if  Max_Packet_Size >= 26 and Max_Packet_Size <= 1526:
          if Payload_Type=="RANDOM" and Max_Packet_Size>=72:
             Payload_Size=Max_Packet_Size-26
             random_bytes_payload = secrets.token_bytes(Payload_Size) ##### as long as Payload type is random
             integer_value_Payload = int.from_bytes(random_bytes_payload, byteorder='big')
             # Convert integer to binary string
             binary_string_Payload = bin(integer_value_Payload)[2:].zfill(Payload_Size * 8)
          elif Max_Packet_Size<=72:
             Payload_Size=46 #min number of bytes should be used for payload data 
             random_bytes_payload = secrets.token_bytes(Payload_Size) ##### as long as Payload type is random
             integer_value_Payload = int.from_bytes(random_bytes_payload, byteorder='big')
             # Convert integer to binary string
             binary_string_Payload = bin(integer_value_Payload)[2:].zfill(Payload_Size * 8)    
          Preamble='10101010101010101010101010101010101010101010101010101010'  #or 0XAA * 7(for 7 bytes)
          Sof='10101011'  #or 0xAB 
          
          ethernet_packet_Bin=Preamble+Sof+Destination_Address_Bin+Source_Address_Bin+Ether_Type_Bin+binary_string_Payload
          # Calculate the CRC
          crc_func = crcmod.predefined.mkCrcFun('crc-32')
          Ethernet_Packet_byte = int(ethernet_packet_Bin, 2).to_bytes(len(ethernet_packet_Bin) // 8, 'big')
          # Calculate the CRC
          crc = crc_func(Ethernet_Packet_byte)
          Crc_Bin=bin(int(hex(crc), 16))[2:]
          Crc_Bin=Crc_Bin.zfill(32)
          #print(Crc_Bin)
          Packet=ethernet_packet_Bin+Crc_Bin
          #print(Packet)
          Packet_bytes=int(Packet, 2).to_bytes(len(Packet) // 8, 'big')
          #print(Packet_bytes)
          return Packet_bytes
        elif Max_Packet_Size >1526:
            ethernet_packet=bytes()
            return ethernet_packet

      # Return a list of generated packets

