import device_input_control
import file_handler
import list_handler
import time

def main():
    searching_keywords = file_handler.keywords_load("inputs/search_keywords.txt")
    reps = file_handler.reps_load("inputs/search_reps.txt")
    
    chosen_keywords = list_handler.choose_keywords(reps, searching_keywords)
    
    new_edge_window = device_input_control.open_ms_edge()
    time.sleep(5)  # Wait for Edge to start up
    
    for words in chosen_keywords:
        device_input_control.start_search_in_address_bar()
        device_input_control.type_each_char(words)
        device_input_control.press_enter()
        time.sleep(10)

    new_edge_window.terminate
    device_input_control.close_tab()
    
if __name__ == "__main__":
    main()