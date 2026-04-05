import device_input_control
import list_handler
import search_keywords
import utils
import time

def main():
    reps = utils.console_try_until_get_int("Enter searching reps: ") 
        
    chosen_keywords = list_handler.choose_keywords(reps, search_keywords.search_keywords)
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
        # file_handler.logs_search(chosen_keywords[i], "logs.txt")
        time.sleep(10)

    new_edge_window.terminate
    device_input_control.close_tab()
    print("=========== DONE SEARCHING ===========")
    
    
if __name__ == "__main__":
    main()