# ecological-survey
An assignment for students to practice processing user input, load data from text files to create sets, use conditionals to redirect flow to the right function calls with the right parameters, and use appropriate set methods for the requested task.


## Example
``` console
% python3 ecological_survey.py
Please enter the path to the folder containing data of your ecological survey:
% <FILEPATH1>
This folder contains 0 .txt files. Please enter a file path to a folder that has at least one .txt file.
% <FILEPATH2>
This folder has 3 .txt files containing data from: dense forest, volcano, cave.
What would you like to know? Enter...
     - "common <area1> <area2> ... <areaN>" to get species that the provided areas have in common. If no areas are provided, species common to all areas will be shown.
     - "combined <area1> <area2> ... <areaN>" to get species found across the areas provided. If no areas are provided, all species will be returned.
     - "unique <area>" to get species that are unique to the provided area (not found in any of the others).
     - "species_in <species> <area1> <area2> ... <areaN>" to get a boolean indicating whether or not `species` is in all of the areas provided. If no areas are provided, it will indicate if the species is in all of the areas.
     - "q" or "quit" to exit the program.
     - "h" or "help" to receive these instructions again.
% common forest volcano
leafcutter ant, tarantula, pit viper
% help
What would you like to know? Enter...
     - "common <area1> <area2> ... <areaN>" to get species that the provided areas have in common. If no areas are provided, species common to all areas will be shown.
     - "combined <area1> <area2> ... <areaN>" to get species found across the areas provided. If no areas are provided, all species will be returned.
     - "unique <area>" to get species that are unique to the provided area (not found in any of the others).
     - "species_in <species> <area1> <area2> ... <areaN>" to get a boolean indicating whether or not `species` is in all of the areas provided. If no areas are provided, it will indicate if the species is in all of the areas.
     - "q" or "quit" to exit the program.
% q
Goodbye.
%
```