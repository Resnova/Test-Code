index = 0
pcb = int(raw_input("Enter the quantity of PCB integrated\n"))
panelQuantity = int(raw_input("Enter the number of panel present\n"))

panelSize = pcb*panelQuantity
print "Number of PCB in total\t\n",panelSize
number = []
for x in range (1, panelSize+1):
   number.append(x)
print "\nNon defective PCB Available\n", number

error = [3,7]   #int(raw_input("Enter the defective PCB Barcode"))

for i in error:
   number.insert(i-1,"x")
   number.pop(panelSize)

print "\nSorted Panel with Defective PCB Available\n", number


barcode = int(raw_input("Please enter Barcode to scan\n"))
print "\nYou have entered ",barcode,"\n"
if 0<barcode<=panelSize:



   for x in range ( , ):
      print "PCB available are\n", x+1 
else:
   print "!!...SORRY PCB BARCODE NOT REGISTERED...!!"
