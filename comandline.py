import concurrent.futures
import graph as G
import algoritms
import sys
import pygame




executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)


def main(graph):
    while True:
        c  = input(">")
        if(c == "kruskal"):
            executor.submit(algoritms.kruskal, graph)
        elif(c == "unlock"):
            graph._Graph__lock = False
        elif(c == "exit"):
            pygame.quit()
            sys.exit(0)
            break

if __name__ == "__main__":
    main(graph)
