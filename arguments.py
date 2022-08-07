import argparse


def arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--wh", type=int, default=800, help="height of the Window (in pixels)")
    parser.add_argument("--ww", type=int, default=800, help="Width of the Window (in pixels)")
    parser.add_argument("--bs", type=int, default=10, help="size of each square on the grid (in pixels)")
    parser.add_argument("--fps", type=int, default=15, help="FPS. Increase it to speed up the simulation")
    parser.add_argument("--amin", type=int, default=2, help="Minimum num. of neighbours that an alive cell needs to "
                                                            "stay alive.")
    parser.add_argument("--amax", type=int, default=3, help="Maximum num. of neighbours that an alive cell needs to "
                                                            "stay alive.")
    parser.add_argument("--dmin", type=int, default=3, help="Minimum num. of neighbours that an alive cell needs to "
                                                            "born again.")
    parser.add_argument("--dmax", type=int, default=3, help="Maximum num. of neighbours that an dead cell needs to "
                                                            "born again")

    args = parser.parse_args()
    return args
