This part of the project allows to see interactive plot
for visualizing differences in frequency spectrum of music generes

The project consist of 2 source code files
1 file for python implementation "musicGenresPlot.py"
and 1 compute shader file "main.glsl" (in "shaders" cathegory)

All required python libraries listed at the start of python implementation file 
no additional libraries / plugins needed other than that

No build provided, building python application on client's behalf!

The program loads already processed data of frequencies per genre
correct format requires .csv file with 1 column labeled "y_values"
followed by 1501 rows of data (float)
and column "x_values" (must be uniformly distributed) from which the step
between frequencies is taken

2 datasets provided withing program that were used in original presentation:
cathegory "General" (non particular songs derived into genres)
cathegory "Crypt" (covers for the game "crypt of the necrodancer")

The program simply loads all correctly formatted data from folder "data",
so choosing dataset is by manually placing down files in that cathegory

The end result is a plot with changable slider (genere to show)
(2 generes can be shown at once to make a comparison)
switch between linear and log scale in x
and set of plot limits by input field
(plot will not change size besides the size of actual data,
except for y where there are no bounds)

Adam Migdalski 2024