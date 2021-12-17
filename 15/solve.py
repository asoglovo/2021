from chiton import find_safest_path, print_path, read_risk_map

if __name__ == '__main__':
    risk_map = read_risk_map()
    path, score = find_safest_path(risk_map)

    # print_path(risk_map, path)
    print(f'Risk score: {score}')
