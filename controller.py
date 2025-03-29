from handler import build_graph, visualize_graph, calculate_max_flow, build_flow_table, load_data, add_item_to_tree, add_item_to_dict, range_query_tree, range_query_dict

def run_logistics_task():
    # Logistics Network Task
    print("Running Logistics Network Task...")
    G = build_graph()
    flow_dict, flow_value = calculate_max_flow(G)
    build_flow_table(flow_dict)
    visualize_graph(G)

def run_price_query_task():
    # Price Range Query Task
    print("Running Price Range Query Task...")
    file_path = 'generated_items_data.csv'
    data = load_data(file_path)

    if data:
        tree = {}
        dict_data = {}

        # Insert items into both structures
        for item in data:
            add_item_to_tree(tree, item)
            add_item_to_dict(dict_data, item)

        min_price, max_price = 50, 100
        num_queries = 100

        # Measure time for range queries
        
        tree_time = range_query_tree(tree, min_price, max_price)
        dict_time = range_query_dict(dict_data, min_price, max_price)

        print(f"Total range_query time for OOBTree: {tree_time:.6f} seconds")
        print(f"Total range_query time for Dict: {dict_time:.6f} seconds")

if __name__ == "__main__":
    run_logistics_task()
    run_price_query_task()
