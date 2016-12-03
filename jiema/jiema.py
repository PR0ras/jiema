from sys import argv
import zbar
import time

# create a Processor
proc = zbar.Processor()

# configure the Processor
proc.parse_config('enable')

# initialize the Processor
device = '/dev/video1'
#if len(argv) > 1:
#    device = argv[1]

proc.init(device)
print device
# setup a callback
time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
def jiema(proc, image, closure):
    # extract results
    for symbol in image:
        if not symbol.count:
            # do something useful with results
            try:
                utf8Data = symbol.data.decode("gb18030")
            except UnicodeDecodeError:
                    try:
                        utf8Data = symbol.data.decode("utf-8").encode("gbk")

                    except:
                        utf8Data=symbol.data.decode('utf-8').encode('sjis').decode('gb18030')
            print 'decoded', symbol.type, 'symbol', '"%s"' % utf8Data,'time',time
proc.set_data_handler(jiema)

# enable the preview window
proc.visible = True

# initiate scanning
proc.active = True

try:
    proc.user_wait()
except zbar.WindowClosed:
    pass
