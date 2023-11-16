# List of storage values with their units
storage_values = [
    "4 TB", "250 GB", "25 GB", "25 GB", "8 TB", "8 TB", "8 TB",
    "8 TB", "8 TB", "8 TB", "1 TB", "2 TB", "550 GB", "260 GB",
    "50 GB", "50 GB"
]

def convert_to_gb(value, unit):
    """
    Convert the storage value to GB.
    
    Args:
    - value (float): Storage value
    - unit (str): Storage unit (e.g., GB, TB)
    
    Returns:
    - float: Storage value in GB
    """
    if unit == "TB":
        return value * 1024
    elif unit == "GB":
        return value
    else:
        raise ValueError("Unsupported unit")

def total_storage(storage_list):
    """
    Calculate the total storage in GB.
    
    Args:
    - storage_list (list of str): List of storage values with units
    
    Returns:
    - float: Total storage in GB
    """
    total = 0
    for storage in storage_list:
        value, unit = storage.split()
        value = float(value)
        total += convert_to_gb(value, unit)
    return total

if __name__ == "__main__":
    total_gb = total_storage(storage_values)
    total_tb = total_gb / 1024
    print(f"Total Storage: {total_gb:.2f} GB ({total_tb:.2f} TB)")

