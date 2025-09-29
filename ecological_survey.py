import os

_instructions = """
What would you like to do? Enter one of the following commands:

 - sites
   Show available sites

 - common <site1>, <site2>, ..., <siteN>  
   Show species found in all of the listed sites.  
   If no sites are given, shows species common to all sites.

 - combined <site1>, <site2>, ..., <siteN>  
   Show species found in any of the listed sites.  
   If no sites are given, shows all species.

 - unique <site>  
   Show species found only in the specified site (not in others).

 - species_in <species>
   Show sites that species is found in.

 - q or quit  
   Exit the program.

 - h or help  
   Show these instructions again.

"""

def run_ecological_survey():
    file_paths = get_survey_files()
    site_species_dict = process_site_files(file_paths)
    print(f"Species from {len(site_species_dict)} sites have been collected.")
    print(_instructions)
    end_program = False
    while not end_program:
        user_input = input("Enter command: ")
        if user_input == 'sites':
            for site in site_species_dict.keys():
                print(site)

        elif user_input[:6] == "common":
            sites = get_arguments(user_input[6:])
            if len(sites) == 0:
                sites = list(site_species_dict.keys())
            try:
                species_sets = [site_species_dict[site] for site in sites]
            except KeyError:
                print(f"One of the provided arguments was invalid: {sites}")
                continue
            except:
                print("Something went wrong.")
                continue
            for species in common(*species_sets):
                print(species)

        elif user_input[:8] == "combined":
            sites = get_arguments(user_input[8:])
            if len(sites) == 0:
                sites = list(site_species_dict.keys())
            try:
                species_sets = [site_species_dict[site] for site in sites]
            except KeyError:
                print(f"One of the provided arguments was invalid: {sites}")
                continue
            except:
                print("Something went wrong.")
                continue
            for species in combined(*species_sets):
                print(species)

        elif user_input[:6] == "unique":
            site = get_arguments(user_input[6:])
            if len(site) != 1:
                print(f"The `unique` command expected one argument. Received: {len(site)}. Enter `help` for more information.")
                continue
            site = site[0]
            other_species_sets = [site_species_dict[s] for s in list(site_species_dict.keys()) if s != site]
            try:
                site_species = site_species_dict[site]
            except KeyError:
                print(f"One of the provided arguments was invalid: {site}")
                continue
            except:
                print("Something went wrong.")
                continue
            for species in unique(site_species, *other_species_sets):
                print(species)

        elif user_input[:10] == "species_in":
            species = get_arguments(user_input[10:])
            if len(species) != 1:
                print(f"The `user_input` command expected one argument. Received: {len(species)}. Enter `help` for more information.")
                continue
            species = species[0]
            for site in species_in(species, site_species_dict):
                print(site)

        elif user_input == 'q' or user_input == 'quit':
            end_program = True

        elif user_input == 'h' or user_input == 'help':
            print(_instructions)

    print("Goodbye.")

def species_in(species: str, sites_species_dict: dict[str, set]):
    for site in sites_species_dict.keys():
        if species in sites_species_dict[site]:
            yield site


def unique(site_species: set, *other_site_species: set) -> set:
    """Returns a set of species found in `site_species` that aren't found in `other_site_species`."""
    unique_species = site_species
    for other_site in other_site_species:
        unique_species = unique_species - other_site
    return unique_species

def common(*species_sets: set) -> set:
    """Returns a set of species that are common to all sets of species provided"""
    if len(species_sets) == 0: return set()
    common = species_sets[0]
    return common.intersection(*species_sets[1:])

def combined(*species_sets: set) -> set:
    """Returns the combined set of species found in all sets of species provided"""
    if len(species_sets) == 0: return set()
    return set().union(*species_sets)

def get_arguments(user_input: str) -> list[str]:
    """Turns a string of arguments separted by commas into a list of arguments"""
    args = user_input.split(',')
    args = [arg.strip() for arg in args]
    if args == ['']: return []
    return args

# def sites(site_species: dict):
#     """Generator"""
#     for site in site_species.keys():
#         yield site

def process_site_files(file_paths) -> dict[str, set]:
    """Turn the provided files into a dictionary where keys are the names of sites and values are sets of species spotted in the sites."""
    spotted_species = dict()
    for path in file_paths:
        with open(path, 'r') as f:
            site_name = f.readline().replace("\n","")
            # Create new empty species set for site if first time seeing site
            if site_name not in spotted_species.keys():
                spotted_species[site_name] = set()
            species_set = spotted_species[site_name]
            for line in f:
                species_set.add(line.replace("\n",""))
    return spotted_species    

def get_survey_files() -> list[str]:
    """Gets a list containing .txt files in this directory"""
    current_directory = os.getcwd()
    all_entries = os.listdir(current_directory)
    return [entry for entry in all_entries if os.path.isfile(os.path.join(current_directory, entry)) and entry[-4:] == ".txt"]


if __name__ == "__main__":
    run_ecological_survey()