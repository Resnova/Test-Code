index = 0
pcb = int(raw_input("\nEnter the quantity of PCB integrated:\t"))
panelQuantity = int(raw_input("\nEnter the number of panel present:\t"))

panelSize = pcb*panelQuantity
print "\nNumber of PCB in total:\t\t\t",panelSize
number = []
for x in range (1, panelSize+1):
   number.append(x)
print "\nPCB Numbers Available:  ", number

barcode = int(raw_input('\nEnter the Barcode INPUT:\t\t'))
print"\n\tOUTPUT\n"
if 0<barcode<=panelSize:
   temp = 0
   newpcb=pcb
   while barcode > pcb:
      pcb+=newpcb
      temp+=1

   temp2=temp*newpcb
   for x in range (temp2, temp2+newpcb):
      print "PCB available are:  ", x+1
else:
   print "!!...SORRY PCB BARCODE NOT REGISTERED...!!"

