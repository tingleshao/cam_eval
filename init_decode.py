# the class is responsible for init nvidia decoder
import os
import subprocess
import time


class init_decode:

    def __init__(self):
        print "you initialized a init_decode!"

    def run(self):
        print "run!"

    def call_nv_decoder(self):
        cmd = '/home/cshao/Downloads/Video_Codec_SDK_7.0.1/Samples/NvDecodeGL/NvDecodeGL -i=/home/cshao/Downloads/Video_Codec_SDK_7.0.1/Samples/common/video/plush1_720p_10s.m2v'
        os.system(cmd)

    def call_nv_decoder_n(self):
        processes = set()
        cmd = ['/home/cshao/Downloads/Video_Codec_SDK_7.0.1/Samples/NvDecodeGL/NvDecodeGL -i=/home/cshao/Downloads/Video_Codec_SDK_7.0.1/Samples/common/video/plush1_720p_10s.m2v']
        processes.add(subprocess.Popen(cmd, shell=True))
        processes.add(subprocess.Popen(cmd, shell=True))
        processes.add(subprocess.Popen(cmd, shell=True))
        processes.add(subprocess.Popen(cmd, shell=True))


def main():
    idec = init_decode()
    idec.call_nv_decoder_n()


if __name__ == "__main__":
    main()
