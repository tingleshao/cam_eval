# the class is responsible for init nvidia decoder
import os
import subprocess
import time
import sys

import numpy as np
import matplotlib.pyplot as plt

# full testing giving results on how the decoder performs under different settings

class full_test:

    def __init__(self):
        print "you initialized a full_test!"
        self.result = []

    def has_result(self):
        return self.result == []

    def plot_result(self):
        print "implement me!"

    def call_nv_decoder_n(self, n, res, bitrate):
        processes = set()
        cmd = ['/home/cshao/Downloads/Video_Codec_SDK_7.0.1/Samples/NvDecodeGL/NvDecodeGL -i=/home/cshao/Videos/jellyfish/jellyfish-'+res+'-'+bitrate+'bps.mp4']
        for i in xrange(n):
            processes.add(subprocess.Popen(cmd, shell=True))

    def call_nv_decoder_n_hd(self, n):
        processes = set()
        cmd = ['/home/cshao/Downloads/Video_Codec_SDK_7.0.1/Samples/NvDecodeGL/NvDecodeGL -i=/home/cshao/Downloads/Video_Codec_SDK_7.0.1/Samples/common/video/plush1_720p_10s.m2v']
        for i in xrange(n):
            processes.add(subprocess.Popen(cmd, shell=True))

    def call_nv_decoder_n_4k(self, n):
        processes = set()
        cmd = ['/home/cshao/Downloads/Video_Codec_SDK_7.0.1/Samples/NvDecodeGL/NvDecodeGL -i=/home/cshao/Videos/jellyfish/jellyfish-120-mbps-4k-uhd-h264.mkv']
        #cmd = ['/home/cshao/Downloads/Video_Codec_SDK_7.0.1/Samples/NvDecodeGL/NvDecodeGL -i=/home/cshao/Videos/iphone6s_4k.mov']
        for i in xrange(n):
            processes.add(subprocess.Popen(cmd, shell=True))

    def make_bar_chart(self):
        fourk_1 = (86, 86, 84)
        fourk_2 = (22, 21.75, 21.75)
        fourk_3 = (10.75, 10.375, 10.75)
        hd_1 = (325, 323, 302)
        hd_2 = (84.75, 85.75, 79.25)
        hd_3 = (42.875, 46.86, 39.625)
        seven20p_1 = (643, 652, 630)
        seven20p_2 = (184.75, 181.25, 182.5)
        seven20p_3 = (117, 100.75, 117)

        ind = np.arange(3)
        width = 0.3
        fig, ax = plt.subplots(1,3)
        rects1 = ax[0].bar(ind, fourk_1, width, color='r')
        rects2 = ax[0].bar(ind + width, fourk_2, width, color='y')
        rects2 = ax[0].bar(ind + width*2, fourk_3, width, color='b')
        ax[0].set_ylabel('decoding speed (fps)')
        ax[0].set_title('4k')
        ax[0].set_xticks(ind + width)
        ax[0].set_xticklabels(('30m', '50m', '120m'))
        ax[0].set_ylim([0,700])

        rects1 = ax[1].bar(ind, hd_1, width, color='r')
        rects2 = ax[1].bar(ind + width, hd_2, width, color='y')
        rects2 = ax[1].bar(ind + width*2, hd_3, width, color='b')
    #    ax[1].set_ylabel('Scores')
        ax[1].set_title('hd')
        ax[1].set_xticks(ind + width)
        ax[1].set_xticklabels(('15m', '20m', '50m'))
        ax[1].set_ylim([0,700])

        rects1 = ax[2].bar(ind, seven20p_1, width, color='r')
        rects2 = ax[2].bar(ind + width, seven20p_2, width, color='y')
        rects2 = ax[2].bar(ind + width*2, seven20p_3, width, color='b')
    #    ax[2].set_ylabel('Scores')
        ax[2].set_title('720p')
        ax[2].set_xticks(ind + width)
        ax[2].set_xticklabels(('3m', '5m', '10m'))
        plt.show()


def main():
    idec = full_test()
    #n = int(sys.argv[1])
    #res = sys.argv[2]
    #bitrate = sys.argv[3]
#    idec.call_nv_decoder_n(n)
    #idec.call_nv_decoder_n_send_null(n)
#    idec.call_nv_decoder_n(n, res, bitrate)
    idec.make_bar_chart()

if __name__ == "__main__":
    main()
