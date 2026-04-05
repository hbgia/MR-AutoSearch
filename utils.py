def console_try_until_get_int(prompt: str) -> int:
    input_success = False
    while not input_success:
        try:
            user_input = int(input(prompt))
            return user_input
        except Exception as e:
            print(f"{e}\n")