Maze KruskalS(int width, int height)
{
  Maze maze(width, height);

  // Create a set with all connecting edges
  // Create a vector of buckets for each cell with their id.
  Set edges(maze);                  // #edges = (height - 1) * width + (width - 1) * height
  BucketsVector bucketCells(maze);  // #buckets = #cells = height * width

  // While the set of edges is not empty
  while (!edges.empty())
  {
    // Randomly get an edge and remove it from the set
    auto edge = GetRandom(edges);

    // If cells are not already in the same bucket: Connect them and Merge Buckets
    if (BucketId(edge.first) != BucketId(edge.second))
    {
      Connect(edge.first, edge.second);
      MergeBuckets(bucketCells, edge);
    }
  }

  return maze;
} 