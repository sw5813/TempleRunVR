import bluetooth

target_name = "Alan's phone"
target_address = None

nearby_devices = bluetooth.discover_devices()

for bdaddr in nearby_devices:
	print bdaddr
    # if target_name == bluetooth.lookup_name( bdaddr ):
        # target_address = bdaddr
        # break

if target_address is not None:
    print "found target bluetooth device with address ", target_address
else:
    print "could not find target bluetooth device nearby"