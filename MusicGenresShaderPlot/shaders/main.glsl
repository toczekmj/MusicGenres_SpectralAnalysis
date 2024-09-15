#version 430

layout (local_size_x = 16, local_size_y = 16) in;
// match the input texture format!
layout(rgba8, location=0) writeonly uniform image2D destTex;


uniform ivec2 resolution;
uniform vec4 backgroundColor;
uniform vec4 bar1Color;
uniform vec4 bar2Color;
uniform vec4 lineColor;
uniform int baseType;
uniform vec4 bounds; //low x low y up x up y
uniform float bar_width;
uniform float x_step;

uniform float[1501] data;
uniform float[1501] data2;

uniform float u_time;

void main() {
    // texel coordinate we are writing to
    ivec2 texelPos = ivec2(gl_GlobalInvocationID.xy);
    vec2 uv = vec2(texelPos.x, texelPos.y) / resolution;
    //this is lin space use log space
    //also mirrors y value (just looks better)
    vec2 pos = vec2(uv.x, abs(uv.y - 0.5) * 2) * vec2(bounds.z - bounds.x, bounds.w - bounds.y);
    pos += vec2(bounds.x, bounds.y);

    //log space in x and y
    vec2 logPos = vec2(exp(uv.x * log(bounds.z - bounds.x)) + bounds.x, exp(uv.y * log(bounds.w - bounds.y)) + bounds.y);

    vec4 col = backgroundColor;

    if (baseType == 1)
    {
        pos.x = logPos.x;
        //pos.x = 0;
    }

    float pos1y = 0;
    float pos2y = 0;
    
    if (baseType == 0)
    {
        //barPlot
        int closestX = int(round(pos.x / x_step));
        float barMod = mod(pos.x, x_step);
        if ( min(barMod, abs(x_step - barMod)) < bar_width)
        {
            pos1y = data[closestX];
        }
    }
    else if (baseType == 1)
    {
        //smoothstepPlot (yeah, no cubic splines here)
        int lowboundX = int(floor(pos.x / x_step));
        int upboundX = int(ceil(pos.x / x_step));
        float pointMod = mod(pos.x, x_step);
        
        //version in real space (unused)
        //float smoothPercent = smoothstep(0, 1, fract(pos.x / x_step));
        //version in screen space (looks better)
        float lowboundScreen = log(x_step * lowboundX) / log(bounds.z);
        float upboundScreen = log(x_step * upboundX) / log(bounds.z);
        float smoothPercent = smoothstep(0, 1, (log(pos.x) / log(bounds.z) - lowboundScreen) / (upboundScreen - lowboundScreen) );
        float lowbound = data[lowboundX];
        float upbound = data[upboundX];

        //have no idead why but first sample doesn't work
        if (lowboundX == 0)
        {
            smoothPercent = smoothstep(0, 1, log(pos.x) / log(bounds.z) / upboundScreen );
        }

        pos1y = lowbound + (upbound - lowbound) * smoothPercent;

    }

    //--------------------------------------------------
    //repeat the whole program for second graph:
        if (baseType == 0)
    {
        //barPlot
        int closestX = int(round(pos.x / x_step));
        float barMod = mod(pos.x, x_step);
        if ( min(barMod, abs(x_step - barMod)) < bar_width)
        {
            pos2y = data2[closestX];
        }
    }
    else if (baseType == 1)
    {
        //smoothstepPlot (yeah, no cubic splines here)
        int lowboundX = int(floor(pos.x / x_step));
        int upboundX = int(ceil(pos.x / x_step));
        float pointMod = mod(pos.x, x_step);
        
        //version in real space (unused)
        //float smoothPercent = smoothstep(0, 1, fract(pos.x / x_step));
        //version in screen space (looks better)
        float lowboundScreen = log(x_step * lowboundX) / log(bounds.z);
        float upboundScreen = log(x_step * upboundX) / log(bounds.z);
        float smoothPercent = smoothstep(0, 1, (log(pos.x) / log(bounds.z) - lowboundScreen) / (upboundScreen - lowboundScreen) );
        float lowbound = data2[lowboundX];
        float upbound = data2[upboundX];

        //have no idead why but first sample doesn't work
        if (lowboundX == 0)
        {
            smoothPercent = smoothstep(0, 1, log(pos.x) / log(bounds.z) / upboundScreen );
        }

        pos2y = lowbound + (upbound - lowbound) * smoothPercent;

    }

    vec4 dataMixCol = vec4(0, 0, 0, 1);
    //vec4 dataMixCol = mix(bar1Color, bar2Color, 0.5f);
    //color mixing
    //not hitting anything
    if (pos.y > max(pos1y, pos2y))
    {
        
    }
    else if (pos1y < pos2y) //pos1 lower
    {
        if (pos.y < pos1y)
        {
            dataMixCol = mix(bar1Color, bar2Color, (1 - pos.y / pos1y));
        }
        else
        {
            dataMixCol = bar2Color;
        }
    }
    else //pos2y lower
    {
        if (pos.y < pos2y)
        {
            dataMixCol = mix(bar2Color, bar1Color, (1 - pos.y / pos2y));
        }
        else
        {
            dataMixCol = bar1Color;
        }
    }

    //shade downside slightly
    if (uv.y < 0.5)
    {
        dataMixCol.xyz *= 0.8f;
    }

    //only for testing
    if (dataMixCol.x > 0.01)
    {
        col = dataMixCol;
    }


    //return
    imageStore(destTex, texelPos, col);
}