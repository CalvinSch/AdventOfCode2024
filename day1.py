import math

left_list = []
right_list = []

def process_location_id_list(filename: str): 
    with open("day1_input.txt", "r") as input:
        for line in input:
            #Split Location IDs
            left_list_entry, right_list_entry = line.split('   ')

            #Cast to int and append to lists
            left_list.append(int(left_list_entry))
            right_list.append(int(right_list_entry))
    
    #Sort to help with comparison between smallest -> largest
    left_list.sort()
    right_list.sort()

def sum_list_distances(left_list: list[int], right_list: list[int]) -> int:
    total_distance = 0
    if(len(left_list) == len(right_list)):
        for i in range(len(left_list)):
            total_distance += abs(left_list[i] - right_list[i])
    return total_distance

if __name__ == "__main__":
    process_location_id_list("input.txt")
    print(sum_list_distances(left_list, right_list))