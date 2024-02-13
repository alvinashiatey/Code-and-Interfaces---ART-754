import time
import random

stanza = [
    "My uncle was the prophetic one,",
    "throwing his beads this way and that,",
    "diving, foretelling,",
    "warnings galore, sweet promising.",
    "One eye on the past, four to the future,",
    "half a dozen or more for now.",
    "He was good if the news was good;",
    "for evil news we blamed the beads."
]


def perform():
    for line in stanza:
        time.sleep(2)
        # time.sleep(random.uniform(1, 3))
        print(line)
        time.sleep(3)
        # time.sleep(random.uniform(2, 4))
    print("Where the Bead Speaks by Ama Ata Aidoo")

def main():
    perform()

if __name__ == "__main__":
    main()
