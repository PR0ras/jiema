from sys import argv
import zbar

# create a Processor
proc = zbar.Processor()

# configure the Processor
proc.parse_config('enable')

# initialize the Processor
device = '/dev/video1'
if len(argv) > 1:
    device = argv[1]

proc.init(device)


# enable the preview window
proc.visible = True

# initiate scanning
proc.active = True

try:
    proc.user_wait()
except zbar.WindowClosed:
    pass
