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

temp = pcb
newpcb = pcb
while (barcode>=newpcb):
   
   


temp-pcb
for x in range (temp, temp+pcb):
   print "PCB available are\n" x 
