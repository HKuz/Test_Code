#!/usr/local/bin/python
# Code Fights Sort Codefighters Problem


def sortCodefighters(codefighters):
    res = [CodeFighter(*codefighter) for codefighter in codefighters]
    res.sort(reverse=True)
    return list(map(str, res))


class CodeFighter():
    def __init__(self, username, eyeD, xp):
        self.username = username
        self.eyeD = int(eyeD)
        self.xp = int(xp)

    def __lt__(self, other):
        return (self.xp, other.eyeD) < (other.xp, self.eyeD)

    def __repr__(self):
        return self.username


def main():
    tests = [
        [
            [["warrior", "1", "1050"],
             ["Ninja!", "21", "995"],
             ["recruit", "3", "995"]],
            ["warrior", "recruit", "Ninja!"]
        ],
        [[], []],
        [[["single hero", "234", "283"]], ["single hero"]],
        [
            [["Corrie", "66", "5"],
             ["Arie", "99", "8"],
             ["Joann", "32", "5"],
             ["Larhonda", "9", "9"],
             ["Leda", "38", "7"],
             ["Anabel", "68", "3"],
             ["Javier", "10", "7"],
             ["Vicente", "49", "9"],
             ["Deanna", "29", "6"],
             ["Tracie", "28", "7"],
             ["Stephaine", "1", "8"],
             ["Yaeko", "2", "10"],
             ["Jared", "27", "8"],
             ["Fernando", "55", "10"],
             ["Sarita", "90", "9"],
             ["Erlene", "35", "2"],
             ["Kandace", "12", "9"],
             ["Jeane", "37", "7"],
             ["Malika", "80", "4"],
             ["Malinda", "92", "7"]],
            ["Yaeko",
             "Fernando",
             "Larhonda",
             "Kandace",
             "Vicente",
             "Sarita",
             "Stephaine",
             "Jared",
             "Arie",
             "Javier",
             "Tracie",
             "Jeane",
             "Leda",
             "Malinda",
             "Deanna",
             "Joann",
             "Corrie",
             "Malika",
             "Anabel",
             "Erlene"]
        ],
        [
            [["Na", "59", "3"],
             ["Huey", "5", "2"],
             ["Elizabeth", "46", "8"],
             ["Kelsi", "25", "7"],
             ["Myrtice", "53", "2"],
             ["Gene", "44", "3"],
             ["Season", "77", "4"],
             ["James", "20", "9"],
             ["Kandy", "86", "1"],
             ["Charise", "54", "10"],
             ["Lanita", "91", "1"],
             ["Jessie", "85", "4"],
             ["Shantelle", "60", "6"],
             ["Shad", "9", "5"],
             ["Doretha", "68", "1"],
             ["Jung", "57", "5"],
             ["Linwood", "19", "8"],
             ["Brynn", "2", "4"],
             ["Lupe", "33", "2"],
             ["Wilfred", "66", "10"]],
            ["Charise",
             "Wilfred",
             "James",
             "Linwood",
             "Elizabeth",
             "Kelsi",
             "Shantelle",
             "Shad",
             "Jung",
             "Brynn",
             "Season",
             "Jessie",
             "Gene",
             "Na",
             "Huey",
             "Lupe",
             "Myrtice",
             "Doretha",
             "Kandy",
             "Lanita"]
        ]
    ]

    for t in tests:
        res = sortCodefighters(t[0])
        ans = t[1]
        if ans == res:
            print("PASSED: sortCodefighters({}) returned {}"
                  .format(t[0], res))
        else:
            print("FAILED: sortCodefighters({}) returned {}, answer: {}"
                  .format(t[0], res, ans))


if __name__ == '__main__':
    main()
