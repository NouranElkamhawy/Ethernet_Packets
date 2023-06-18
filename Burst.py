import time
import secrets
from GeneratorOfEthernetPackets import EthernetPacketGenerator
from ReadFile import ReadFile
#file_reader = ReadFile("C:\\nouran\\Siemens\\task 1\\config.txt")
#parameters = ReadFile.read_parameters(file_reader)
class BurstGenerator:
    
    def __init__(self, parameters,outputFile):
         self.parameters = parameters
         self.packet_generator = EthernetPacketGenerator(parameters)
         self.ethernet_packet = self.packet_generator.generate_ethernet_packet()
         self.time=self.packet_generator.Time_parameters()
         self.outputfile=outputFile
    def IFGs(self,Num):
        random_IFGs=0
        
        if Num<=12:                
                random_IFGs = secrets.token_bytes(12)
        else:
                random_IFGs = secrets.token_bytes(Num) ##### generate random bytes of IFGs with number equals to the number read from config.file 
        return random_IFGs
                   
    def BurstOfPackets(self):
        GenerationTime=self.time[0]/10 #to get it in seconds as it was in milliseconds
        IFGS=self.time[1]
        once=0
        if once==0 and IFGS:
                 print("according to the standards the minimum number of IFGs is 12 so we will consider it")
                 once=1
                 
        Burst_size=self.time[2]
        Burst_delay=self.time[3]/1000000 #to get it in seconds as it was in microseconds
        notfinished=0
        burstcounter=1
        start_time =time.time()
        end_time = start_time + GenerationTime
        while time.time() < end_time:
                burst=bytes() 
                #starttimeofpacket=time.time()
                starttimeofburst=time.time() 
                packet = self.packet_generator.generate_ethernet_packet()
                endtimeofpacket=time.time()
                if endtimeofpacket > end_time:
                    notfinished=1 ######### if streaming time ended during generation of packet
                else: ######## adding packet to burst
                    if len(packet)%4 !=0:
                       packet =packet+self.IFGs(IFGS+(4-(len(packet)+IFGS))%4) ######### to be 4 byte aligned
                        
                               
                for _ in range(1,Burst_size+1):
                    
                    if notfinished !=1:    ######### if the packet was generated within the time of duration
                        burst=burst+packet
                    else:
                        burst=burst+self.IFGs(IFGS)  
                        
                        break    
                            # Open the file in write mode
                          
                if  burstcounter==1:     
                    file = open(self.outputfile, "w")
                    byte_string = ' '.join([str(hex(byte)) for byte in burst])
                    file.write(byte_string+"\n")
                       
                    burst=bytes()  
                    burstcounter=0 
                elif (time.time()-starttimeofburst) >=Burst_delay and notfinished!=1:
                    byte_string = ' '.join([str(hex(byte)) for byte in burst])
                    file.write(byte_string+"\n")
                    burst=bytes()
                elif time.time()-starttimeofburst <=Burst_delay and notfinished!=1:
                    
                         while((Burst_delay-(time.time()-starttimeofburst))>0): #####generate IFGs as long as the time between 2 bursts hasn't end yet
                            # Write data to the file
                              byte_string = ' '.join([str(hex(byte)) for byte in self.IFGs(12)])
                              file.write(byte_string+"\n")
                           
                         byte_string = ' '.join([str(hex(byte)) for byte in burst]) ######once the time is over send the burst
                         file.write(byte_string+"\n")   
                         burst=bytes()                   
                elif time.time()-starttimeofburst >= Burst_delay and notfinished==1 :
                        byte_string = ' '.join([str(hex(byte)) for byte in self.IFGs(12)])
                        file.write(byte_string+"\n")
                        file.close() 
                        break
                elif time.time()-starttimeofburst <= Burst_delay and notfinished==1 :    
                        file.close() 
                        break