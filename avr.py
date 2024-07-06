def generate_gpio_init():
    # Ask the user to input the mode for each bit
    bits = []
    for i in range(8):
        mode = input(f"Please enter Bit {i} mode (in/out): ")
        while mode not in ["in", "out"]:
            print("Invalid input. Please enter 'in' or 'out'.")
            mode = input(f"Please enter Bit {i} mode (in/out): ")
        bits.append(mode)

    # Generate the DDR register value
    ddr_value = 0
    for i, mode in enumerate(bits):
        if mode == "out":
            ddr_value |= (1 << i)
    
    # Convert the DDR register value to binary string
    ddr_value_bin = f"0b{ddr_value:08b}"
    
    # Generate the C code for the init function
    c_code = f"""\
void Init_PORTA_DIR(void)
{{
    DDRA = {ddr_value_bin};
}}"""
    
    return c_code

# Generate the GPIO init function and print it
c_code = generate_gpio_init()
print(c_code)