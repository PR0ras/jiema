from sys import argv
import zbar
#import datetime
import time
import sqlite3
#conn = sqlite3.connect('test.db')
#conn.execute('''CREATE TABLE D  (ID INT PRIMARY KEY     NOT NULL,NAME TEXT  NOT NULL, SHIJIAN  TEXT  NOT NULL);''')

def jiema(proc, image, closure):
    global a
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

            print 'decoded', symbol.type, 'utf8Data', '"%s"' % utf8Data
            #print 'decoded', symbol.type, 'utf8Data',utf8Data
            print a
            conn = sqlite3.connect('test.db')
            #b =datetime.datetime.now()
            b =time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
            print b
            #conn.execute("INSERT INTO B VALUES ('%d','%s')" %(a,utf8Data))
            #a = int(str(utf8Data))
            conn.execute("INSERT INTO D VALUES ('%d','%s','%s')" %(a,utf8Data,b))
            conn.commit()
            print "Records created successfully";
            conn.close()
            a =a+1
            print b

def output():
    global a
    a = 26
    print a

    # create a Processor
    proc = zbar.Processor()

    # configure the Processor
    proc.parse_config('enable')

    # initialize the Processor
    device = '/dev/video1'

    proc.init(device)
    # setup a callback

    proc.set_data_handler(jiema)
    #print 'time2',time
    # enable the preview window
    proc.visible = True

    # initiate scanning
    proc.active = True
    try:
        proc.user_wait()
    except zbar.WindowClosed:
        pass


if __name__ =='__main__':

    output()
