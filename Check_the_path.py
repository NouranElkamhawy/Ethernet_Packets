import os
class PathPermissionChecker:
       def __init__(self, path1, path2):
         self.path1 = path1
         self.path2 = path2
         
# File path to check
       def check_permissions(self):
          # Check permissions for path1
         validations=[]
         path1_read_permission = os.access(self.path1, os.R_OK)
         # path1_write_permission = os.access(self.path1, os.W_OK)
         validations.append(path1_read_permission)
         # Check permissions for path2
         #path2_read_permission = os.access(self.path2, os.R_OK)
         path2_write_permission = os.access(self.path2, os.W_OK)
         validations.append(path2_write_permission)
         # Print the permissions for path1 and path2
         print("Permissions for", self.path1)
         print("Read permission:", path1_read_permission)
         #print("Write permission:", path1_write_permission)
 
         print("Permissions for", self.path2)
         #print("Read permission:", path2_read_permission)
         print("Write permission:", path2_write_permission)
         return validations
#path_checker = PathPermissionChecker('C:\\nouran\\Siemens\\task 1\\config.txt', '/path/to/file2.txt')
