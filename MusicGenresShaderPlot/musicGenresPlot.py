import moderngl
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets
from matplotlib.backend_bases import MouseButton
import pandas as pd
import os
import math
import copy

from PIL import Image

#load file as string:
def loadStringFile(path):
        file = open(path, 'r')
        result = file.read();
        file.close()
        return result

def loadStringFileArray(paths):
    result = "";
    for path in paths:
        file = open(path, 'r')
        result += file.read();
        file.close()
    return result;

#also first result is list of datasets names
def loadCSVFromDirectory(directoryPath):
    result = []
    result.append([])
    for file in os.listdir(directoryPath):
        result[0].append(file)
        result.append(pd.read_csv(directoryPath + "/" + file))
    return result


#-------------------------------------------------------
#GLOBALS
#load csv data from file
allData = loadCSVFromDirectory("data")
computeShader = None
fig = plt.figure()
labelAx = plt.axes([0.1, 0.15, 0.4, 0.8])
button_prev = None
slider_prev = None
slider2_prev = None
curBase = 0
curData = 1
#this is enum for traversing plot
moveState = 0 #0 nothing 1 translate 2 scale
scale = []
absoluteScale = []
startingPos = [0, 0]
moveStarted = True
lowXtext = None
upXtext = None
upYtext = None

#------------------------------------------------
#INTERACTION EVENTS
def switchBase(event):
    global curBase
    global labelAx
    global button_prev
    if (curBase == 0):
        curBase = 1;
        labelAx.set_xscale('log')
        button_prev.label.set_text('log scale')
    else:
        curBase = 0;
        labelAx.set_xscale('linear')
        button_prev.label.set_text('linear scale')
    computeShader['baseType'] = curBase
    #computeShader['data'] = allData[curData].loc[:, "y_values"]

def switchData(val):
    global curData
    global computeShader
    global slider_prev
    global allData
    curData = val;
    #sent data to gpu again
    if (val == 0): 
        computeShader['data'] = [0] * 1501
        slider_prev.label.set_text('None')
    else:
        computeShader['data'] = allData[curData].loc[:, "y_values"]
        slider_prev.label.set_text(allData[0][curData - 1])

def switchData2(val):
    global curData
    global computeShader
    global slider2_prev
    global allData
    curData = val;
    #sent data to gpu again
    if (val == 0): 
        computeShader['data2'] = [0] * 1501
        slider2_prev.label.set_text('None')
    else:
        computeShader['data2'] = allData[curData].loc[:, "y_values"]
        slider2_prev.label.set_text(allData[0][curData - 1])

def setLowXLim(expression):
    global scale
    global computeShader
    global lowXtext
    val = float(expression)
    if (val < absoluteScale[0]):
        val = absoluteScale[0]
        lowXtext.set_val(str(round(val, 3)))
    if (val > scale[2]):
        val = scale[2]
        lowXtext.set_val(str(round(val, 3)))
    scale[0] = val
    labelAx.set_xlim(scale[0], scale[2])
    computeShader['bounds'] = scale

def setLowYLim(expression):
    global scale
    global computeShader
    scale[1] = float(expression)
    labelAx.set_ylim(-scale[3], scale[3])
    computeShader['bounds'] = scale

def setUpXLim(expression):
    global scale
    global computeShader
    global lowXtext
    val = float(expression)
    if (val > absoluteScale[2]):
        val = absoluteScale[2]
        lowXtext.set_val(str(round(val, 3)))
    if (val < scale[0]):
        val = scale[0]
        lowXtext.set_val(str(round(val, 3)))
    scale[2] = val
    labelAx.set_xlim(scale[0], scale[2])
    computeShader['bounds'] = scale

def setUpYLim(expression):
    global scale
    global computeShader
    global upYtext
    val = float(expression)
    if (val < absoluteScale[1]):
        val = absoluteScale[1]
        lowXtext.set_val(str(round(val, 3)))
    scale[3] = val
    labelAx.set_ylim(-scale[3], scale[3])
    computeShader['bounds'] = scale

#UNUSED!!!!!!
def scrollZoom(event):
    if (event.button == 'up'):
        scale[0] *= scale[0] * 0.1;
        scale[1] += scale[0] * 0.1;
    else:
        scale[0] -= scale[0] * 0.1;
        scale[1] -= scale[0] * 0.1;
    #computeShader['bounds'] = scale

ctx = moderngl.create_context(standalone=True)

compute_shader_code = loadStringFile("shaders/main.glsl")

computeShader = ctx.compute_shader(source=compute_shader_code)
texture = ctx.texture((512, 512), 4)

w, h = texture.size
gw, gh = 16, 16
nx, ny, nz = int(texture.size[0]/16), int(texture.size[0]/16), 1


texture.bind_to_image(0, read=False, write=True)

