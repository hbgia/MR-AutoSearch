import device_input_control
import file_handler
import list_handler
import time

def main():
    searching_keywords = file_handler.keywords_load("inputs/search_keywords.txt")
    reps = file_handler.reps_load("inputs/search_reps.txt")
    
    chosen_keywords = list_handler.choose_keywords(reps, searching_keywords)
    print(f"Prepared {chosen_keywords.__len__()} keyword(s).")
    
    new_edge_window = device_input_control.open_ms_edge()
    time.sleep(5)  # Wait for Edge to start up
    
    print("====== SEARCHING SESSION STARTS ======")
    for i in range(len(chosen_keywords)):
        print(f"({i + 1}) Searching {chosen_keywords[i]}...")
        device_input_control.start_search_in_address_bar()
        time.sleep(0.5) # Wait for the browser to respond
        device_input_control.type_each_char(chosen_keywords[i])
        device_input_control.press_enter()
        time.sleep(10)

    new_edge_window.terminate
    file_handler.logs_searches(chosen_keywords, "logs.txt")
    device_input_control.close_tab()
    print("=========== DONE SEARCHING ===========")
    
    
if __name__ == "__main__":
    main()