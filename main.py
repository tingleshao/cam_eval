# main script launchs the decoding process.
# initializing many decoding instances
# see the agg. decoding resources (from cmd output? does it print out how much memory is allocated for each decoder?)

from init_decode import init_decode

import argparse

def run(args):
    # call dispather, get model
    # use motion_generator, get motion
    # use motion, model, param, generates simulation result
    # display simulation result
    # save motion and simulation result
    # step 1: call dispather,
    for i in args.x:
        init_decode.run()
    print "Simulation done! Result saved to ... %s" % "foo/bar

def main():
    print "hello world, this is sim_cam main program"
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbosity", help="""increase output verbosity""",
                        action="store_true")
    parser.add_argument("-w", help="""the allowable bandwidth for the system
                        to transmit video data from server side to the client
                        side""", type=int)
    parser.add_argument("-a", help="""the weight for the pixel overhead term
                        of the loss function""", type=int)
    parser.add_argument("-b", help="""the weight for the average delay term of
                        the loss function""", type=int)
    parser.add_argument("-h", help="""size of the H264 header""", type=int)
    args = parser.parse_args()
    if args.verbosity:
        print "verbosity turned on"
    # run the simulatoin
    args.x = [1 2 3]
    run(args)

if __name__ == '__main__':
    main()
