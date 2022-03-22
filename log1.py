import os

location = '/Users/Damilola Odili/Downloads/VMware Research Collaboration Project/gclog/async-replicator/'
for filename in os.listdir(location):
    if filename == 'gc.log.1':
       f  = open(os.path.join(location, 'gc.log.1'), "r")
       print (f.read())

hekjdfnkjbdfkjvdbkvjbdkvjdbvkjbdfvjbdfkvjbdfjvbdfj
