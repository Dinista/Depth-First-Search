# Depth-First-Search

## Introduction

This implementation involves a program that reads a <a href="https://en.wikipedia.org/wiki/Directed_graph" style="text-decoration: none;">directed graph</a> from user input, displaying its <a href="https://en.wikipedia.org/wiki/Strongly_connected_component" style="text-decoration: none;">strongly connected components</a>. If there are no cycles, it also provides its <a href="https://en.wikipedia.org/wiki/Topological_sorting" style="text-decoration: none;">topological sorting</a>.

## How it works
First the program will read the <b>vertices and edges</b> number (v e), then after entering those values it will star to read the pairs of vertices (representing the edges). The graph is represented through an <b>adjacency list</b> and <b>depth-first search</b> is applied to find <b>strongly connected components</b>, <b>topological sorting</b>, and possible <b>cycles</b>.

## How to use

### Input
First of all it's necessary to inform the number of vertices and the number of edges in one line (v e), as and exemple for a graph with 6 vertices and 6 edges:
```
6 6
```
then, press enter and start to input each edge path, from a vertice to another, an example of input will be:

```
6 6 
5 0
5 2
2 3
3 1
4 1
4 0
```

### Output

An example of output, considering the previous input, would be:

```
Tempos:
0 : 1 / 2
1 : 3 / 4
2 : 5 / 8
3 : 6 / 7
4 : 9 / 10
5 : 11 / 12

Numero de ciclos: 0

Ordenacao topologica:
[5, 4, 2, 3, 1, 0]

Componentes: ['|', 5, '|', 4, '|', 2, '|', 3, '|', 1, '|', 0, '|']

```
"Tempo" means the time of visit in the algorithm, followed by number of cicles,  topological order and strongly connected components.

### Dependencies

Pyhton 3.7 or higher.
