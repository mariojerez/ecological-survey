import os

#region command logic

def species_in(species: str, sites_species_dict: dict[str, set]):
    pass

def unique(site_species: set, *other_site_species: set) -> set:
    pass

def common(*species_sets: set) -> set:
    pass

def combined(*species_sets: set) -> set:
    pass

#endregion


#region process user and file data

def get_arguments(user_input: str) -> list[str]:
    """Turns a string of arguments separted by commas into a list of arguments"""
    pass

def process_site_files(file_paths: list[str]) -> dict[str, set]:
    """Turn the provided files into a dictionary where keys are the names of sites and values are sets of species spotted in the sites."""
    pass

def get_expedition_files() -> list[str]:
    """Gets a list containing ecological expediction .txt files in this directory"""
    current_directory = os.getcwd()
    all_entries = os.listdir(current_directory)
    return [entry for entry in all_entries if os.path.isfile(os.path.join(current_directory, entry)) and entry[-4:] == ".txt"]

#endregion

def run_ecological_survey():
    pass

if __name__ == "__main__":
    run_ecological_survey()