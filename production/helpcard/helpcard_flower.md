=Flower Generator<| procedural flower creator =
#type:node
#context:object
"""Quickly creates a fully procedural simple flower, customizable with user inputs."""

@overview

The asset can be used to easily produce simple flowers structures
allowing control over the final shape by shaping the stem, the petals and the stamen.

The parameters for the asset are divided in three sections based on the main parts of the flower:
    * *Stem*: defines the shape, the bending and the cross section of the flower.
    * *Stamen*: switches between the flat stamen base and stamen filaments.
    * *Petals*: controls petals scattering, bending and their rotation.

@inputs
The Flower Generator node takes up to two inputs respectively for the stem and the petals.
If no input is added, defaul geometry is used instead.

@parameters

==Stem==

Gives control over the stem shape. If no input is added,
a custom skeleton for the stem is used.

NOTE:
        #display: magenta
        :box:
            #dir: left
            #display: magenta      
            
            The custom stem geometry has to be a simple line, not a mesh.

~~~
~~~
===Shape===

*Length*:
    #id: internalname
    
    Stem length.
    
*Radius*:
    #id: internalname
    
    Changes cross section for the stem across its length.
    
*Radius Multiplicator*:
    #id: internalname
    
    Scales the *Radius* by a constant value.
    
*Distortion Scale*:
    #id: internalname
    
    Creates various random bends along the stem moving its points.
    Set the maximum offset each point can assume.
    
*Random Seed*:
    #id: internalname
    
    Creates random variations along the stem.
    
*Points*:
    #id: internalname
    
    Number of points of the stem geometry.
    Increase to have a more defined shape.

~~~    
===Bending===

====Deformation====

*Bend*:
    #id: internalname
    
    Angle in degrees to bend. You can make this over 180
    to bend something over itself multiple times.
    
*Up Vector*:
    #id: internalname
    
    The bend is always perpendicular to the capture axis,
    but this specifies what orientation it should use.
    
*Twist*:
    #id: internalname
    
    Angle in degrees to rotate around the capture axis.
    Can be over 180 to twist multiple times int he interval.
    
*Preserve Volume*:
    #id: internalname
    
    If scaling the length, a corresponding inverse scale will be performed
    on the other axes to roughly preserve volume.
    Because this is applied smoothly, it is not an accurate
    volume preservation but is of the appropriate magnitude.
    
    
====Capture====

*Capture Origin*:
    #id: internalname
    
    The center of the source capture plane.
    
*Capture Direction*:
    #id: internalname
    
    The normal of the capture planes, and the direction
    pointing to the destination capture plane from the source.
    
*Capture Length*:
    #id: internalname
    
    Controls the region of space that receives
    the partial transforms. Must be non-zero in length.

~~~
===Sculpt===
Gives more refined control over the stem mesh.

*Enable Sculpting*:
    #id: internalname
    
    Enables sculpting: use the brush in the viewport
    to add more details to the stem geometry.
    
*Reset All Changes*:
    #id: internalname
    
    Reset changes applied with the scuplt tool.
    
*End*:
    #id: internalname
    
    Press to quit sculpting mode and save changes.
    
    
~~~
~~~

==Stamen==

Gives control over the central part of the flower.
You can choose your custom geometry or modify the built in models.

*Type*:
    #id: internalname
    
    Choose between a round-like stamen base or filaments.
    
    *Filaments*: for more like a lily final look.
    
    *Base*: choose it if you aim for a daisy/sunflower look.

~~~
===Filaments===
This tab is only visible when the *Type* is set to *Filaments*.
You can use your custom geometry or a built in model
that you can further manipulate with different bending tools.

*Custom Filament*:
    #id: internalname
    
    Path to custom filament object.
    
====Bend====

*Average Angle*:
    #id: internalname
    
    Path to custom filament object.
    
*Additional Angle (Random)*:
    #id: internalname
    
    Path to custom filament object.
    
====Length====

*Average Length*:
    #id: internalname
    
    Filament Length.
    
*Additional Length (Random)*:
    #id: internalname
    
    Adds a random additional length within the given range.
    
*Radius*:
    #id: internalname
    
    Changes cross section for the filament across its length.
    
*Radius Multiplicator*:
    #id: internalname
    
    Scales the *Radius* by a constant value.

*Points*:
    #id: internalname
    
    Number of points of the stem geometry.
    Increase to have a more defined shape.
    
*Distortion Scale*:
    #id: internalname
    
    Creates various random bends along the filament moving its points.
    Set the maximum offset each point can assume.
    
*Random Seed*:
    #id: internalname
    
    Creates random variations along the filament.
  
    
====Instancing====

*Total Count*:
    #id: internalname
    
    Total number of filaments.
    
*Filaments Separation*:
    #id: internalname
    
    Distance between filaments.
    Higher numbers determine greater distance.
    
*Bloom*:
    #id: internalname
    
    Filaments are organized similarly to petals crown.
    Here you can set how open the crown for filament is.
    E.g.: 0 means the filaments are oriented vertically compared to their base.
    1 means they lay flat.

~~~
===Stamen Base===
This tab is only visible when the *Type* is set to *Base*.
You can use your custom geometry or a built in model
that you can further manipulate with a sculpt tool.

*Custom Base*:
    #id: internalname
    
    Path to custom stamen base object.
    
*Specie*:
    #id: internalname
    
    Choose between two built in models for the stamen base.
    The two options are *Sunflower* and *Daisy*.
    
*Uniform Scale*:
    #id: internalname
    
    Scale the stamen base uniformly along xyz axis.
    
====Sculpt====
Gives more refined control over the stamen base mesh.

*Enable Sculpting*:
    #id: internalname
    
    Enables sculpting: use the brush in the viewport
    to add more details to the stem base geometry.
    
*Reset All Changes*:
    #id: internalname
    
    Reset changes applied with the scuplt tool.
    
*End*:
    #id: internalname
    
    Press to quit sculpting mode and save changes.
    
~~~
~~~
==Petals==

*Specie*:
    #id: internalname
    
    Let you choose between built in geometry for petals.
    
*Total Count*:
    #id: internalname
    
    Total number of petals.
    
*Scale*:
    #id: internalname
    
    Scale petal geometry along x, y, z at the time.
    
*Additional Length*:
    #id: internalname
    
    Random additional length value for petals length
    calculated within the given range.

*Random Seed*:
    #id: internalname
    
    Randomply modifies the achieved geometry.
    
*Separation*:
    #id: internalname
    
    Changes distance between petals.

~~~
===Rotation===

*Rotate*:
    #id: internalname
    
    Twist petals around their axes.
    Change this value if you want the petals not to face all the same direction.
    
*Spin*:
    #id: internalname
    
    Move to change petals inclination relative to stamen base normals.
    Petals will remain on the same plane as before.
        
*Bloom*:
    #id: internalname
    
    Open/closes petals.

~~~
===Instancing===

*Min Heigth*:
    #id: internalname
    
    Initial heigth measured on stamen base for petals to be born.
    
*Max Height*:
    #id: internalname
    
    Maximum height calculated on the base stamen shape for petals to be scattered.
    
*Roll the Dice*:
    #id: internalname
    
    Randomly rearrange petals.
    
*Diffusion*:
    #id: internalname
    
    Prune some petals to avoid clumpiness.
    
*Relax Iterations*:
    #id: internalname
    
    Petals will be relaxed, pushed away from each other, to avoid clumping.
    
*Scale Radii By*:
    #id: internalname
    
    Point radii will be scaled by this before any relaxing of the points.
    Specifying a scale less than 1 will increase "clumpiness" of the resulting points,
    with a value of zero resulting in no relaxation.
