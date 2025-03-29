# goit-algo2-hw-03
The repository for the 3rd GoItNeo Design and Analysis of Algorithms homework


### Task 1: Application of the Maximum Flow Algorithm for Goods Logistics
This task involved developing a program to model a flow network for logistics, simulating the movement of goods from warehouses to stores using the maximum flow algorithm.

#### Requirements:
- Construct a graph model representing the flow network based on the given connections and capacities.

- Use the Edmonds-Karp algorithm to calculate the maximum flow in the constructed graph.

- Analyze the results and compare them with theoretical expectations.

#### Results:
After applying the maximum flow algorithm, the total maximum flow in the logistics network was calculated as 115 units. The results are shown in the table below, which indicates the actual flow between terminals and stores:
| Terminal | Store | Actual Flow (units) | 
| ------------- | ------------- | ------------- |
| Terminal 1 | Store 1 | 15.00 | 
| Terminal 1 | Store 2 | 10.00 |
| Terminal 1 | Store 3 | 0.00 |
| Terminal 1 | Store 4 | 10.00 |
| Terminal 1 | Store 5 | 6.67 |
| Terminal 1 | Store 6 | 3.33 |
| Terminal 1 | Store 7 | 10.00 |
| Terminal 1 | Store 8 | 5.00 |
| Terminal 1 | Store 9 | 0.00 |
| Terminal 1 | Store 10 | 0.00 |
| Terminal 1 | Store 11 | 0.00 |
| Terminal 1 | Store 12 | 0.00 |
| Terminal 1 | Store 13 | 0.00 |
| Terminal 1 | Store 14 | 0.00 |
| Terminal 2 | Store 1 | 0.00 |
| Terminal 2 | Store 2 | 0.00 |
| Terminal 2 | Store 3 | 0.00 |
| Terminal 2 | Store 4 | 5.00 |
| Terminal 2 | Store 5 | 3.33 |
| Terminal 2 | Store 6 | 1.67 |
| Terminal 2 | Store 7 | 10.00 |
| Terminal 2 | Store 8 | 5.00 |
| Terminal 2 | Store 9 | 0.00 |
| Terminal 2 | Store 10 | 20.00 |
| Terminal 2 | Store 11 | 10.00 |
| Terminal 2 | Store 12 | 0.00 |
| Terminal 2 | Store 13 | 0.00 |
| Terminal 2 | Store 14 | 0.00 |

#### Answers to Key Questions:
1. Which terminals provide the highest flow of goods to stores?

Terminal 1 provides the highest flow of goods to various stores, with a total of 69 units being distributed.

2. Which routes have the smallest capacity and how does this affect the overall flow?

Routes from Warehouse 1 to Store 3, and Warehouse 2 to Stores 1, 2, and 3 have the smallest capacities. These bottlenecks limit the overall flow to some stores.

3. Which stores received the least amount of goods, and can their supply be increased by enhancing the capacity of certain routes?

Stores 3, 9, 12, 13, and 14 received no goods. Increasing the capacity of routes feeding these stores could potentially improve their supply.

4. Are there any bottlenecks that can be eliminated to improve the efficiency of the logistics network?

Store 3, which receives no goods, and other stores with zero goods could be improved by increasing the flow capacity of the routes leading to them.

### Task 2: Comparison of OOBTree and Dictionary for Range Queries
This task required the development of a program to store product data using OOBTree and the dict data structure, and to compare their performance in executing range queries on the prices of products.

#### Requirements:
- Implement two data structures: an OOBTree using the BTrees library and a dict (standard dictionary) for storing product data.

- Implement functions for adding products and performing range queries to retrieve products in a specified price range.

- Measure the execution time for both data structures, executing 100 range queries for each to calculate the average time taken.

#### Results:
The results of the range query task for both data structures are as follows:

OOBTree: Total range query time was 0.002169 seconds.

Dict: Total range query time was 0.006619 seconds.

The OOBTree outperformed the dict in terms of speed due to its sorted data structure, which allows for faster access to range queries.