#!/Applications/anaconda/envs/Python3/bin

from vector import Vector
from line import Line


def main():
    test_intersections = True
    test_errors = False # Includes examples to deliberately throw errors


    # Test if lines are parallel, same, or have an intersection
    if test_intersections:
        print("=== Parallel, Same, or Intersecting Lines Quiz ===")

        l_1 = Line(Vector([4.046, 2.836]), 1.21)
        l_2 = Line(Vector([10.115, 7.09]), 3.025)
        print(l_1)
        print(l_2)
        print("Parallel: {}".format(l_1.is_parallel(l_2)))
        print("Same line: {}".format(l_1 == l_2))
        print("Intersection: {}\n".format(l_1.intersection(l_2)))

        l_3 = Line(Vector([7.204, 3.182]), 8.68)
        l_4 = Line(Vector([8.172, 4.114]), 9.883)
        print(l_3)
        print(l_4)
        print("Parallel: {}".format(l_3.is_parallel(l_4)))
        print("Same line: {}".format(l_3 == l_4))
        print("Intersection: {}\n".format(l_3.intersection(l_4)))

        l_5 = Line(Vector([1.182, 5.562]), 6.744)
        l_6 = Line(Vector([1.773, 8.343]), 9.525)
        print(l_5)
        print(l_6)
        print("Parallel: {}".format(l_5.is_parallel(l_6)))
        print("Same line: {}".format(l_5 == l_6))
        print("Intersection: {}\n".format(l_5.intersection(l_6)))

    # Test magnitude and normalization of vectors
    if False:
        print("\n=== Planes in 3D Quiz ===")

        vec6 = Vector([-0.221, 7.437])
        print(vec6)
        print("Magnitude: {}\n".format(vec6.magnitude()))

        vec7 = Vector([8.813, -1.331, -6.247])
        print(vec7)
        print("Magnitude: {}\n".format(vec7.magnitude()))

        vec8 = Vector([5.581, -2.136])
        print(vec8)
        print("Normalization: {}\n".format(vec8.normalization()))

        vec9 = Vector([1.996, 3.108, -4.554])
        print(vec9)
        print("Normalization: {}\n".format(vec9.normalization()))

        # Error test Zero Vector
        if test_errors:
            vec_zero = Vector([0, 0, 0])
            print(vec_zero)
            print("Normalization: {}\n".format(vec_zero.normalization()))



if __name__ == '__main__':
    main()