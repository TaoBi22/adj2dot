# adj2dot
This is an incredibly simple script to convert a CSV undirected graph adjacency matrix to a DOT representation. There is no input checking, or anything fancy like that! This includes checking whether the adjacency matrix is symmetric - the script assumes that it is, and only visits each pair of nodes once. The output DOT code is just printed to `stdout`.

The file should be in this format, with the node labels in the first line:

```
A,B,C
1,0,1
0,0,0
1,0,0
```