#initialize uniforms
backgroundColor = (0.1, 0.2, 0.5, 0.3)#[0.9, 0.9, 0.9, 1]
bar1Color = [0.35, 0.2, 0.9, 1]
bar2Color = [0.8, 0.7, 0.5, 1]
x_step = allData[1].loc[:, "x_values"][1]
scale = [x_step, 0, allData[1].loc[:, "x_values"][1500], allData[1].loc[:, "y_values"].max()]
#get max from all gathered data:
for i in range(2, len(allData)):
    maxVal = allData[i].loc[:, "y_values"].max()
    if (scale[3] < maxVal):
        scale[3] = maxVal;
bar_width = allData[1].loc[:, "x_values"][1] * 0.5
absoluteScale = copy.deepcopy(scale)

#---------------------------------------------------------
#MATPOLTLIB SETUP
fig.set_size_inches(8, 4)
#fig(figsize=(1, 1))
buttonAx = plt.axes([0.75, 0.1, 0.2, 0.1])
sliderAx = plt.axes([0.75, 0.3, 0.2, 0.1])
slider2Ax = plt.axes([0.75, 0.5, 0.2, 0.1])
lowXlim = plt.axes([0.75, 0.6, 0.2, 0.1])
#lowXlim = plt.axes([0.75, 0.6, 0.2, 0.1])
upXlim = plt.axes([0.75, 0.7, 0.2, 0.1])
upYlim = plt.axes([0.75, 0.8, 0.2, 0.1])

button_prev = matplotlib.widgets.Button(buttonAx, 'linear scale', color=(0.65, 0.65, 0.7, 1), hovercolor=(0.4, 0.6, 0.8, 1))
button_prev.on_clicked(switchBase);

#dropdown is not avaible at all so
#I need to use a slider
#needs special override for non values
slider_prev = matplotlib.widgets.Slider(
    sliderAx, "None", 0, len(allData[0]),
    valinit=0, valstep=1, #this can be non linear
    color=bar1Color
)
slider_prev.on_changed(switchData)

slider2_prev = matplotlib.widgets.Slider(
    slider2Ax, "None", 0, len(allData[0]),
    valinit=0, valstep=1, #this can be non linear
    color=bar2Color
)
slider2_prev.on_changed(switchData2)

lowXtext = matplotlib.widgets.TextBox(lowXlim, "Low X Limit", textalignment="center")
lowXtext.on_submit(setLowXLim)
lowXtext.set_val(str(round(scale[0], 3)))
#lowYtext = TextBox(lowYlim, "Evaluate", textalignment="center")
#lowYtext.on_submit(submit)
upXtext = matplotlib.widgets.TextBox(upXlim, "Up X Limit", textalignment="center")
upXtext.on_submit(setUpXLim)
upXtext.set_val(str(round(scale[2], 3)))
upYtext = matplotlib.widgets.TextBox(upYlim, "Up Y Limit", textalignment="center")
upYtext.on_submit(setUpYLim)
upYtext.set_val(str(round(scale[3], 3)))


computeShader['backgroundColor'] = backgroundColor
computeShader['bar1Color'] = bar1Color
computeShader['bar2Color'] = bar2Color
computeShader['resolution'] = texture.size
computeShader['x_step'] = x_step
computeShader['bounds'] = scale
computeShader['bar_width'] = bar_width
#print(allData[0].loc[:, "y_values"].size)

computeShader['data'] = [0] * 1501
computeShader['data2'] = [0] * 1501
computeShader['data2'] = [0] * 1501

#-------------------------------------------------------------
#FINAL PLOT SETUP:

#axes labels need to be set separately in empty plot
labelAx.set_xlim(scale[0], scale[2])
labelAx.set_ylim(-scale[3], scale[3])
labelAx.set_xlabel('frequency band (Hz)')
labelAx.set_ylabel('mean amplitude')

finalAx = plt.axes([-0.1, 0.15, 0.8, 0.8])
plt.axis('off')

ctx.clear(0.3, 0.3, 0.3)
computeShader.run(nx, ny, nz)
#initialize per frame uniforms

#prerender and initialize image
texture.use(location=0)
data = ctx.buffer(reserve=8)
texture.read_into(data)
mainTexture = Image.frombytes(
"RGBA", texture.size, texture.read(),
"raw", "RGBA", 0, -1
)
imagePlot = plt.imshow(mainTexture)

#dynamic loop
while (True):
    ctx.clear(0.3, 0.3, 0.3)
    computeShader.run(nx, ny, nz)
    #initialize per frame uniforms
    #real time stuff

    #render
    texture.use(location=0)
    data = ctx.buffer(reserve=8)
    texture.read_into(data)
    mainTexture = Image.frombytes(
    "RGBA", texture.size, texture.read(),
    "raw", "RGBA", 0, -1
    )
    imagePlot.set_data(mainTexture)
    fig.canvas.draw()
    plt.pause(0.1)
