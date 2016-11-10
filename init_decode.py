# the class is responsible for init nvidia decoder
import os
import subprocess
import time
import sys


class init_decode:

    def __init__(self):
        print "you initialized an init_decode!"

    def run(self):
        print "run!"

    def call_nv_decoder(self):
        cmd = '/home/cshao/Downloads/Video_Codec_SDK_7.0.1/Samples/NvDecodeGL/NvDecodeGL -i=/home/cshao/Downloads/Video_Codec_SDK_7.0.1/Samples/common/video/plush1_720p_10s.m2v'
        os.system(cmd)

    def call_nv_decoder_n(self, n):
        processes = set()
        cmd = ['/home/cshao/Downloads/Video_Codec_SDK_7.0.1/Samples/NvDecodeGL/NvDecodeGL -i=/home/cshao/Downloads/Video_Codec_SDK_7.0.1/Samples/common/video/plush1_720p_10s.m2v']
        for i in xrange(n):
            processes.add(subprocess.Popen(cmd, shell=True))

    def call_nv_decoder_n_send_null(self, n):
        processes = set()
        cmd = ['/home/cshao/Downloads/Video_Codec_SDK_7.0.1/Samples/NvDecodeGL/NvDecodeGL -i=/home/cshao/Downloads/Video_Codec_SDK_7.0.1/Samples/common/video/plush1_720p_10s.m2v -o=foo.yuv']
        for i in xrange(n):
            processes.add(subprocess.Popen(cmd, shell=True))

    def call_nv_decoder_n_4k(self, n):
        processes = set()
        cmd = ['/home/cshao/Downloads/Video_Codec_SDK_7.0.1/Samples/NvDecodeGL/NvDecodeGL -i=/home/cshao/Videos/jellyfish/jellyfish-120-mbps-4k-uhd-h264.mkv']
        #cmd = ['/home/cshao/Downloads/Video_Codec_SDK_7.0.1/Samples/NvDecodeGL/NvDecodeGL -i=/home/cshao/Videos/iphone6s_4k.mov']
        for i in xrange(n):
            processes.add(subprocess.Popen(cmd, shell=True))

def main():
    idec = init_decode()
    n = int(sys.argv[1])
#    idec.call_nv_decoder_n(n)
    #idec.call_nv_decoder_n_send_null(n)
    idec.call_nv_decoder_n_4k(n)

if __name__ == "__main__":
    main()
