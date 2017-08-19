=Tree Generator<| procedural trees creator =
#type:node
#context:object
"""Quickly creates a fully procedural tree, customizable with user inputs."""

@overview

The asset can be used to easily produce natural tree structures allowing control over the growth by
shaping the roots, the foliage and the way the tree fills up the space.

The asset implements the [space colonization algorithm|http://algorithmicbotany.org/papers/colonization.egwnp2007.large.pdf]
by Runions et al (2005).
The algorithm takes as input roots points and a geometry for the tree crown shape.
The process works on a per point base: points are divided between attraction points and tree nodes.
Tree nodes are points that, when linked together, will create the tree structure: the first tree nodes are the root points.
Attraction points represent the available space and they will influence the growth direction of the tree nodes: attractions points 
are seeded in the volume of the tree crown geometry.
Shortly, at each iteration the colonization algorithm needs to first find the set of attraction points
(if any) that will influence each fertile tree node, create the new nodes in the direction determined 
by the influencing attraction points, and decide which attraction points will survive to the next iteration.

The parameters for the asset are divided in three sections:
    * *Setup*: defines the roots, the tree crown shape and the distribution for the attraction points.
    * *Growth*: defines number of iteration for the colonization algorithm as well as parameters to find influencing attraction points.
    * *Post Processing*: controls leaves scattering, tree mesh geometry smooth and shading options.
    
Different options are available to prepare the final layout:
    * *Foliage* will create a simple tree.
    * *Collision* allows to define a collision object for the tree to avoid.
    * *Wrap* will give a vine-like final branching structure that wraps around a given geometry.

@inputs
The Tree Generator node does not take any input.
Custom geometry can be added by specifying the path to the object in the relevant fields.

@parameters

==General Control==

*Visualize Setup*:
    #id: internalname
    
    Toggle to enable visibility over the setup options.
    
    NOTE:
        #display: magenta
        :box:
            #dir: left
            #display: magenta      
            
            The network requires time to cook. You might want to keep the toggle on
            while tuning the parameters and untoggle to see the whole tree.

~~~
==Setup==

Here you can set the roots points for the tree either by specifying their coordinates,
setting the path to a group of points or using a custom structure for the trunk.
Alongside the roots, you can choose the tree crown shape, add a collision object or set the tree to grow like a vine around an object of your choice.

~~~
~~~
===Roots===
*Visualize Roots*:
    #id: internalname
    
    When toggle *Visualize Setup* is on, switches visibility for root points.
    
*Root Type*:
    #id: internalname
    
    Defines the root type for the first tree nodes.
    
    *Single Roots*: for adding single points by specifying the coordinates.
    
    *Group of Roots*: takes the path to an external node where the points are specified.
    
    *Trunk Structure*: takes a curves geometry hierarchy and selects some of these points as roots for the colonization algorithm.

~~~
====Single Points====
You can set the root points by setting their total count in the *Number of Point* slot
and place them in different positions by specifying their coordinates.
This tab is only available when *Root Type* is set to *Single Roots*.

*Number of Points*:
    #id: internalname
    
    Total count of roots points. When increased, a new slot for point coordinates is added.

~~~
====Group Points====

Input a custom group of points: they will be the roots of the tree.
This tab is only available when *Root Type* is set to *Group of Roots*.

*Group*:
    #id: internalname
    
    Path to the object that contains the points to use as roots.

=====Transform=====

*Translate*:
    #id: internalname
    
    Amount of rotation about xyz axes.
    
*Rotate*:
    #id: internalname
    
    Rotate the geometry by the specified angle around the x, y, z axis.

*Scale*:
    #id: internalname
    
    Scale the geometry along the x, y, z axis.
    
*Shear*:
    #id: internalname
    
    Deform the geometry along x, y, z axis.
    
*Pivot*:
    #id: internalname
    
    Move the pivot to the specified coordinates.

*Uniform Scale*:
    #id: internalname
    
    Scale the input geometry uniformly along the x, y, z axis.

~~~

====Trunk====

You can decide to grow the tree from a pre-made base skeleton. Here you can specify the path to
your basic shape for the tree and set some of their points as roots for the new branches to come.
This tab is only available when *Root Type* is set to *Trunk Structure*.

WARNING:
        #display: red
        :box:
            #dir: left
            #display: red      
            
            Make sure that the first primitive of the object is the main trunk,
            the next ones are the first order branches and so on.

*Trunk Object*:
    #id: internalname
    
    Path to the object that contains the curves to use as trunk.
    
*Discretization*:
    #id: internalname
    
    Choose one every `value` points of the trunk as root points.
    Example: if set to 3, one every three points is set as root.

=====Transform=====

*Translate*:
    #id: internalname
    
    Amount of rotation about xyz axes.
    
*Rotate*:
    #id: internalname
    
    Rotate the geometry by the specified angle around the x, y, z axis.

*Scale*:
    #id: internalname
    
    Scale the geometry along the x, y, z axis.
    
*Shear*:
    #id: internalname
    
    Deform the geometry along x, y, z axis.
    
*Pivot*:
    #id: internalname
    
    Move the pivot to the specified coordinates.

*Uniform Scale*:
    #id: internalname
    
    Scale the input geometry uniformly along the x, y, z axis.

~~~
~~~
===Foliage===

You can specify a custom shape for tree crown, as well as a collision object.
This way, you can produce a tree aware of surrounding obstacles.
Its geometry will bend to avoid that object. If you aim for a vine-like final look, 
the *Wrap* options creates a layer around an object of your choice where the plant will grow.

*Visualize Foliage*:
    #id: internalname
    
    When toggle *Visualize Setup* is on, switches visibility for foliage shape.
    
*Grow Type*:
    #id: internalname
    
    Defines the type for the tree crown shape.
    
    *Foliage*: specify tree crown shape.
    
    *Collision Object*: select to specify an object for the tree to avoid.
    
    *Wrap Object*: select to specify an object for the tree to cling on.

~~~
====Foliage Shape====
This tab is only available when *Grow Type* is set to either *Foliage* or *Collision Object*.

*Custom Geometry*:
    #id: internalname
    
    Path to the tree crown envelope geometry.
    If left empty a teapot is used.
    
=====Transform=====

*Translate*:
    #id: internalname
    
    Amount of rotation about xyz axes.
    
*Rotate*:
    #id: internalname
    
    Rotate the geometry by the specified angle around the x, y, z axis.

*Scale*:
    #id: internalname
    
    Scale the geometry along the x, y, z axis.
    
*Shear*:
    #id: internalname
    
    Deform the geometry along x, y, z axis.
    
*Pivot*:
    #id: internalname
    
    Move the pivot to the specified coordinates.

*Uniform Scale*:
    #id: internalname
    
    Scale the input geometry uniformly along the x, y, z axis.

~~~

====Collision====
This tab is only available when *Grow Type* is set to *Collision Object*.

*Custom Geometry*:
    #id: internalname
    
    Path to the collision object geometry. If empty a simple house shape is used.
    
=====Transform=====

*Translate*:
    #id: internalname
    
    Amount of rotation about xyz axes.
    
*Rotate*:
    #id: internalname
    
    Rotate the geometry by the specified angle around the x, y, z axis.

*Scale*:
    #id: internalname
    
    Scale the geometry along the x, y, z axis.
    
*Shear*:
    #id: internalname
    
    Deform the geometry along x, y, z axis.
    
*Pivot*:
    #id: internalname
    
    Move the pivot to the specified coordinates.

*Uniform Scale*:
    #id: internalname
    
    Scale the input geometry uniformly along the x, y, z axis.

~~~

===Wrap===

For a vine-like final look.
This tab is only available when *Grow Type* is set to *Wrap Object*.

WARNING:
    #display: red
    :box:
        #dir: left
        #display: red      
        
        If the toggle *Visualize Setup* is off and the geometry turns black,
        the root points may be too far from the wrap object. Move them closer
        and re cook the node.

*Custom Geometry*:
    #id: internalname
    
    Path to the object the tree will cling onto. If empty an angel statue model is used.
    
=====Transform=====

*Translate*:
    #id: internalname
    
    Amount of rotation about xyz axes.
    
*Rotate*:
    #id: internalname
    
    Rotate the geometry by the specified angle around the x, y, z axis.

*Scale*:
    #id: internalname
    
    Scale the geometry along the x, y, z axis.
    
*Shear*:
    #id: internalname
    
    Deform the geometry along x, y, z axis.
    
*Pivot*:
    #id: internalname
    
    Move the pivot to the specified coordinates.

*Uniform Scale*:
    #id: internalname
    
    Scale the input geometry uniformly along the x, y, z axis.
    
=====Bounds=====
Create the tree crown shape as a thick layer wrapped around the input object.
The difference between the *Outside Bound* and the *Inside Bound* is the thickness of such layer.

WARNING:
    #display: red
    :box:
        #dir: left
        #display: red      
        
        Make sure that *Outside Bound > Inside Bound*

*Outside Bound*:
    #id: internalname
    
    External surface for the layer wrapping the object, calculated from the surface of the wrap object.
    
*Inside Bound*:
    #id: internalname
    
    Internal surface for the layer wrapping the object, calculated from the surface of the wrap object.
    
    TIP:
        #display: green
        :box:
            #display: green
            
            You might want to keep this value slightly above zero to avoid branches growing inside the geometry.

~~~
~~~
===Attractors===

Attraction points represent the empty space. Here you can set the granularity of this space.
To achieve custom density distributions, first the volume occupied by the tree crown shape
is seeded with points (*Number of Attractors*).
Based on the *Distribution Type*, some of these points are removed based on a *probability* parameter.
The remaining points are the attraction points that will interact with the space colonization algorithm.


*Visualize Attractors*:
    #id: internalname
    
    When toggle *Visualize Setup* is on, switches visibility for attraction points.
    
*Number of Attractors*:
    #id: internalname
    
    Total number of attraction points seeded in the tree crown envelope.
    
*Distribution Type*:
    #id: internalname
    
    Defines the density of attraction points in the tree crown volume.
    
    *Uniform*: attraction points density is uniform throughout the whole shape.
    
    *Radial*: set varying density from the centroid of the object to its surface.
    
    *Vertical Axis*: set varying density along the Y axis.

~~~

====Radial Distribution====

Achieves a varying density for attraction points from the center of the tree crown object to its surface.
This tab is only available when *Distribution Type* is set to *Radial*.

*Probability*:
    #id: internalname
    
    Ramp function of the distance of the point from the surface of the tree crown shape. The probability values set how likely it is for a point to be removed.
    Moving the values will make the density of attraction points more sparse or more dense across the volume.
    
*Mult*:
    #id: internalname
    
    Rescale *Probability* to a new range.

~~~

====Vertical Distribution====

Achieves a varying density for attraction points along the Y axis.
This tab is only available when *Distribution Type* is set to *Vertical Axis*.

*Probability*:
    #id: internalname
    
    Ramp function of Y coordinate of the point. The probability values set how likely it is for a point to be removed.
    Moving the values will make the density of attraction points more sparse or more dense across the volume, along the Y axis.
    
*Mult*:
    #id: internalname
    
    Rescale *Probability* to a new range.
~~~
~~~
~~~

==Growth==

*Iterations*:
    #id: internalname
    
    Increase to get more mature trees, decrease to get shrubs.
    
    NOTE:
        #display: purple
        :box:
            #dir: left
            #display: purple      
            
            Since the tree grows inside the tree crown shape, only high iteration values (20 for the default geometry)
            can make the tree structure fill the volume nicely.

~~~
~~~
===Attraction Options===
Set attraction points options. Attraction points influence the tree growth as they represent the free space.

~~~
====Radius of Influence====

*Radius of Influence*:
    #id: internalname
    
    Specify the distance from which the branches can sense the empty space.

~~~
====Kill Distance====
Attraction points are removed when branches approach them meaning that the space is not empty anymore.
    
*Constant Kill Distance*:
    #id: internalname    

    The minimum distance from the branches to declare the space as "occupied", remains constant
    across successive iterations.
    
*Enable Scaling*:
    #id: internalname
    
    Toggle between a *Constant Kill Distance* and a varying one
    
*Initial Kill Distance*:
    #id: internalname
    
    Initial minimum distance from the branches to declare the space as "occupied"
    
*Ramp*:
    #id: internalname
    
    Scales the *Initial Kill Distance* across consecutive iterations.
    
    TIP:
        #display: green
        :box:
            #dir: left
            #display: green      
            
            Decrease the ramp value to get smaller and denser twigs closer to the tree crown surface.

~~~            
~~~
===Branching Options===

Set branching properties for the tree.

*Branching Start*:
    #id: internalname
    
    Set iteration value for roots to start to branch out.
    When the *Iterations* value is less than the *Branching Start* value, branches grow without forking.
    
*Kids*:
    #id: internalname
    
    Set maximum amount of branches per junction.

~~~
====Branch Length====

*Initial Length*:
    #id: internalname
    
    Initial length of branches
    
*Constant Scaling*:
    #id: internalname
    
    Scaling factor across generations. Branches of each generation will be as long as a fraction of their parent branches length.
    
    For example, if the value is `0.75`, every new generation branch will measure `0.75` times the length of the parent branches.
    
*Enable Ramp Scaling*:
    #id: internalname
    
    Enables custom scaling factor across generations.
    
*Ramp Scaling*:
    #id: internalname
    
    Manually modify the scaling factor across generations. Here you can decide to keep the same
    length for more than one generation, increase or decrease the length on a per generation basis.

~~~
====Angle Correction====

Sometimes, especially for low generation values, branches might grow too close too each other giving a cramped look.
Here you can set a minimum angle between branches and at which generation to start applying this correction.

*Enable*:
    #id: internalname
    
    Enables angle correction between siblings branches.
    
*Angle*:
    #id: internalname
    
    Set minimum angle allowed between siblings branches.

*Gen Correction*:
    #id: internalname
    
    Set generation from which to start correcting the angles.
    

~~~
~~~
===Pruning===
You can prune branches randomly or based on the distance from the tree crown shape to achieve a more natural look.

====Probability====

*Enable*:
    #id: internalname
    
    Enables pruning based on a probability value.
    
*Kill Gen*:
    #id: internalname
    
    Set minimum generation value for the pruning to start affecting the tree growth.

*Probability*:
    #id: internalname
    
    Set probability value of survival for branches.

~~~
====Bounding Object====

*Enable*:
    #id: internalname
    
    Enables pruning based on distance from the tree crown surface.
    
*Min Dist*:
    #id: internalname
    
    Minimum distance of a branch from the tree crown surface.

*Generation*:
    #id: internalname
    
    Set generation from which to start applying the minimum distance rule.
    
    WARNING:
        #display: red
        :box:
            #dir: left
            #display: red      
            
            If set to low values, it may prevent the tree from growing at all.
~~~
~~~
~~~
==Post Processing==

Refine the created tree by choosing colors, adding shaders, smoothing the geometry or increasing/decreasing the resolution.
Add leaves from default geometry or from a custom model.

*Flip Normals*:
    #id: internalname
    
    When the *Foliage Type* is set to *Collision Object* or *Wrap Object*,
    it may happens that either the tree or the object appear with reversed normals
    causing issues. Use the toggle *Flip Normals* to to have outward pointing normals.

~~~
~~~
===Tree Structure===

*Color Type*:
    #id: internalname
    
    Choose either plain color or select a shader from the shop.
    
    *Simple Color*: uniform color for tree geometry.
    
    *Shading*: provides shader options.

~~~    
====Color====
This tab is only available when *Color Type* is set to *Simple Color*.

*Color Type*:
    #id: internalname
    
    Set color for tree mesh.
    
~~~
====Shading====
This tab is only available when *Color Type* is set to *Shading*.

*Number of Materials*:
    #id: internalname
    
    The path of the material to assign.
    Click the [Smallicon:../../icons/BUTTONS/chooser_node.svg] chooser icon 
    to choose the material from a list.

~~~
====Width====

*Width Type*:
    #id: internalname
    
    Choose scaling method.
    
    *Ramp Scale*: uniform color for tree geometry.
    
    *Leonardo's Scale*: provides shader options.
    
=====Ramp Scale=====

The thickness of branches decreases across
generations according to the *Scale* ramp control.
In case of a custom trunk geometry, the thickness for the trunk
and the newly generated branches have two different controls.
Choose *From Trunk* parameters to manipulate the trunk width,
*Trunk Branches* for the branches being born based on the trunk.
This tab is only available when *Width Type* is set to *Ramp Scale*.

======Points======
This tab is only available when *Root Type* is set to either *Single Roots* or "Group of Roots".

*Mult*:
    #id: internalname
    
    Scale branches width uniformely across the tree geometry.

*Scale*:
    #id: internalname
    
    Change width of the branches across generations.
    
======Trunk Branches======
This tab is only available when *Root Type* is set to either *Trunk Structure".

*Scale*:
    #id: internalname
    
    Scale width of the branches generated in the *Growth* part.
    
======From Trunk======
This tab is only available when *Root Type* is set to either *Trunk Structure".

*Mult*:
    #id: internalname
    
    Scale width value uniformely for the trunk structure.

*Scale*:
    #id: internalname
    
    Change width of the trunk structure across branch length.
    
=====Leonardo's Scale=====

Scales branches width based on [Leonardo's rule|http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0093535].
Each branch width is equal to the sum of the its children branches width.
This tab is only available when *Width Type* is set to *Leonardo's Scale*.

*Tips Width*:
    #id: internalname
    
    Set width for tip branches. This will subsequently affect the parent branches until the root of the tree.
    The option is only available for *Single Points* or *Group Points* options.

~~~
====Resample====
Increase the resolution on a per branch basis.
Affects the skeleton of the tree.
    
*Segments*:
    #id: internalname
    
    The maximum number of edges in a branch.
    
~~~

====Variation====
Applies a random offset, within a specified scale, to the points of the tree geometry.
It achieves a more gnarled look for the final tree model.
Affects the skeleton on the tree.

TIP:
        #display: green
        :box:
            #dir: left
            #display: green      
            
            High value can create very sharp angles between consecutive branches.
            Counterbalance its effect with the *Smooth* parameters.


*Scale*:
    #id: internalname
    
    Overall scale of the offset to move the points.
    Points are jittered by a value of -0.5 to 0.5 times this scale,
    and then modified by the other scales.
    
*Axis Scale*:
    #id: internalname
    
    Each axis of jitter is scaled by the corresponding scale here.
    This can be used to achieve a two dimensional jitter by setting the unwanted axis to 0.
    
*Seed*:
    #id: internalname
    
    The random number seed used to generate the jitter values.
    Changing this will create a different set of jitter offsets.
    
    TIP:
        #display: green
        :box:
            #dir: left
            #display: green      
            
            If you want to populate a scene with small variations of this tree model,
            you can use a `copy_stamp` node and link a stamping variable based on `rand(@ptnum)`
            to this parameter.
    
~~~

====Smooth====

Smooths angles between consecutive notes achieving an overall more natural tree.
Useful to counterbalance the effect of the *Variation* parameters.

=====Branches=====

*Method*:
    #id: internalname
    
    Lets you choose different smoothing models that have different effects on the point positions.
    It affects the tree skeleton.

    *Uniform*: move points so they are evenly spaced.
    
    *Scale-Dominant*: move points trying to mainting their original relative distances from one another.
    
    *Curvature-Dominant*: move points to smooth the curvature while trying to maintain their original arrangement.
    
*Strength*:
    #id: internalname
    
    How much to smooth the selected points.
    Higher values move the points farther from their original positions.
    It affects the tree skeleton.
    
*Divisions*:
    #id: internalname
    
    This is the number of divisions in the circle which is
    to be swept over the polygon. It can vary on a point basis.
    It affects the tree polygon mesh.
    
*Segments*:
    #id: internalname
    
    The number of segments to divide each edge of the polygon into.
    It can vary on a point basis.
    It affects the tree polygon mesh.

=====Smooth Joints=====
This section interpolates the thicknes of the branches at the junction points.
It affects the tree polygon mesh.

*Method*:
    #id: internalname
    
    Lets you choose different smoothing models that have different effects on the point positions.

    *Uniform*: move points so they are evenly spaced.
    
    *Scale-Dominant*: move points trying to mainting their original relative distances from one another.
    
    *Curvature-Dominant*: move points to smooth the curvature while trying to maintain their original arrangement.
        
*Strength*:
    #id: internalname
    
    How much to smooth the selected points.
    Higher values move the points farther from their original positions.


~~~
~~~
===Leaves===

*Leaf Type*:
    #id: internalname
    
    Choose either default geometry or custom one.
    
    *Default Leaf*: use the built-in leaf geometry.
    
    *Custom Geometry*: select to use custom model for leaf geometry.

~~~
====Default Leaf====
This tab is only available when *Leaf Type* is set to *Default Leaf*.

*Uniform Scale*:
    #id: internalname
    
    Scale leaves along X, Y, Z axis at the same time.
    
====Custom Leaf====
This tab is only available when *Leaf Type* is set to *Custom Geometry*.

*Total Number*:
    #id: internalname
    
    Total count of leaves per branch tip.
    
=====Transform=====

*Translate*:
    #id: internalname
    
    Amount of rotation about xyz axes.
    
*Rotate*:
    #id: internalname
    
    Rotate the geometry by the specified angle around the x, y, z axis.

*Scale*:
    #id: internalname
    
    Scale the geometry along the x, y, z axis.
    
*Pivot*:
    #id: internalname
    
    Move the pivot to the specified coordinates.

*Uniform Scale*:
    #id: internalname
    
    Scale the input geometry uniformly along the x, y, z axis.

~~~
*Color Type*:
    #id: internalname
    
    Choose either plain color or select a shader from the shop.
    
    *Simple Color*: uniform color for leaf geometry.
    
    *Shading*: provides shader options.
    
====Color====
This tab is only available when *Color Type* is set to *Simple Color*.

*Color Type*:
    #id: internalname
    
    Set color for leaves.
    

====Shading====
This tab is only available when *Color Type* is set to *Shading*.

*Number of Materials*:
    #id: internalname
    
    The path of the material to assign. Click the [Smallicon:../../icons/BUTTONS/chooser_node.svg] chooser icon  to choose the material from a list.
    

~~~
~~~
~~~
