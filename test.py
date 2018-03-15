index = 0
pcb = int(raw_input("Enter the quantity of PCB integrated\n"))
panelQuantity = int(raw_input("Enter the number of panel present\n"))

panelSize = pcb*panelQuantity
print "Number of PCB in total\t\n",panelSize
number = []
for x in range (1, panelSize+1):
   number.append(x)
print "\nPCB Numbers Available\n", number

barcode = int(raw_input('\nEnter the Barcode INPUT\n'))
print "\nYou have entered ",barcode,"\n"
if barcode<=panelSize:
   temp = 0
   newpcb=pcb
   while barcode > pcb:
      pcb+=newpcb
      temp+=1

   temp2=temp*newpcb
   for x in range (temp2, temp2+newpcb):
      print "PCB available are\n", x+1 
else:
   print "!!...SORRY PCB BARCODE NOT REGISTERED...!!"
